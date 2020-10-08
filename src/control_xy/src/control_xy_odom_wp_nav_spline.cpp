#include "ros/ros.h"
#include <std_msgs/String.h>
#include <std_msgs/Int16.h>
#include <std_msgs/Float32.h>
#include <std_msgs/Float64.h>
#include <geometry_msgs/Twist.h>
#include <geometry_msgs/Vector3.h>

#include "sensor_msgs/LaserScan.h"
//#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>
#include "sensor_msgs/Joy.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <control_xy/State.h>
#include <control_xy/Obstacle.h> 
#include <control_xy/TriggerAction.h> 
float filter_yaw=0;



class test_head
{
public:
	test_head(ros::NodeHandle nh)
	{
	    
        	speed_publisher=nh.advertise<geometry_msgs::Twist>(nh.resolveName("/cmd_vel"), 1);
		tracked_publisher=nh.advertise<geometry_msgs::Vector3>(nh.resolveName("/tracked"), 2);
		alerts_publisher=nh.advertise<std_msgs::Int16>(nh.resolveName("/alerts"), 1);
                head_subscriber = nh.subscribe("/euler", 1, &test_head::headCallback,this);
		odometry_sub = nh.subscribe("odom",1,&test_head::ReceiveOdometry,this);
                //odometry_sub = nh.subscribe("poseupdate",1,&test_head::ReceiveOdometry,this);
		joy_subscriber = nh.subscribe("/j0/joy", 1, &test_head::joyCallback,this);
		pose_subscriber = nh.subscribe("setPoints", 1, &test_head::setPointsCallback,this);
		ang_subscriber = nh.subscribe("peopAng", 1, &test_head::angPeopCallback,this);
		dist_subscriber = nh.subscribe("peopDist", 1, &test_head::distPeopCallback,this);
               // ang_subscriber2 = nh.subscribe("peopAng2", 3, &test_head::angPeopCallback2,this);
		//ang_subscriber2 = nh.subscribe("peopAng2", 2, &test_head::angPeopCallback3,this);
		ang_subscriber2 = nh.subscribe("peopAng2", 2, &test_head::angPeopCallback4,this);
                //ang_subscriber_cam = nh.subscribe("ang_peop_detect_img", 1, &test_head::angCamCallback,this);
		ang_subscriber_cam = nh.subscribe("ang_peop_detect_img", 1, &test_head::angCamCallback2,this);
		dist_subscriber2 = nh.subscribe("peopDist2", 1, &test_head::distPeopCallback2,this);
                obst_subscriber = nh.subscribe("/obstacle_closest", 1, &test_head::obstCallback,this);
                state_subscriber = nh.subscribe("/trigger_action", 1, &test_head::stateCallback,this);
		//nh.param<float>("break_distance", break_distance, 1.5);
		nh.getParam("/control_xy/break_distance", break_distance);
		nh.getParam("/control_xy/break_danger", break_danger);
		nh.getParam("/control_xy/low_vel_gain_karugamo", low_vel_gain);
		nh.getParam("/control_xy/high_vel_gain_karugamo", high_vel_gain);
		nh.getParam("/control_xy/low_vel_gain_follow", low_vel_gain_follow);
		nh.getParam("/control_xy/high_vel_gain_follow", high_vel_gain_follow);
		nh.getParam("/control_xy/frontal_gain_karugamo", frontal_gain_karugamo);
		nh.getParam("/control_xy/frontal_gain_follow", frontal_gain_follow);
		nh.getParam("/control_xy/frontal_gain_manual", frontal_gain_manual);
		nh.getParam("/control_xy/max_speed_karugamo", max_speed_karugamo);
		nh.getParam("/control_xy/max_speed_follow", max_speed_follow);
		nh.getParam("/control_xy/max_speed_manual", max_speed_manual);
                nh.getParam("/control_xy/max_speed_side_manual", max_speed_side_manual);
		nh.getParam("/control_xy/smooth_accel", smooth_accel);
		nh.getParam("/control_xy/radius_follow", radius_follow);
		//nh.param<float>("break_danger", break_danger, 0.45);
		subScan_ = nh.subscribe("/scan", 1, &test_head::scanCallback,this);
		ROS_INFO_STREAM("******break_distance "<< break_distance << " break danger " << break_danger << " low vel gain " << low_vel_gain << " high vel gain " << high_vel_gain
				<< " max_speed_follow " << max_speed_follow << " max_speed_manual " << max_speed_manual);
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
		missing_track=0;
		mode=1;
                ang_peop_cam=-500;
		aux_dist=8000;

		tracked_angle=0;
                ang_peop_lidar=0;
		distanciaPeople2=0;
		tracked_distance=0;
		cont_detect_peop=0;

		start_route=false;
		loaded_route=false;
		obstacle_front=false;
		obstacle_front1=false;
		obstacle_front2=false;
		ruta_learn=false;
		save_waypoint=false;
		
                newobstacle=false;
                col_avoid_mode=true;
		mode_idle=true;
		mode_manual=false;
		mode_karugamo=false;
                mode_follow=false;
                tracking_people=false;
		mode_auto=false;
		
		danger=false;
		free_way=true;
		collision = false;
		start_route = false;
		index_wp=-1;
		dist_auxwp=0;
	}
	~test_head(){}
	

void stateCallback(const control_xy::TriggerAction& data)
	{
		//ROS_INFO("Controlxy ");
		//ROS_INFO("%s ",data.trigger.c_str());
		if(data.trigger=="collision"){
			collision =true;
			vel_steer.linear.x= 0;
                        vel_steer.angular.z= 0;
			speed_publisher.publish(vel_steer);
			alerts_command.data=6;//6 collision 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			alerts_publisher.publish(alerts_command);
			mode_idle=false;
			mode_manual=false;
			mode_karugamo=false;
			mode_follow=false;
			danger=false;
			free_way=false;
			collision = true;
			ctrl_front_follow= 0;
			ctrl_ang= 0;
			ctrl_front_manual= 0;
			ctrl_side_manual= 0;
			
		//	ROS_INFO("Yuhu");
		//	ROS_INFO("%s ",data.trigger.c_str());
		}else if(data.trigger=="break_release_button_on"){
			collision = false;
			mode_idle=true;
			mode_manual=false;
			mode_karugamo=false;
			mode_follow=false;
			danger=false;
			free_way=true;
			ctrl_front_follow= 0;
			ctrl_ang= 0;
			ctrl_front_manual= 0;
			ctrl_side_manual= 0;
			alerts_command.data=2;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			alerts_publisher.publish(alerts_command);
			vel_steer.linear.x= 0;
                        vel_steer.angular.z= 0;
			speed_publisher.publish(vel_steer);
                        tracked_angle=0;
                        ang_peop_lidar=0;
			distanciaPeople2=0;
			tracked_distance=0;
		//	ROS_INFO("Yuhu");
		//	ROS_INFO("%s ",data.trigger.c_str());
		}
	}
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
	ang_robot=head.data;
	//contadorvel++;
	   //if(contadorvel%1==0){
		//if(mode!=3){
		if(start_route and mode_auto){
		
			errpx=nspx-px;
			errpy=nspy-py;
			//sp_yaw=80;
			//sp_yaw=atan2(errpx,errpy)*180/3.1416;
			sp_yaw=-atan2(errpy,-errpx)*180/3.1416;
			////TEsts
/*
			ROS_INFO("Test1 front -1.7,0");
			errpx=-1.7-px;
			errpy=0-py;
			//sp_yaw=atan2(errpx,errpy)*180/3.1416;
			sp_yaw=atan2(-errpy,-errpx)*180/3.1416;
			ROS_INFO("R %f,%f,%f",errpx,errpy,sp_yaw);
			ROS_INFO("Test2 side 0 1.7");
			errpx=0-px;
			errpy=1.7-py;
			//sp_yaw=atan2(errpx,errpy)*180/3.1416;
			sp_yaw=atan2(-errpy,-errpx)*180/3.1416;
			ROS_INFO("R %f,%f,%f",errpx,errpy,sp_yaw);
		
			ROS_INFO("Test3 back 1.7 0");
			errpx=1.7-px;
			errpy=0-py;
			//sp_yaw=atan2(errpx,errpy)*180/3.1416;
			sp_yaw=atan2(-errpy,-errpx)*180/3.1416;
			ROS_INFO("R %f,%f,%f",errpx,errpy,sp_yaw);
			//sp_yaw=80;
			ROS_INFO("Test4 side 0 -1.7");
			errpx=0-px;
			errpy=-1.7-py;
			//sp_yaw=atan2(errpx,errpy)*180/3.1416;
			sp_yaw=atan2(-errpy,-errpx)*180/3.1416;
			ROS_INFO("R %f,%f,%f",errpx,errpy,sp_yaw);
		*/	
			
			//sp_yaw=-atan2(nspx,nspy)*180/3.1416;
			yaw=head.data;//head.data;//quitamos el offset
			//error_yaw=alfa*error_yaw+(1-alfa)*(sp_yaw-yaw);
			error_yaw=-(sp_yaw-yaw);
			ROS_INFO("epx %f,epy %f, ey %f, spy %f , y %f ",errpx,errpy,error_yaw,sp_yaw,yaw);
			if (error_yaw < -180.0 ){
				error_yaw=error_yaw+360;
			}else if (error_yaw > 180.0 ){
				error_yaw=error_yaw-360;
			}
			spVel=0.05*(error_yaw);
			nkp=190;//=0.0085;
			nkd=1;
			nki=0;
			errVelYaw=spVel-velyaw;
			intErr=intErr+errVelYaw;
			if(intErr>7){
				intErr=7;
			}
			if(intErr<-7){
				intErr=-7;
			}
			ctrl_yaw=(nkp*spVel);//-nkd*velyaw+nki*intErr;//+0.5*(error_yaw-last_error));//+0.5*(error_yaw-last_error));//2*(error_yaw);
				if(ctrl_yaw<7&&ctrl_yaw>-7||abs(error_yaw) <2){
				ctrl_yaw=0;
				}
				else if(ctrl_yaw>400){
						ctrl_yaw=400; 
				}else if(ctrl_yaw<-400){
						ctrl_yaw=-400;
				}
			//ROS_INFO("%f ,%f ,%f ",yaw,error_yaw,ctrl_yaw);
			nvkp=1;//=0.0085;
			nvkd=1;
			spPos=sqrt((nspx*nspx)+(nspy*nspy));
			distAct=sqrt((px*px)+(py*py));
			if(error_yaw<8&&error_yaw>-8){
				conta++;
				if(conta>7){
				arrived=true;
				conta=0;
				}
			}
		
			if(error_yaw<10&&error_yaw>-10&&abs(spPos-distAct)>0.10&&arrived==true){
					spPVel=1000*(spPos-distAct);
					errPVel=(spPVel-velx);
					ctrl_vel=3*errPVel;
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

			if(ctrl_vel>600){
				ctrl_vel=600;
			}else if(ctrl_vel<-600){
				ctrl_vel=-600;
			}
			
			vel_steer.angular.z= ctrl_yaw;
			vel_steer.linear.x=abs(ctrl_vel);
			//ROS_INFO("%f,%f,%f,%f,%f",errpx,errpy,error_yaw,ctrl_vel,errPVel); 
			if( danger){
				vel_steer.linear.x= 0;
                        	vel_steer.angular.z= 0;
				speed_publisher.publish(vel_steer);
				alerts_command.data=4;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     				alerts_publisher.publish(alerts_command);
		        }
			speed_publisher.publish(vel_steer);
			//}
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
		if(mode_karugamo && danger!=true){
		   if(msg.data!=-500){
			geometry_msgs::Twist vel_steer;		
			if (msg.data>-7 && msg.data<7&& distanciaPeople<95){
                        	vel_steer.angular.z=0;
                        }else{	
				
				if(distanciaPeople<120){
					ctrl_ang= low_vel_gain*msg.data-ctrl_ang/2;
					vel_steer.angular.z=ctrl_ang;//low_vel_gain*msg.data;//*(distanciaPeople/40);
				   	if (vel_steer.angular.z>400){
                        			vel_steer.angular.z= 400;
				  	}else if (vel_steer.angular.z<-400){
                        			vel_steer.angular.z= -400;
					}
				}else{
				   	//vel_steer.angular.z=15*msg.data - vel_steer.angular.z/2;//*(distanciaPeople/40);
					ctrl_ang= high_vel_gain*msg.data-ctrl_ang/2;
					vel_steer.angular.z=ctrl_ang;//vel_steer.angular.z=high_vel_gain*msg.data;
				   	if (vel_steer.angular.z>500){
                        			vel_steer.angular.z= 500;
				  	}else if (vel_steer.angular.z<-500){
                        			vel_steer.angular.z= -500;
					}
				}
			   if(distanciaPeople>95 && distanciaPeople<=150){
				ctrl_front_karugamo=frontal_gain_karugamo*distanciaPeople-ctrl_front_karugamo/2;
				if (ctrl_front_karugamo>(max_speed_karugamo/2)){
                          		ctrl_front_karugamo= max_speed_karugamo/2;
				}
				vel_steer.linear.x= ctrl_front_karugamo;
			   }else if(distanciaPeople>150){
				ctrl_front_karugamo=frontal_gain_karugamo*distanciaPeople-ctrl_front_karugamo/2;
				if (ctrl_front_karugamo>(max_speed_karugamo)){
                          		ctrl_front_karugamo= max_speed_karugamo;
				}
				vel_steer.linear.x= ctrl_front_karugamo;
			   }else{
				vel_steer.linear.x=0;
			   }
				
                        }
			
		        if(obstacle_front && col_avoid_mode){
                        //if(newobstacle && col_avoid_mode){
                           vel_steer.linear.x=0;
                        //   vel_steer.angular.z= 0;
			   speed_publisher.publish(vel_steer);
                           ros::Duration(1).sleep(); // sleep for half a second
                        }else if(danger && col_avoid_mode){
                           vel_steer.linear.x=0;
                           vel_steer.angular.z= 0;
			   speed_publisher.publish(vel_steer);
                           ros::Duration(1).sleep(); // sleep for half a second			
			}
			alerts_command.data=4;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			alerts_publisher.publish(alerts_command);
			speed_publisher.publish(vel_steer);
		  }else if( danger){
			vel_steer.linear.x= 0;
                        vel_steer.angular.z= 0;
			speed_publisher.publish(vel_steer);
			alerts_command.data=4;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			alerts_publisher.publish(alerts_command);
		  }else{
		  	vel_steer.linear.x= 0;
                        vel_steer.angular.z= 0;
			speed_publisher.publish(vel_steer);
			alerts_command.data=4;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			alerts_publisher.publish(alerts_command);
		  }

	       }//mode3
	   
    }  

	void distPeopCallback(const std_msgs::Float32& msg){
		
			distanciaPeople=msg.data;
	   
    	} 

	void distPeopCallback2(const std_msgs::Float32& msg){
		
			distanciaPeople2=msg.data;
	   
    	} 


  void angCamCallback2(const std_msgs::Float32& msg){
                ang_peop_cam=msg.data;
		if(ang_peop_cam!=-500 && mode_follow && tracking_people==false ){
		       cont_detect_peop+=1;
			if(ang_peop_lidar<ang_peop_cam+6 && ang_peop_lidar> ang_peop_cam-6  && distanciaPeople2<aux_dist ){
				//cont_detect_peop+=1;
				aux_dist = distanciaPeople2;
				ROS_INFO("Tracked angle %f",ang_peop_lidar);
				tracked_cx=cx;
				tracked_cy=cy;
				tracked_pos.x=cx;
				tracked_pos.y=cy;
				tracked_pos.z= ang_peop_lidar;
				tracked_angle=ang_peop_lidar;
				
			}
			if(cont_detect_peop>4){
				tracking_people=true;
				cont_detect_peop=0;
                                	tracked_distance=distanciaPeople2;
					tracking_people=true;
					aux_dist=5000;
					missing_track=0;
					tracked_publisher.publish(tracked_pos);
                                	ctrl_front_follow= 0;
			        	ctrl_ang=0;
			        	vel_steer.linear.x= 0;
                                	vel_steer.angular.z= 0;
					cont_sp_follow=0;
					kf=0;
					
					//fp = fopen ("/home/xavier/catkin_ws/src/control_xy/people.txt" , "w+");

				}
		}
       }


/*
Pitakuru coordinate system and angles w.r.t Robot
		-x 0deg
		|
		|
		|
	
  90deg	-y--------------- y  -90deg
		|
		|
		|
		|
		|
	 179deg x -179 deg       
*/





void angPeopCallback4(const geometry_msgs::Vector3& msg){

int num_wp=6;
cicles=20;

cx = msg.x;//pos people or object
cy = msg.y;//pos people or object
ang_peop_lidar = 90+ atan2(cx, cy) * 180 / 3.1416 ;
spx_saved[0]=-0.4;
spy_saved[0]=0.02;
spx_saved[1]=-0.9;
spy_saved[1]=-.2;
spx_saved[2]=-0.9;
spy_saved[2]=-0.5;
spx_saved[3]=-0.9;
spy_saved[3]=-0.9;
spx_saved[4]=-1.2;
spy_saved[4]=-1.1;

spx_saved[5]=-1.7;
spy_saved[5]=-1.1;

if(mode_follow && danger!=true){
		///////////////New algorithm
                 //index_wp=-1;
		//dist_auxwp=0;
		  if(dist_auxwp<0.5){
			index_wp++;
			if(index_wp>=(num_wp-1)){
				index_wp=num_wp-1;
			}
			
			float c=0.05;//must be 1/cicles
			float p0x=px;//pos robot x
			float p0y=py;//pos robot y
			float p1x=spx_saved[index_wp];//spx_follow_old;//first wp
			float p1y=spy_saved[index_wp];//spy_follow_old;//first wp
			float p2x=spx_saved[index_wp+1];//spx_follow_new;//second wp
			float p2y=spy_saved[index_wp+1];//spy_follow_new;//second wp
			float aux1=px;//first should be pos robot x
			float aux2=py;//first should be pos robot y
			float Rx,Ry;
			float angle;
			ROS_INFO("************");
			for(int i=0;i<cicles;i++){
				float Q0x=p0x-p0x*i*c+i*c*p1x;
				float Q0y=p0y-p0y*i*c+i*c*p1y;
				float Q1x=p1x-p1x*i*c+i*c*p2x;
				float Q1y=p1y-p1y*i*c+i*c*p2y;
				Rx=Q0x-Q0x*i*c+i*c*Q1x;
				Ry=Q0y-Q0y*i*c+i*c*Q1y;
				spx_follow[i]=Rx;
				spy_follow[i]=Ry;
				//angle= atan2(Ry-aux2,Rx-aux1) * 180 / 3.1416;//angle wrt robot
				angle= -atan2((Ry-aux2),-(Rx-aux1)) * 180 / 3.1416;//angle wrt robot
				angle_follow[i]=angle;
				aux1=Rx;
				aux2=Ry;
				ROS_INFO("Rcalc %f,%f,%f",Rx,Ry,angle);
			}
		   }
		   dist_auxwp=sqrt((spx_follow[19]-px)*(spx_follow[19]-px)+(spy_follow[19]-py)*(spy_follow[19]-py));//calc dist for next loop

		        float auxdis=700000;
			for(int i=0;i<cicles;i++){//search for the nearest point in the created spline
				float errdist=sqrt((spx_follow[i]-px)*(spx_follow[i]-px)+(spy_follow[i]-py)*(spy_follow[i]-py));
				if(errdist<auxdis){
					indice=i+1;
					auxdis=errdist;
				}
			}
			
			ROS_INFO("***********");
			////////////
			errpx=spx_follow[indice]-px;
			errpy=spy_follow[indice]-py;
			sp_yaw=angle_follow[indice+1];
			
			if(sqrt((errpx*errpx)+(errpy*errpy))<0.2){
				indice++;
				if (indice>19){
					indice=19;
				}
			}
			
			error_yaw=-(sp_yaw-ang_robot);
			//ROS_INFO("epx %f,epy %f, ey %f, spy %f , y %f ",errpx,errpy,error_yaw,sp_yaw,yaw);
			if (error_yaw < -180.0 ){
				error_yaw=error_yaw+360;
			}else if (error_yaw > 180.0 ){
				error_yaw=error_yaw-360;
			}
			spVel=0.1*(error_yaw);//0.05*(error_yaw);
			nkp=140;//=0.0085;
			//nkd=1;
			//nki=0;
			ROS_INFO("sp %f %f, R %f %f, YSP %f %f\n",spx_follow[indice],spy_follow[indice],px,py,ang_robot,sp_yaw);
			fprintf(fp, "sp %f %f, R %f %f, YSP %f %f\n",spx_follow[indice],spy_follow[indice],px,py,ang_robot,sp_yaw);
			ctrl_yaw=(nkp*spVel);//
				if(ctrl_yaw>400){
						ctrl_yaw=400; 
				}else if(ctrl_yaw<-400){
						ctrl_yaw=-400;
				}
				
			ctrl_front_follow=350;
			vel_steer.linear.x= ctrl_front_follow;
			vel_steer.angular.z= ctrl_yaw;
			speed_publisher.publish(vel_steer);
   }

	}

/*
void angPeopCallback4(const geometry_msgs::Vector3& msg){
                //px pos robot
		//py pos robot
		//ang_robot 
		cx = msg.x;//pos people or object
		cy = msg.y;//pos people or object
		ang_peop_lidar = 90+ atan2(cx, cy) * 180 / 3.1416 ;
		distanciaPeople2 = sqrt(cx*cx+cy*cy)*100;

		if(mode_follow && danger!=true){ //&& tracking_people){//1
		   
		 if( cx!=0.01 && cy !=0.01 && tracking_people && cx<=(tracked_cx+radius_follow) && cx>=(tracked_cx-radius_follow) && cy<=(tracked_cy+radius_follow) && cy >=(tracked_cy-radius_follow)){//2
			ang_peop_lidar = 90 + atan2(cx, cy) * 180 / 3.1416;
			distanciaPeople2 = sqrt(cx*cx+cy*cy)*100;
                        //ROS_INFO("T%f,%f",tracked_cx,tracked_cy);
                        tracked_angle= ang_peop_lidar;
			tracked_distance = distanciaPeople2;
			missing_track=0;
			tracked_cx=cx;
			tracked_cy=cy;
			tracked_pos.x=cx;
			tracked_pos.y=cy;
			tracked_pos.z=tracked_angle;
			tracked_publisher.publish(tracked_pos);
                     	geometry_msgs::Twist vel_steer;		
			//ctrl_ang= low_vel_gain_follow*ang_peop_lidar-ctrl_ang/2;
			/////////////////////////new implement
			float dobs,angobs,npcx,npcy;
			dobs=sqrt(tracked_cx*tracked_cx+tracked_cy*tracked_cy);
			angobs=atan2(-tracked_cy,-tracked_cx)*180/3.1416;
			//px,py, ang_robot position robot
			npcx=px-dobs*(cos((angobs+ang_robot)*3.1416/180));//#rcx+ocx*(cos((angobs+angr)*3.1416/180))
			npcy=py-dobs*(sin((angobs+ang_robot)*3.1416/180));//#rcy+ocy*(sin((angobs+angr)*3.1416/180))
			//ROS_INFO("T%f,%f,%f,%f",tracked_cx,tracked_cy,npcx,npcy);
			if(sqrt((npcx-prev_cx)*(npcx-prev_cx)+(npcy-prev_cy)*(npcy-prev_cy))>0.45){
			     if(cont_sp_follow<1){//if it is the first then prevoius and new are the same
				spx_follow_old=npcx;//the same position for the first time detection
				spy_follow_old=npcy;//the same position to 
                                spx_follow_new=npcx;
				spy_follow_new=npcy;
				//spx_follow[cont_sp_follow]=npcx;
				//spy_follow[cont_sp_follow]=npcy;
				ROS_INFO("added %f,%f",npcx,npcy);
				fprintf(fp, "Robot %f %f %f, Objeto %f %f, Poscalc %f %f \n",px,py,ang_robot,tracked_cx,tracked_cy,npcx,npcy );
				prev_cx=npcx;
				prev_cy=npcy;
				cont_sp_follow++;
				
			      }else{
				spx_follow_old=spx_follow_new;//the same position for the first time detection
				spy_follow_old=spy_follow_new;//the same position to 
                                spx_follow_new=npcx;
				spy_follow_new=npcy;
				ROS_INFO("added %f,%f",npcx,npcy);
				fprintf(fp, "Robot %f %f %f, Objeto %f %f, Poscalc %f %f \n",px,py,ang_robot,tracked_cx,tracked_cy,npcx,npcy );
			      }
			  }
			////////////
		//if(distanciaPeople2>110 ){
		//if(tracking_people==true){
		if(true){
			///////////////New algorithm
			int cicles=1;
			float c=0.05;//must be 1/cicles
			float p0x=px;//pos robot x
			float p0y=py;//pos robot y
			float p1x=-1.2;//spx_follow_old;//first wp
			float p1y=-1.2;//spy_follow_old;//first wp
			float p2x=-1.2;//spx_follow_new;//second wp
			float p2y=-1.2;//spy_follow_new;//second wp
			float aux1=px;//first should be pos robot x
			float aux2=py;//first should be pos robot y
			float Rx,Ry;
			float angle;
			for(int i=0;i<cicles;i++){
				float Q0x=p0x-p0x*i*c+i*c*p1x;
				float Q0y=p0y-p0y*i*c+i*c*p1y;
				float Q1x=p1x-p1x*i*c+i*c*p2x;
				float Q1y=p1y-p1y*i*c+i*c*p2y;
				Rx=Q0x-Q0x*i*c+i*c*Q1x;
				Ry=Q0y-Q0y*i*c+i*c*Q1y;
				angle= atan2(Ry-aux2,Rx-aux1) * 180 / 3.1416;//angle wrt robot
				aux1=Rx;
				aux2=Ry;
				ROS_INFO("Rcalc %f,%f,%f",Rx,Ry,angle);
			}
			////////////
			errpx=Rx-px;
			errpy=Ry-py;
			sp_yaw=angle;
			//sp_yaw=-atan2(errpy,-errpx)*180/3.1416;//use the angle calculated before instead of this
			error_yaw=-(sp_yaw-ang_robot);
			//ROS_INFO("epx %f,epy %f, ey %f, spy %f , y %f ",errpx,errpy,error_yaw,sp_yaw,yaw);
			if (error_yaw < -180.0 ){
				error_yaw=error_yaw+360;
			}else if (error_yaw > 180.0 ){
				error_yaw=error_yaw-360;
			}
			spVel=0.05*(error_yaw);
			nkp=140;//=0.0085;
			//nkd=1;
			//nki=0;
			fprintf(fp, "F %f %f, R %f %f, YSP %f %f\n",spx_follow[kf],spy_follow[kf],px,py,ang_robot,sp_yaw);
			ctrl_yaw=(nkp*spVel);//-nkd*velyaw+nki*intErr;//+0.5*(error_yaw-last_error));//+0.5*(error_yaw-last_error));//2*(error_yaw)				
				if(ctrl_yaw>400){
						ctrl_yaw=400; 
				}else if(ctrl_yaw<-400){
						ctrl_yaw=-400;
				}
			
			nvkp=1;//=0.0085;
			nvkd=1;
			//spPos=sqrt((spx_follow[kf]*spx_follow[kf])+(spy_follow[kf]*spy_follow[kf]));
			spPos=sqrt((spx_follow_new*spx_follow_new)+(spy_follow_new*spy_follow_new));
			distAct=sqrt((px*px)+(py*py));
			
			//if(distanciaPeople2>110){
			if(true){			
			 	//ctrl_front_follow=(1-smooth_accel)*(frontal_gain_follow*(distanciaPeople2-110))+		   (smooth_accel*ctrl_front_follow);
				ctrl_front_follow=500;
				if (ctrl_front_follow>(max_speed_follow)){
                          		ctrl_front_follow= max_speed_follow;
				}
				vel_steer.linear.x= ctrl_front_follow;
			   }else{
				vel_steer.linear.x=0;
				ctrl_front_follow=0;
			   }
					


//vel_steer.linear.x=400;
			        if((spPos-distAct)<=0.3){	 
					//indx++;
 					fprintf(fp, "llegue wp %i sigueinte %i , %f ,%f numwp = %i \n",kf, kf+1, spx_follow[kf+1],spy_follow[kf+1],cont_sp_follow);
					kf++;
					
				if(kf>=250000){
				    kf=0;}
				//nspx=sp_rx[indx];
				//nspy=sp_ry[indx];
				//ROS_INFO("Llegue, nextwaypint %i,%f,%f",indx);
					}
			//}

			
			
			vel_steer.angular.z= ctrl_yaw;
			//vel_steer.linear.x=abs(ctrl_vel);
			//ROS_INFO("%f,%f,%f,%f,%f",errpx,errpy,error_yaw,ctrl_vel,errPVel); 
			if( danger){
				vel_steer.linear.x= 0;
                        	vel_steer.angular.z= 0;
				speed_publisher.publish(vel_steer);
				alerts_command.data=4;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     				alerts_publisher.publish(alerts_command);
		        }
			speed_publisher.publish(vel_steer);


/////////////////////////////////////////////

	

                   }//end contador

		  }else{
                        missing_track+=1;
                        if(missing_track>=25){//thiscounter also can help to see if theres a lot of objects and its not able to follow
				ROS_INFO("LOST");
				tracking_people=false;
				missing_track=0;
				tracked_cx=0;
				tracked_cy=0;
				aux_dist=5000;
				tracked_pos.x=-50;
				tracked_pos.y=-50;

				missing_track=0;
				cont_detect_peop=0;
			        tracking_people=false;
				//ctrl_front_follow= 0;
				ctrl_front_follow=(1-smooth_accel)*(-400)+(smooth_accel*ctrl_front_follow);//smooth slow down
				if(ctrl_front_follow<14){
					ctrl_front_follow= 0;				      
				}
				ctrl_ang= (1-smooth_accel)*(0)+(smooth_accel*ctrl_ang);//smooth slow down
		  		vel_steer.linear.x= ctrl_front_follow;
                        	vel_steer.angular.z= 0;
				tracked_cx=0;
				tracked_cy=0;
				aux_dist=5000;
				speed_publisher.publish(vel_steer);
				alerts_command.data=7;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     				alerts_publisher.publish(alerts_command);

				tracked_pos.x=-50;
				tracked_pos.y=-50;
				tracked_publisher.publish(tracked_pos);


				alerts_command.data=4;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     				alerts_publisher.publish(alerts_command);

			}

			//7777777777777777777777777777777777777


	if(cont_sp_follow>=2 && kf < cont_sp_follow){
		

			errpx=spx_follow[kf]-px;
			errpy=spy_follow[kf]-py;
			sp_yaw=-atan2(errpy,-errpx)*180/3.1416;
			error_yaw=-(sp_yaw-ang_robot);
			
			if (error_yaw < -180.0 ){
				error_yaw=error_yaw+360;
			}else if (error_yaw > 180.0 ){
				error_yaw=error_yaw-360;
			}
			spVel=0.05*(error_yaw);
			
			fprintf(fp, "lost F %f %f, R %f %f, YSP %f %f\n",spx_follow[kf],spy_follow[kf],px,py,ang_robot,sp_yaw);
			ctrl_yaw=(nkp*spVel);//-nkd*velyaw+nki*intErr;//+0.5*(error_yaw-last_error));//+0.5*(error_yaw-last_error));//2*(error_yaw);

				if(ctrl_yaw>400){
						ctrl_yaw=400; 
				}else if(ctrl_yaw<-400){
						ctrl_yaw=-400;
				}

			nvkp=1;//=0.0085;
			nvkd=1;
			spPos=sqrt((spx_follow[kf]*spx_follow[kf])+(spy_follow[kf]*spy_follow[kf]));
			distAct=sqrt((px*px)+(py*py));
			

				vel_steer.linear.x=500;
				ctrl_front_follow=500;
					

			        if((spPos-distAct)<=0.3){	 
					//indx++;
					fprintf(fp, "lost llegue wp %i sigueinte %i , %f ,%f numwp = %i \n",kf, kf+1, spx_follow[kf+1],spy_follow[kf+1],cont_sp_follow);
					kf++;
					if(kf>=250000){
				    		kf=0;
					}

				}

			vel_steer.angular.z= ctrl_yaw;
			
			if( danger){
				vel_steer.linear.x= 0;
                        	vel_steer.angular.z= 0;
				speed_publisher.publish(vel_steer);
				alerts_command.data=4;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     				alerts_publisher.publish(alerts_command);
		        }
			speed_publisher.publish(vel_steer);

                   }else{//lost and finished last wp
			vel_steer.angular.z= 0;
			vel_steer.linear.x= 0;
			speed_publisher.publish(vel_steer);
			}
//77777777777777777777777777777777777777
			
                        
		  }

	       }//mode3
	   
    }  



*/



    void scanCallback(const sensor_msgs::LaserScan::ConstPtr& scan)
	{
	    int count = scan->scan_time / scan->time_increment;
	    //float  break_distance=1.5;
            //float  break_danger=0.5;
		for(int j=329;j<=358;j++){
  			if (scan->ranges[j] <= break_danger && scan->ranges[j] >0.24 && mode_idle==false){
     				danger=true;
				free_way=false;
     				ROS_INFO("Danger1");
				alerts_command.data=5;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			        alerts_publisher.publish(alerts_command);
				if (mode_manual && ctrl_front_manual >0){
				   ctrl_front_manual=0;
				   ctrl_side_manual=0;
				    vel_steer.linear.x= 0;
                        	    vel_steer.angular.z= 0;
				    speed_publisher.publish(vel_steer);
				}else if(mode_follow){
				    ctrl_front_follow=0;
				    ctrl_front_karugamo=0;
			            ctrl_ang=0;
				    vel_steer.linear.x= 0;
                        	    vel_steer.angular.z= 0;
				    speed_publisher.publish(vel_steer);
				}else if(mode_auto){
				    ctrl_front_follow=0;
				    ctrl_front_karugamo=0;
			            ctrl_ang=0;
				    vel_steer.linear.x= 0;
                        	    vel_steer.angular.z= 0;
				    speed_publisher.publish(vel_steer);
				}
				
				return;
	  		}else{
				free_way=true;
				if(mode_manual && danger){
					danger=false;
					alerts_command.data=1;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     					alerts_publisher.publish(alerts_command);
				} if(mode_karugamo && danger){
					danger=false;
					alerts_command.data=3;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     					alerts_publisher.publish(alerts_command);
				}
				if(mode_follow && danger){
					danger=false;
					alerts_command.data=8;//8 follow 5 danger 4 warning 3 karugamo 2 idle 1 manual
     					alerts_publisher.publish(alerts_command);
				} if(mode_auto && danger){
				    danger=false;
					alerts_command.data=3;//8 follow 5 danger 4 warning 3 karugamo 2 idle 1 manual
     					alerts_publisher.publish(alerts_command);
				}
			        //danger=false;
  			}
		}

		for(int i=0;i<=30;i++){
  			if (scan->ranges[i] <= break_danger && scan->ranges[i] >0.24 && mode_idle==false){
     				danger=true;
				free_way=false;
     				ROS_INFO("Danger2");
				alerts_command.data=5;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			        alerts_publisher.publish(alerts_command);
				if (mode_manual && ctrl_front_manual >0){
				   ctrl_front_manual=0;
				   ctrl_side_manual=0;
				    vel_steer.linear.x= 0;
                        	    vel_steer.angular.z= 0;
				    speed_publisher.publish(vel_steer);
				}else if(mode_follow){
				    ctrl_front_follow=0;
				    ctrl_front_karugamo=0;
			            ctrl_ang=0;
				    vel_steer.linear.x= 0;
                        	    vel_steer.angular.z= 0;
				    speed_publisher.publish(vel_steer);
				}else if(mode_auto){
				    ctrl_front_follow=0;
				    ctrl_front_karugamo=0;
			            ctrl_ang=0;
				    vel_steer.linear.x= 0;
                        	    vel_steer.angular.z= 0;
				    speed_publisher.publish(vel_steer);
				}
			
				
				
				return;
	  		}else{
				free_way=true;
				if(mode_manual && danger){
					danger=false;
					alerts_command.data=1;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     					alerts_publisher.publish(alerts_command);
				} if(mode_karugamo && danger){
					danger=false;
					alerts_command.data=3;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     					alerts_publisher.publish(alerts_command);
				} if(mode_follow && danger){
					danger=false;
					alerts_command.data=7;//7 follow 5 danger 4 warning 3 karugamo 2 idle 1 manual
     					alerts_publisher.publish(alerts_command);
				}if(mode_auto && danger){
				    danger=false;
					alerts_command.data=3;//8 follow 5 danger 4 warning 3 karugamo 2 idle 1 manual
     					alerts_publisher.publish(alerts_command);
				}
			        //danger=false;
  			}
		}
/*
		for(int i=0;i<=30;i++){
  			if (scan->ranges[i] <= break_distance&& scan->ranges[i] >0.5 && mode_idle==false){
     				obstacle_front=true;
     				ROS_INFO("Warning");
				alerts_command.data=4;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			        alerts_publisher.publish(alerts_command);
				return;
	  		}else{
				free_way=true;
			        //obstacle_front=false;
  			}
		}

		for(int i=359;i<=329;i++){
			if (scan->ranges[i] <= break_distance&& scan->ranges[i] >0.5 && mode_idle==false){
			     obstacle_front=true;
			     ROS_INFO("Warning");
			     alerts_command.data=4;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			        alerts_publisher.publish(alerts_command);
			     return;
			  }else{
			     obstacle_front=false;
			  }
		}
*/
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
			
			loaded_route=true;

    }

    void joyCallback(const sensor_msgs::Joy::ConstPtr& joy)
	{
		geometry_msgs::Twist vel_steer;
		if (joy->buttons[4]==1&&joy->buttons[5]==1 ){//R1L1
			printf("Cargando Ruta \n");
			loadRoute();
			ros::Duration(0.2).sleep(); // sleep for half a second
		}else if(joy->buttons[13]&&loaded_route==true && start_route == false){//start
			
			ROS_INFO("Start");
			indx=0;
			nspx=sp_rx[indx];
			nspy=sp_ry[indx];
			mode=0;
			//ros::Duration(0.3).sleep(); // sleep for half a second
			mode_idle=false;
			mode_karugamo=false;
			mode_manual=false;
			mode_follow=false;
			tracking_people=false;
			mode_auto=true;
			start_route=true;
			ROS_INFO("Mode Auto");
			alerts_command.data=3;//8 follow 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			alerts_publisher.publish(alerts_command);
			vel_steer.linear.x= 0;
                        vel_steer.angular.z= 0;
			ctrl_front_follow= 0;
			ctrl_ang= 0;
			ctrl_front_manual= 0;
			ctrl_side_manual= 0;
			speed_publisher.publish(vel_steer);
			ros::Duration(0.5).sleep(); // sleep for half a second
		}else if(joy->buttons[13]&&loaded_route==true && start_route == true){//stopt with click  pad ps4 controller
			start_route=true;
			ROS_INFO("Stop");
			indx=0;
			nspx=sp_rx[indx];
			nspy=sp_ry[indx];
			mode=1;
			//ros::Duration(0.3).sleep(); // sleep for half a second
			mode_idle=false;
			mode_karugamo=false;
			mode_manual=false;
			mode_follow=false;
			tracking_people=false;
			mode_auto=false;
			start_route=false;
			
			ROS_INFO("Mode Auto");
			alerts_command.data=3;//8 follow 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			alerts_publisher.publish(alerts_command);
			vel_steer.linear.x= 0;
                        vel_steer.angular.z= 0;
			ctrl_front_follow= 0;
			ctrl_ang= 0;
			ctrl_front_manual= 0;
			ctrl_side_manual= 0;
			speed_publisher.publish(vel_steer);
			ros::Duration(0.5).sleep(); // sleep for half a second
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
		//}else if (joy->buttons[2]==1 && ruta_learn ==true && save_waypoint==false){
		//	save_waypoint=true;
		//	ros::Duration(0.4).sleep(); // sleep for half a second
		//	
//
		}else if(joy->buttons[2]==1 && free_way==true && collision == false){//danger!=true && free_way==true){//circulo


///////////////New algorithm
/*
int cicles=20;
float c=0.05;
float p0x=0;
float p0y=0;
float p1x=1.5;
float p1y=0.2;
float p2x=4;
float p2y=-0.7;
float aux1=0;
float aux2=0;
for(int i=0;i<cicles;i++){
//ROS_INFO("added %i,%f,%f",k,spx_follow[k],spy_follow[k]);
float Q0x=p0x-p0x*i*c+i*c*p1x;
float Q0y=p0y-p0y*i*c+i*c*p1y;

float Q1x=p1x-p1x*i*c+i*c*p2x;
float Q1y=p1y-p1y*i*c+i*c*p2y;

float Rx=Q0x-Q0x*i*c+i*c*Q1x;
float Ry=Q0y-Q0y*i*c+i*c*Q1y;

float angle= atan2(Ry-aux2, Rx-aux1) * 180 / 3.1416;
aux1=Rx;
aux2=Ry;
ROS_INFO("Rcalc %f,%f,%f",Rx,Ry,angle);
}
*/
////////////


			mode_idle=true;
			mode_karugamo=false;
			mode_manual=false;
			danger=false;
			mode_follow=false;
   			tracking_people=false;
			start_route = false;
			ROS_INFO("Mode IDLE");
			ctrl_front_follow= 0;
			ctrl_ang= 0;
			ctrl_front_manual= 0;
			ctrl_side_manual= 0;
			alerts_command.data=2;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			alerts_publisher.publish(alerts_command);
			vel_steer.linear.x= 0;
                        vel_steer.angular.z= 0;
			//fclose(fp);
			speed_publisher.publish(vel_steer);
			
			ros::Duration(0.5).sleep(); // sleep for half a second
			
		//}else if(joy->buttons[1]==1 && danger!=true && collision == false){//equis
		}else if(joy->buttons[1]==1 && collision == false){//equis
			mode_idle=false;
			mode_karugamo=false;
			mode_manual=true;
			mode_follow=false;
			tracking_people=false;
			start_route = false;
			mode_auto=false;
			ROS_INFO("Mode Manual");
			alerts_command.data=1;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			alerts_publisher.publish(alerts_command);
			vel_steer.linear.x= 0;
                        vel_steer.angular.z= 0;
			ctrl_front_follow= 0;
			ctrl_ang= 0;
			ctrl_front_manual= 0;
			ctrl_side_manual= 0;
			speed_publisher.publish(vel_steer);
			ros::Duration(0.5).sleep(); // sleep for half a second
		/*}else if(joy->buttons[8]==1){//select
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
			}*/
		}else if(joy->buttons[3] && danger!=true && collision == false ){//triangulo	
		      //if(mode_karugamo){
			//mode_idle=true;
			//mode_karugamo=false;
			//mode_manual=false;
			//ROS_INFO("Mode IDLDE");
			//vel_steer.linear.x=0;
			//vel_steer.angular.z=0;
			//speed_publisher.publish(vel_steer);
			//ros::Duration(0.5).sleep(); // sleep for half a second
		      //}else{
			/*mode_idle=false;
			mode_karugamo=true;
			mode_manual=false;
			mode_follow=false;
			tracking_people=false;
			ROS_INFO("Mode Karugamo");
			vel_steer.linear.x=0;
			vel_steer.angular.z=0;
			speed_publisher.publish(vel_steer);
			alerts_command.data=3;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			alerts_publisher.publish(alerts_command);
			ros::Duration(0.5).sleep(); // sleep for half a second
			*/
		      //}
			/*if(mod_seguir==false){
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
			}*/
			
		}else if(joy->buttons[0] && danger!=true && collision == false){//square
			mode_idle=false;
			mode_karugamo=false;
			mode_manual=false;
			mode_follow=true;
			tracking_people=false;
			start_route = false;
			mode_auto=false;
			ctrl_front_follow= 0;
			ctrl_ang= 0;
			ctrl_front_manual= 0;
			ctrl_side_manual= 0;
			vel_steer.linear.x=0;
			vel_steer.angular.z=0;
			cont_sp_follow=0;
			kf=1;
			speed_publisher.publish(vel_steer);
			alerts_command.data=8;// 8people follow 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			//alerts_publisher.publish(alerts_command);
     			alerts_publisher.publish(alerts_command);

			ROS_INFO("Mode People Follow");
			
			fp = fopen ("/home/xavier/catkin_ws/src/control_xy/people.txt" , "w+");
			//alerts_command.data=7;//7 peop follow 5 danger 4 warning 3 karugamo 2 idle 1 manual
			
			ros::Duration(0.5).sleep(); // sleep for half a second
			
		}

		if(mode_manual){
			if(free_way){
			   ctrl_front_manual=(1-smooth_accel)*(joy->axes[1]*max_speed_manual)+(smooth_accel*ctrl_front_manual);
			   if(ctrl_front_manual<20 && ctrl_front_manual>-20){
				ctrl_front_manual=0;
			   }
			   vel_steer.linear.x= ctrl_front_manual;
			   //vel_steer.linear.x=-joy->axes[1]*-max_speed_manual;

			   ctrl_side_manual=(1-smooth_accel)*(-joy->axes[0]*max_speed_side_manual)+(smooth_accel*ctrl_side_manual);
			   
			   if(ctrl_side_manual<7 && ctrl_side_manual>-7){
				ctrl_side_manual=0;
			   }
			   vel_steer.angular.z=ctrl_side_manual;
			   
			   if(joy->axes[7]!=0){
			     vel_steer.linear.x=joy->axes[7]*max_speed_manual;
			   }
			   if(joy->axes[6]!=0){
			     vel_steer.angular.z=joy->axes[6]*-800;
			   }
			   speed_publisher.publish(vel_steer);


		}else{//else free way
		
			ctrl_front_manual=(1-smooth_accel)*(joy->axes[1]*max_speed_manual)+(smooth_accel*ctrl_front_manual);
			if(ctrl_front_manual<0){
				vel_steer.linear.x= ctrl_front_manual;
				ctrl_side_manual=(1-smooth_accel)*(-joy->axes[0]*max_speed_side_manual)+(smooth_accel*ctrl_side_manual);
			   
			   	if(ctrl_side_manual<7 && ctrl_side_manual>-7){
					ctrl_side_manual=0;
			   	}
			   	vel_steer.angular.z=ctrl_side_manual;
				speed_publisher.publish(vel_steer);
				
			}else{
			    
			    vel_steer.linear.x= 0;
			    vel_steer.angular.z= 0;
			    speed_publisher.publish(vel_steer);
			}		   
		}
                         
	    }
		
		
	}//end joy

	
private:

    	ros::Subscriber head_subscriber;
	ros::Subscriber ang_subscriber;
        ros::Subscriber ang_subscriber_cam;
	ros::Subscriber dist_subscriber;
        ros::Subscriber ang_subscriber2;
	ros::Subscriber dist_subscriber2;
    	ros::Subscriber pose_subscriber;	
    	ros::Publisher light_publisher;
	ros::Publisher alerts_publisher;
	ros::Publisher tracked_publisher;
    	std_msgs::String light_command;
        ros::Publisher steering_publisher;
        std_msgs::Int16 steering_command;
        ros::Publisher speed_publisher;
        std_msgs::Int16 speed_command;
	std_msgs::Int16 alerts_command;
	ros::Subscriber subTwist_;
        ros::Subscriber state_subscriber;
        ros::Subscriber obst_subscriber;
	ros::Subscriber odometry_sub;
	ros::Subscriber joy_subscriber;
	ros::Subscriber subScan_;
        geometry_msgs::Twist vel_steer;
	geometry_msgs::Vector3 tracked_pos;
        std_msgs::Float32 ang_people;
	bool save_waypoint,start_tray,col_avoid_mode,danger, mode_idle,mode_karugamo,mode_manual,mode_follow,free_way,collision,mode_auto;
	float angulo_seguimiento,sp_yaw,sp_yaw2,ctrl_yaw,error_yaw,yaw,distanciaPeople,distanciaPeople2,break_distance,break_danger,max_speed_karugamo,max_speed_follow,max_speed_manual,ctrl_ang,ctrl_lin;
	float px,py,norm,norm2,x_ini,y_ini,x_p,y_p,px2,py2,spx,spy,err_x,err_y,err_xx,err_yy,low_vel_gain,high_vel_gain,low_vel_gain_follow,high_vel_gain_follow,smooth_accel,ctrl_side_manual,max_speed_side_manual;
	char rx[80],ry[80],rx2[80],ry2[80],pa[80],yag[80];
	float sp_rx[1000],sp_ry[1000],sp_rx2[1000],sp_ry2[1000],param[1000],sp_yaww[1000];
	float spx_follow[25],spy_follow[25],angle_follow[25],prev_cx,prev_cy;
	float spx_saved[10000],spy_saved[10000];
	int count,count2,ca,direction,count_odo,cont_detect_peop,cont_sp_follow,kf;
	FILE * fp;
	bool obstaculo,changed,crucero,ruta_learn,loaded_route,start_route,arrived,obstacle_front,obstacle_front1,obstacle_front2,newobstacle,tracking_people;
	float px_aux,py_aux,n_aux,last_error,alfa,velx,err2,velyaw,intErr,velCtrl,nspx,nspy,errPos,ang_peop_cam,ang_peop_lidar,tracked_angle,tracked_distance,radius_follow,tracked_cx,tracked_cy;
	int num_sp,k_idx,carril,velocity,contadorvel,mode,indx,h,conta,missing_track;
	ros::Time time_obst,time_cruce,time_obst_last,time_cruce_last;
        float errpx,errpy,spVel,nkp,nkd,nki,errVelYaw,nvkp,nvkd,spPos,distAct,errPVel,spPVel;
        float ctrl_vel,frontal_gain_follow,frontal_gain_karugamo,frontal_gain_manual,ctrl_front_follow,ctrl_front_karugamo;
	float ctrl_front_manual,cx,cy,aux_dist,ang_robot;

	float spx_follow_old,spy_follow_old,spx_follow_new,spy_follow_new,dist_auxwp;
	int indice,index_wp,numwp,cicles;
	
};

int main(int argc, char **argv)
{
    ros::init(argc, argv, "heading_follow_node");
    ros::NodeHandle nh; 

    test_head test_head_obj(nh);
    //ros::Rate rate(0.5); //0.5 Hz, every 2 second
	ros::Rate rate(50); //100 Hz, every .01 second
    //printf("%f",-atan2(5,1)*180/3.1416);
	while(ros::ok())
	{
		
		ros::spinOnce();
		rate.sleep();
	}
    return 0;
}
