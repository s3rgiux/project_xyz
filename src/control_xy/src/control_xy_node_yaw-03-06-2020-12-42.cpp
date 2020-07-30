#include "ros/ros.h"
#include <std_msgs/String.h>
#include <std_msgs/Int16.h>
#include <std_msgs/Float32.h>
#include <std_msgs/Float64.h>
#include <geometry_msgs/Twist.h>
#include "sensor_msgs/LaserScan.h"
//#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>
#include "sensor_msgs/Joy.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h> 
float filter_yaw=0;


class test_head
{
public:
	test_head(ros::NodeHandle nh)
	{
	    
        	speed_publisher=nh.advertise<geometry_msgs::Twist>(nh.resolveName("/cmd_vel"), 2);
                head_subscriber = nh.subscribe("/euler", 1, &test_head::headCallback,this);
		odometry_sub = nh.subscribe("odom",1,&test_head::ReceiveOdometry,this);
                //odometry_sub = nh.subscribe("poseupdate",1,&test_head::ReceiveOdometry,this);
		joy_subscriber = nh.subscribe("/j0/joy", 1, &test_head::joyCallback,this);
		pose_subscriber = nh.subscribe("setPoints", 1, &test_head::setPointsCallback,this);
		ang_subscriber = nh.subscribe("peopAng", 1, &test_head::angPeopCallback,this);
		dist_subscriber = nh.subscribe("peopDist", 1, &test_head::distPeopCallback,this);
                obst_subscriber = nh.subscribe("/obstacle_closest", 1, &test_head::obstCallback,this);
                
		
		subScan_ = nh.subscribe("/scan", 1, &test_head::scanCallback,this);
		start_tray=false;
		sp_yaw=90;
		ca=0;
		ruta_learn=false;
		loaded_route=false;
		n_aux=3000;
		k_idx=0;
		px_aux=1000000000000;
		py_aux=1000000000000;
		carril=0;//0 externo 1 interno
		velocity=0;
		alfa=0.8;
		obstaculo=false;
		changed=false;
		errpx=0;
		errpy=0;
		error_yaw=0;
		px=0;
		py=0;
		nspx=0.00;
		nspy=0.05;
		yaw=0;
		conta=0;
		mode=1;
		start_route=false;
		loaded_route=false;
		obstacle_front=false;
		obstacle_front1=false;
		obstacle_front2=false;
		ruta_learn=false;
		save_waypoint=false;
		mod_seguir=false;
                newobstacle=false;
	}
	~test_head(){}
	


void setPointsCallback(const geometry_msgs::Twist& twist)
	{
	nspx=twist.linear.x;
	nspy=twist.linear.y;
        sp_yaw=-atan2(nspx,nspy)*180/3.1416;
	ROS_INFO("%f,%f,%f",nspx,nspy,sp_yaw);
	}

	void obstCallback(const std_msgs::Float32& msg)
	{
           if(msg.data==1){
              newobstacle=true;
           }else{
              newobstacle =false;
           }
	}

