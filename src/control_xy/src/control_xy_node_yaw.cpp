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
		alerts_publisher=nh.advertise<std_msgs::Int16>(nh.resolveName("/alerts"), 1);
                head_subscriber = nh.subscribe("/euler", 1, &test_head::headCallback,this);
		odometry_sub = nh.subscribe("odom",1,&test_head::ReceiveOdometry,this);
                //odometry_sub = nh.subscribe("poseupdate",1,&test_head::ReceiveOdometry,this);
		joy_subscriber = nh.subscribe("/j0/joy", 1, &test_head::joyCallback,this);
		pose_subscriber = nh.subscribe("setPoints", 1, &test_head::setPointsCallback,this);
		ang_subscriber = nh.subscribe("peopAng", 1, &test_head::angPeopCallback,this);
		dist_subscriber = nh.subscribe("peopDist", 1, &test_head::distPeopCallback,this);
                ang_subscriber2 = nh.subscribe("peopAng2", 1, &test_head::angPeopCallback2,this);
                ang_subscriber_cam = nh.subscribe("ang_peop_detect_img", 1, &test_head::angCamCallback,this);
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

		tracked_angle=0;
                ang_peop_lidar=0;
		distanciaPeople2=0;
		tracked_distance=0;

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
		
		danger=false;
		free_way=true;
		collision = false;
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
			//ROS_INFO("%f,%f,%f,%f,%f",errpx,errpy,error_yaw,ctrl_vel,errPVel); 
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

       void angCamCallback(const std_msgs::Float32& msg){
                ang_peop_cam=msg.data;
	
		if(ang_peop_cam!=-500 && mode_follow && tracking_people==false){
			if(ang_peop_lidar+5>ang_peop_cam && ang_peop_lidar-5< ang_peop_cam ){
				ROS_INFO("Tracked angle %f",ang_peop_lidar);
                                tracked_angle=ang_peop_lidar;
                                tracked_distance=distanciaPeople2;
				tracking_people=true;
				missing_track=0;
				tracked_cx=cx;
				tracked_cy=cy;
			}
		}
       }