    void headCallback(const std_msgs::Float64& head)
	{	
	//contadorvel++;
	   //if(contadorvel%1==0){
		if(mode!=3){

			errpx=nspx-px;
			errpy=nspy-py;
			//sp_yaw=80;
			sp_yaw=atan2(errpx,errpy)*180/3.1416;
			//sp_yaw=-atan2(nspx,nspy)*180/3.1416;
			yaw=head.data;//head.data;//quitamos el offset
			//error_yaw=alfa*error_yaw+(1-alfa)*(sp_yaw-yaw);
			error_yaw=(sp_yaw-yaw);
			//ROS_INFO("%f,%f,%f,%f",errpx,errpy,error_yaw);
			if (error_yaw < -180.0 ){
				error_yaw=error_yaw+360;
			}else if (error_yaw > 180.0 ){
				error_yaw=error_yaw-360;
			}
			spVel=20*0.05*(error_yaw);
			nkp=40*0.3;//=0.0085;
			nkd=5*0.05;
			nki=0.002;
			errVelYaw=spVel-velyaw;
			intErr=intErr+errVelYaw;
			if(intErr>7){
				intErr=7;
			}
			if(intErr<-70){
				intErr=-7;
			}
			ctrl_yaw=(nkp*spVel);//-nkd*velyaw+nki*intErr;//+0.5*(error_yaw-last_error));//+0.5*(error_yaw-last_error));//2*(error_yaw);
				if(ctrl_yaw<2&&ctrl_yaw>-2||abs(error_yaw) <2){
				ctrl_yaw=0;
				}
				else if(ctrl_yaw>10){
						ctrl_yaw=10; 
				}else if(ctrl_yaw<-10){
						ctrl_yaw=-10;
				}
			//ROS_INFO("%f ,%f ,%f ",yaw,error_yaw,ctrl_yaw);
			nvkp=30*0.0095;//=0.0085;
			nvkd=30*0.04;
			spPos=sqrt((nspx*nspx)+(nspy*nspy));
			distAct=sqrt((px*px)+(py*py));
			if(error_yaw<10&&error_yaw>-10){
				conta++;
				if(conta>7){
				arrived=true;
				conta=0;
				}
			}
		
			if(error_yaw<10&&error_yaw>-10&&abs(spPos-distAct)>0.10&&arrived==true){
					spPVel=60*0.8*(spPos-distAct);
					errPVel=(spPVel-velx);
					ctrl_vel=60*5*errPVel;
			}else{
					ctrl_vel=0;
				arrived=false;
					if(start_route==true&&loaded_route==true&&abs(spPos-distAct)<=0.1){	 
						indx++;
						if(indx>=h){
						indx=h;}
					nspx=sp_rx[indx];
					nspy=sp_ry[indx];
					ROS_INFO("Llegue, nextwaypint %i,%f,%f",indx);
					}
			}

			if(ctrl_vel>60){
				ctrl_vel=60;
			}else if(ctrl_vel<-60){
				ctrl_vel=-60;
			}
			
			vel_steer.angular.z= ctrl_yaw;
			vel_steer.linear.x=abs(ctrl_vel);
			ROS_INFO("%f,%f,%f,%f,%f",errpx,errpy,error_yaw,ctrl_vel,errPVel); 
			if (mode!=1){
				if(obstacle_front==true){
					vel_steer.linear.x= 0;
				}
			speed_publisher.publish(vel_steer);
			}
		}//IFMODE3
          //}//contadorvel

	}

	void ReceiveOdometry(const nav_msgs::Odometry::ConstPtr& msg){
	    velyaw=msg->twist.twist.angular.z;
            px=msg->pose.pose.position.x;
    	    py=msg->pose.pose.position.y;
	    velx=msg->twist.twist.linear.x;

		if (ruta_learn==true){
    	    		norm=sqrt((px-px_aux)*(px-px_aux)+(py-py_aux)*(py-py_aux));
    	    		if (save_waypoint==true){
				save_waypoint=false;
    	    			fprintf(fp, "%f %f\n",px,py );
    	    			px_aux=px;
    	    			py_aux=py;
    	    			ROS_INFO("NP %f,%f",px,py); 
    	    		}
    		}
	    
      }

	void angPeopCallback(const std_msgs::Float32& msg){
		//ROS_INFO("%i,%f,%f",mode,msg.data,distanciaPeople);
		if(mode==3){
		   if(msg.data!=-500){
			geometry_msgs::Twist vel_steer;		
			if (msg.data>-5 && msg.data<5&& distanciaPeople<40){
                        	vel_steer.angular.z=0;
                        }else{	
				
				if(distanciaPeople<100){
					vel_steer.angular.z=5*msg.data;//*(distanciaPeople/40);
				   	if (vel_steer.angular.z>350){
                        			vel_steer.angular.z= 350;
				  	}else if (vel_steer.angular.z<-350){
                        			vel_steer.angular.z= -350;
					}
				}else{
				   	//vel_steer.angular.z=15*msg.data - vel_steer.angular.z/2;//*(distanciaPeople/40);
					vel_steer.angular.z=5*msg.data;
				   	if (vel_steer.angular.z>400){
                        			vel_steer.angular.z= 400;
				  	}else if (vel_steer.angular.z<-400){
                        			vel_steer.angular.z= -400;
					}
				}
			   if(distanciaPeople>60 && distanciaPeople<100){
				//vel_steer.linear.x=120;
				vel_steer.linear.x=5*distanciaPeople;
				if (vel_steer.linear.x>900){
                          		vel_steer.linear.x= 900;
				}
			   }else if(distanciaPeople>100){
				//vel_steer.linear.x=120;
				vel_steer.linear.x=10*distanciaPeople;
				if (vel_steer.linear.x>2000){
                          		vel_steer.linear.x= 2000;
                                }
			   }else{
				vel_steer.linear.x=0;
			   }
				
                        }
			//vel_steer.angular.z=0;
		        //if(obstacle_front){
                        //if(newobstacle){
                        //   vel_steer.linear.x=0;
                        //   vel_steer.angular.z= 0;
			//   speed_publisher.publish(vel_steer);
                        //   ros::Duration(1).sleep(); // sleep for half a second
                       // }
			
			speed_publisher.publish(vel_steer);
		  }else{
			vel_steer.linear.x= 0;
                        vel_steer.angular.z= 0;
			speed_publisher.publish(vel_steer);
		  }
	       }
	   
    }  

	void distPeopCallback(const std_msgs::Float32& msg){
		
			distanciaPeople=msg.data;
	   
    } 


    void scanCallback(const sensor_msgs::LaserScan::ConstPtr& scan)
	{
	    int count = scan->scan_time / scan->time_increment;
	    float  break_distance=1.5;

for(int i=0;i<=30;i++){
  if (scan->ranges[i] <= break_distance&& scan->ranges[i] >0.3){
     obstacle_front=true;
     ROS_INFO("Obstacle");
     return;
  }else{
     obstacle_front=false;
  }
}

for(int i=359;i<=329;i++){
  if (scan->ranges[i] <= break_distance&& scan->ranges[i] >0.3){
     obstacle_front=true;
     ROS_INFO("Obstacle");
     return;
  }else{
     obstacle_front=false;
  }
}
}


   void loadRoute(){
    	    char mystring [100];
			//ROS_INFO("Cargando Ruta");
			fp = fopen ("/home/xavier/catkin_ws/src/control_xy/ruta.txt" , "r");
			h=0;
			if (fp == NULL){ perror ("Error opening file");}
			h=0;
			while (1) {
       			 if (fgets(mystring,100, fp) == NULL){ 
       			 	break;
       			 }
        		 sscanf(mystring,"%s %s",&rx,&ry);
        		 sp_rx[h]=atof(rx);
        			sp_ry[h]=atof(ry);
        			
        			//printf("%3d: %s", h, mystring);
        			printf("R %f,%f \n",sp_rx[h],sp_ry[h]);
        			h++;
			}
			printf("Ruta cargada %d elementos\n ",h);
			
			num_sp=h;
			//determinar el mas cercano
			/*n_aux=30000;
			for (int at=0;at<num_sp;at++){
				err_xx=sp_rx[at]-px;
	        	err_yy=sp_ry[at]-py;
	        	
	        	if(sqrt(err_xx*err_xx+err_yy*err_yy)<n_aux){
	        		n_aux=sqrt(err_xx*err_xx+err_yy*err_yy);
	        		k_idx=at+1;
	        		if(k_idx>=num_sp){
	        			k_idx=0;
	        		}	        		
	        	}

			}
			printf("Siguiente SP %d, p%f,%f, sp%f,%f\n", k_idx,px,py,sp_rx[k_idx],sp_ry[k_idx] );*/
			loaded_route=true;

    }