//void angPeopCallback2(const std_msgs::Float32& msg){
void angPeopCallback2(const geometry_msgs::Vector3& msg){
                //ang_peop_lidar=msg.data;
		//python ang = 90+np.arctan2(x.center.x, x.center.y) * 180 / np.pi
                //python dist =np.sqrt(x.center.x*x.center.x+x.center.y*x.center.y)
		cx = msg.x;
		cy = msg.y;
		ang_peop_lidar = 90+ atan2(cx, cy) * 180 / 3.1416 ;
		distanciaPeople2 = sqrt(cx*cx+cy*cy)*100;
		//ang_peop_lidar=msg.x;
		//distanciaPeople2=msg.y;
		if(mode_follow && danger!=true){ //&& tracking_people){//1
		   //ROS_INFO("R%f,%f",ang_peop_lidar,distanciaPeople2);
		   //ROS_INFO("P%f,%f",tracked_angle,tracked_distance);
		   ROS_INFO("R%f,%f%400",cx,cy);
		   ROS_INFO("P%f,%f",tracked_cx,tracked_cy);
		   //if(ang_peop_lidar!=-500 && ang_peop_lidar<=(tracked_angle+12) && ang_peop_lidar>=(tracked_angle-12) && distanciaPeople2<=(tracked_distance+38) && distanciaPeople2 >=(tracked_distance-38)){//2
		   if(tracking_people && cx!=0.01 && cy !=0.01 && cx<=(tracked_cx+radius_follow) && cx>=(tracked_cx-radius_follow) && cy<=(tracked_cy+radius_follow) && cy >=(tracked_cy-radius_follow)){//2
			ang_peop_lidar = 90+ atan2(cx, cy) * 180 / 3.1416 ;
			distanciaPeople2 = sqrt(cx*cx+cy*cy)*100;
                        ROS_INFO("T%f,%f",tracked_cx,tracked_cy);
                        tracked_angle= ang_peop_lidar;
			tracked_distance = distanciaPeople2;
			missing_track=0;	

			tracked_cx=cx;
			tracked_cy=cy;
                     	geometry_msgs::Twist vel_steer;		
			if (ang_peop_lidar>-8 && ang_peop_lidar<8){
                        	vel_steer.angular.z=0;
                        }else{	
				if(distanciaPeople2<120){
					ctrl_ang= low_vel_gain_follow*ang_peop_lidar-ctrl_ang/2;
					vel_steer.angular.z=ctrl_ang;//low_vel_gain*msg.data;//*(distanciaPeople/40);
				   	if (vel_steer.angular.z>400){
                        			vel_steer.angular.z= 400;
				  	}else if (vel_steer.angular.z<-400){
                        			vel_steer.angular.z= -400;
					}
				}else{
				   	//vel_steer.angular.z=15*msg.data - vel_steer.angular.z/2;//*(distanciaPeople/40);
					ctrl_ang= high_vel_gain_follow*ang_peop_lidar-ctrl_ang/2;
					vel_steer.angular.z=ctrl_ang;//vel_steer.angular.z=high_vel_gain*msg.data;
				   	if (vel_steer.angular.z>500){
                        			vel_steer.angular.z= 500;
				  	}else if (vel_steer.angular.z<-500){
                        			vel_steer.angular.z= -500;
					}
				}			
                        }
			 
			 if(distanciaPeople2>120){			
			 	ctrl_front_follow=(1-smooth_accel)*(frontal_gain_follow*(distanciaPeople2-120))+(smooth_accel*ctrl_front_follow);
				//ROS_INFO("%f,%f",ctrl_front_follow,distanciaPeople2);
			   	if(ctrl_front_follow<5 && ctrl_front_follow>-5){
					ctrl_front_follow=0;
			   	}
				if (ctrl_front_follow>(max_speed_follow)){
                          		ctrl_front_follow= max_speed_follow;
				}
				vel_steer.linear.x= ctrl_front_follow;
			   }else{
				vel_steer.linear.x=0;
				ctrl_front_follow=0;
			   }
			
		        if(obstacle_front && col_avoid_mode){
                           vel_steer.linear.x=0;
			   speed_publisher.publish(vel_steer);
                           ros::Duration(1).sleep(); // sleep for half a second
                        }else if(danger && col_avoid_mode){
                           vel_steer.linear.x=0;
                           vel_steer.angular.z= 0;
			   speed_publisher.publish(vel_steer);
                           ros::Duration(1).sleep(); // sleep for half a second			
			}
			alerts_command.data=7;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			alerts_publisher.publish(alerts_command);
			speed_publisher.publish(vel_steer);
		  }else if( danger){
                        //tracking_people=false;
			ctrl_front_follow= 0;
			vel_steer.linear.x= 0;
                        vel_steer.angular.z= 0;
			speed_publisher.publish(vel_steer);
			alerts_command.data=4;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			alerts_publisher.publish(alerts_command);
		  }else{
                        missing_track+=1;
                        if(missing_track>=7){//thiscounter also can help to see if theres a lot of objects and its not able to follow
				ROS_INFO("LOST");
				missing_track=0;
			        tracking_people=false;
				ctrl_front_follow= 0;
		  		vel_steer.linear.x= 0;
                        	vel_steer.angular.z= 0;
				tracked_cx=0;
				tracked_cy=0;
				speed_publisher.publish(vel_steer);
				alerts_command.data=7;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     				alerts_publisher.publish(alerts_command);
			}
			alerts_command.data=4;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			alerts_publisher.publish(alerts_command);
                        
		  }

	       }//mode3
	   
    }  





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
				vel_steer.linear.x= 0;
                        	vel_steer.angular.z= 0;
				ctrl_front_follow=0;
				ctrl_front_karugamo=0;
				ctrl_front_follow=0;
				speed_publisher.publish(vel_steer);
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
				ctrl_front_follow=0;
				ctrl_front_karugamo=0;
				vel_steer.linear.x= 0;
                        	vel_steer.angular.z= 0;
				ctrl_front_follow=0;
				speed_publisher.publish(vel_steer);
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
				}
			        //danger=false;
  			}
		}
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
		//}else if (joy->buttons[2]==1 && ruta_learn ==true && save_waypoint==false){
		//	save_waypoint=true;
		//	ros::Duration(0.4).sleep(); // sleep for half a second
		//	
//
		}else if(joy->buttons[2]==1 && free_way==true && collision == false){//danger!=true && free_way==true){//circulo
			mode_idle=true;
			mode_karugamo=false;
			mode_manual=false;
			danger=false;
			mode_follow=false;
   			tracking_people=false;
			ROS_INFO("Mode IDLE");
			alerts_command.data=2;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			alerts_publisher.publish(alerts_command);
			vel_steer.linear.x= 0;
                        vel_steer.angular.z= 0;
			speed_publisher.publish(vel_steer);
			ros::Duration(0.5).sleep(); // sleep for half a second
			
		//}else if(joy->buttons[1]==1 && danger!=true && collision == false){//equis
		}else if(joy->buttons[1]==1 && collision == false){//equis
			mode_idle=false;
			mode_karugamo=false;
			mode_manual=true;
			mode_follow=false;
			tracking_people=false;
			ROS_INFO("Mode Manual");
			alerts_command.data=1;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			alerts_publisher.publish(alerts_command);
			vel_steer.linear.x= 0;
                        vel_steer.angular.z= 0;
			ctrl_front_manual=0;
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
			vel_steer.linear.x=0;
			vel_steer.angular.z=0;
			speed_publisher.publish(vel_steer);
			alerts_command.data=8;// 8people follow 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			//alerts_publisher.publish(alerts_command);
     			alerts_publisher.publish(alerts_command);

			ROS_INFO("Mode People Follow");
			
			
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
        std_msgs::Float32 ang_people;
	bool save_waypoint,start_tray,col_avoid_mode,danger, mode_idle,mode_karugamo,mode_manual,mode_follow,free_way,collision;
	float angulo_seguimiento,sp_yaw,sp_yaw2,ctrl_yaw,error_yaw,yaw,distanciaPeople,distanciaPeople2,break_distance,break_danger,max_speed_karugamo,max_speed_follow,max_speed_manual,ctrl_ang,ctrl_lin;
	float px,py,norm,norm2,x_ini,y_ini,x_p,y_p,px2,py2,spx,spy,err_x,err_y,err_xx,err_yy,low_vel_gain,high_vel_gain,low_vel_gain_follow,high_vel_gain_follow,smooth_accel,ctrl_side_manual,max_speed_side_manual;
	char rx[80],ry[80],rx2[80],ry2[80],pa[80],yag[80];
	float sp_rx[1000],sp_ry[1000],sp_rx2[1000],sp_ry2[1000],param[1000],sp_yaww[1000];
	int count,count2,ca,direction,count_odo;
	FILE * fp;
	bool obstaculo,changed,crucero,ruta_learn,loaded_route,start_route,arrived,obstacle_front,obstacle_front1,obstacle_front2,newobstacle,tracking_people;
	float px_aux,py_aux,n_aux,last_error,alfa,velx,err2,velyaw,intErr,velCtrl,nspx,nspy,errPos,ang_peop_cam,ang_peop_lidar,tracked_angle,tracked_distance,radius_follow,tracked_cx,tracked_cy;
	int num_sp,k_idx,carril,velocity,contadorvel,mode,indx,h,conta,missing_track;
	ros::Time time_obst,time_cruce,time_obst_last,time_cruce_last;
        float errpx,errpy,spVel,nkp,nkd,nki,errVelYaw,nvkp,nvkd,spPos,distAct,errPVel,spPVel,ctrl_vel,frontal_gain_follow,frontal_gain_karugamo,frontal_gain_manual,ctrl_front_follow,ctrl_front_karugamo,ctrl_front_manual,cx,cy;

};

int main(int argc, char **argv)
{
    ros::init(argc, argv, "heading_follow_node");
    ros::NodeHandle nh; 

    test_head test_head_obj(nh);
    //ros::Rate rate(0.5); //0.5 Hz, every 2 second
	ros::Rate rate(20); //100 Hz, every .01 second
    //printf("%f",-atan2(5,1)*180/3.1416);
	while(ros::ok())
	{
		
		ros::spinOnce();
		rate.sleep();
	}
    return 0;
}