    void joyCallback(const sensor_msgs::Joy::ConstPtr& joy)
	{
		geometry_msgs::Twist vel_steer;
 /*
		ROS_INFO("entre");
		if(joy->buttons[0]==1){
			ROS_INFO("button0");
		}
		if(joy->buttons[1]==1){
			ROS_INFO("button1");
		}
		if(joy->buttons[2]==1){
			ROS_INFO("button2");
		}
		if(joy->buttons[3]==1){
			ROS_INFO("button3");
		}
		if(joy->buttons[4]==1){
			ROS_INFO("button4");
		}
		if(joy->buttons[5]==1){
			ROS_INFO("button5");
		}
		if(joy->buttons[6]==1){
			ROS_INFO("button6");
		}
		if(joy->buttons[7]==1){
			ROS_INFO("button7");
		}
		if(joy->buttons[8]==1){
			ROS_INFO("button8");
		}
		if(joy->buttons[9]==1){
			ROS_INFO("button9");
		}
		if(joy->buttons[10]==1){
			ROS_INFO("button10");
		}
		if(joy->buttons[11]==1){
			ROS_INFO("button11");
		}
		if(joy->buttons[12]==1){
			ROS_INFO("button12");
		}
		if(joy->buttons[13]==1){
			ROS_INFO("button13");
		}
		if(joy->buttons[14]==1){
			ROS_INFO("button14");
		}
		if(joy->buttons[15]==1){
			ROS_INFO("button15");
		}
		if(joy->buttons[16]==1){
			ROS_INFO("button16");
		}
*/

		if (joy->buttons[4]==1&&joy->buttons[5]==1 ){//R1L1
			printf("Cargando Ruta \n");
			loadRoute();
			ros::Duration(0.2).sleep(); // sleep for half a second
		}else if(joy->buttons[13]&&loaded_route==true){//start
			start_route=true;
			ROS_INFO("Start");
			indx=0;
			nspx=sp_rx[indx];
			nspy=sp_ry[indx];
			mode=0;
			ros::Duration(0.3).sleep(); // sleep for half a second
		}else if(joy->buttons[13]&&loaded_route==true){//start
			start_route=false;
			ROS_INFO("Stop");
			mode=1;
			ros::Duration(0.3).sleep(); // sleep for half a second
		}else if(joy->buttons[6]==1&&joy->buttons[7]==1 && ruta_learn==false ){//L2R2
			fp = fopen ("/home/xavier/catkin_ws/src/control_xy/ruta.txt" , "w+");
			ruta_learn=true;
			ROS_INFO("Listo para comenzar a aprender la ruta");	
			ros::Duration(0.4).sleep(); // sleep for half a second
			px_aux=1000000000000;
		    py_aux=1000000000000;
		}else if(joy->buttons[6]==1&&joy->buttons[7]==1 && ruta_learn==true){
			
			ROS_INFO("Terminado de aprender la ruta");
			fclose(fp);	 
			ros::Duration(0.4).sleep(); // sleep for half a second
			ruta_learn=false;
		}else if (joy->buttons[2]==1 && ruta_learn ==true && save_waypoint==false){
			save_waypoint=true;
			ros::Duration(0.4).sleep(); // sleep for half a second
			

		}else if(joy->buttons[8]==1){//select
			
			mode++;
			if(mode==1){
				ROS_INFO("Manual");
				vel_steer.linear.x=0;
				vel_steer.angular.z=0;
				speed_publisher.publish(vel_steer);
				ros::Duration(0.3).sleep(); // sleep for half a second
			}else if (mode>1){
				mode=1;
				ROS_INFO("Waiting command");
				vel_steer.linear.x=0;
				vel_steer.angular.z=0;
				speed_publisher.publish(vel_steer);
				ros::Duration(0.3).sleep(); // sleep for half a second
			}
		}else if(joy->buttons[3]){//triangulo
			if(mod_seguir==false){
				ROS_INFO("Seguimiento objeto");
				vel_steer.linear.x=0;
				vel_steer.angular.z=0;
				speed_publisher.publish(vel_steer);
			    mode=3;
				ros::Duration(0.4).sleep(); // sleep for half a second
				mod_seguir=true;
			}else{
				ROS_INFO("Seguimiento objeto Terminado");

				vel_steer.linear.x=0;
				vel_steer.angular.z=0;
				speed_publisher.publish(vel_steer);
				mode=1;
				mod_seguir=false;
				ros::Duration(0.4).sleep(); // sleep for half a second	
			}
			
		}

		if(mode==1){
			
			vel_steer.linear.x=-joy->axes[1]*-1500;
			vel_steer.angular.z=joy->axes[0]*-800;
			//ROS_INFO("%f , %f",joy->axes[1]*80,joy->axes[1]*40);
			//std_msgs::Int16 steer;
			//steer.data=90+(joy->axes[2]*90);
			//if(obstacle_front==true){
			//		vel_steer.linear.x= 0;
			//	}
			
                        //if(newobstacle){
                        //if(obstacle_front){
                        //   vel_steer.linear.x=0;
                        //   vel_steer.angular.z= 0;
			   //speed_publisher.publish(vel_steer);
                           //ros::Duration(1).sleep(); // sleep for half a second
                        //}
                        speed_publisher.publish(vel_steer);
		}
		/*
		if(joy->buttons[5]==1&&joy->buttons[7]==1 && ruta_learn==false){
			fp = fopen ("ruta.txt", "w+");
			ruta_learn=true;
			ROS_INFO("Listo para comenzar a aprender la ruta");	
			px_aux=1000000000000;
		    py_aux=1000000000000; 
		}else if(joy->buttons[5]==1&&joy->buttons[7]==1 && ruta_learn==true){
			ruta_learn=false;
			ROS_INFO("Terminado de aprender la ruta");
			fclose(fp);	 
		}else if(joy->buttons[4]==1&&joy->buttons[5]==1 ){
			printf("Cargando Ruta \n");
			loadRoute();

		}else if(joy->buttons[6]==1){
        	start_tray=true;
        	speed.data=-1100;
        	speed_publisher.publish(speed);
        	
        }else if(joy->buttons[7]==1){
			start_tray=false;
			speed.data=0;
        	speed_publisher.publish(speed);
		}
		if(ruta_learn==true){

			std_msgs::Int16 speed;
		speed.data=-joy->axes[1]*1100;
		std_msgs::Int16 steer;
		steer.data=96+(joy->axes[0]*110);
		speed_publisher.publish(speed);
		steering_publisher.publish(steer);
		}*/
		
		}

	
private:

    ros::Subscriber head_subscriber;
	ros::Subscriber ang_subscriber;
	ros::Subscriber dist_subscriber;
    ros::Subscriber pose_subscriber;	
    ros::Publisher light_publisher;
    std_msgs::String light_command;
    ros::Publisher steering_publisher;
    std_msgs::Int16 steering_command;
    ros::Publisher speed_publisher;
    std_msgs::Int16 speed_command;
	ros::Subscriber subTwist_;
        ros::Subscriber obst_subscriber;
	ros::Subscriber odometry_sub;
	ros::Subscriber joy_subscriber;
	ros::Subscriber subScan_;
        geometry_msgs::Twist vel_steer;
		std_msgs::Float32 ang_people;
    int ca;
	int direction;
	bool mod_seguir;
	bool save_waypoint;
	float distanciaPeople;
	float angulo_seguimiento;
	float yaw;
	float error_yaw;
	float sp_yaw,sp_yaw2;
	float ctrl_yaw;
	float px,py,norm,norm2,x_ini,y_ini,x_p,y_p,px2,py2,spx,spy,err_x,err_y,err_xx,err_yy;
	char rx[80],ry[80],rx2[80],ry2[80],pa[80],yag[80];
	float sp_rx[1000],sp_ry[1000],sp_rx2[1000],sp_ry2[1000],param[1000],sp_yaww[1000];
	bool start_tray;
	int count,count2;
	bool loaded_route;
	int count_odo;
	FILE * fp;
	bool ruta_learn;
	float px_aux,py_aux;
	int num_sp;
	int k_idx;
	float n_aux;
	int carril;
	int velocity;
	float last_error,alfa;
	float velx,err2;
	ros::Time time_obst,time_cruce,time_obst_last,time_cruce_last;
	bool obstaculo,changed,crucero;
	float velyaw;
int contadorvel;
float intErr;
float velCtrl;

float errPos;
float nspx;
float nspy;

float errpx,errpy,spVel,nkp,nkd,nki,errVelYaw,nvkp,nvkd,spPos,distAct,errPVel,spPVel,ctrl_vel;
bool start_route;
int conta;
bool arrived,obstacle_front,obstacle_front1,obstacle_front2;
bool newobstacle;
int indx,h;
int mode;

};

int main(int argc, char **argv)
{
    ros::init(argc, argv, "heading_follow_node");
    ros::NodeHandle nh; 

    test_head test_head_obj(nh);
    //ros::Rate rate(0.5); //0.5 Hz, every 2 second
	ros::Rate rate(30); //100 Hz, every .01 second
    //printf("%f",-atan2(5,1)*180/3.1416);
	while(ros::ok())
	{
		
		ros::spinOnce();
		rate.sleep();
	}
    return 0;
}
