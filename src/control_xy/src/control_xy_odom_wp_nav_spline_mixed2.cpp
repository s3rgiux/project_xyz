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

#include <visualization_msgs/Marker.h>
#include <nav_msgs/Odometry.h>

float filter_yaw=0;



class test_head
{
public:
	test_head(ros::NodeHandle nh)
	{
	    
        	speed_publisher=nh.advertise<geometry_msgs::Twist>(nh.resolveName("/cmd_vel"), 1);
		tracked_publisher=nh.advertise<geometry_msgs::Vector3>(nh.resolveName("/tracked"), 2);
		alerts_publisher=nh.advertise<std_msgs::Int16>(nh.resolveName("/alerts"), 1);
		marker_pub   = nh.advertise<visualization_msgs::Marker>(nh.resolveName("/visualization_marker"),1);
		pos_peop_pub = nh.advertise<nav_msgs::Odometry>(nh.resolveName("/peop_way"),1);
		
                head_subscriber = nh.subscribe("/euler", 1, &test_head::headCallback,this);
		odometry_sub = nh.subscribe("odom",1,&test_head::ReceiveOdometry,this);
                //odometry_sub = nh.subscribe("poseupdate",1,&test_head::ReceiveOdometry,this);
		joy_subscriber = nh.subscribe("/j0/joy", 1, &test_head::joyCallback,this);
		pose_subscriber = nh.subscribe("setPoints", 1, &test_head::setPointsCallback,this);
		//ang_subscriber = nh.subscribe("peopAng", 1, &test_head::angPeopCallback,this);
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
		is_near=false;
		stop_follow=false;
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
		}else if(data.trigger=="break_release_button_on" && collision ==true){
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
		} else if(data.trigger=="karugamo_button_on" && mode_follow==false){
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
			speed_publisher.publish(vel_steer);
			alerts_command.data=8;// 8people follow 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			//alerts_publisher.publish(alerts_command);
     			alerts_publisher.publish(alerts_command);

			ROS_INFO("Mode People Follow");
			
			
			//alerts_command.data=7;//7 peop follow 5 danger 4 warning 3 karugamo 2 idle 1 manual
			
			ros::Duration(0.5).sleep(); // sleep for half a second
		} else if(data.trigger=="karugamo_button_on" && mode_follow==true){
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
			ros::Duration(0.5).sleep(); // sleep for half a second
		}
		
	}void setPointsCallback(const geometry_msgs::Twist& twist)
	{
	nspx=twist.linear.x;
	nspy=twist.linear.y;
        sp_yaw=-atan2(nspx,nspy)*180/3.1416;
	ROS_INFO("%f,%f,%f",nspx,nspy,sp_yaw);
	}

	void obstCallback(const std_msgs::Float32& msg)
	{
           if(msg.data==1){
              newobstacle = true;
           }else{
              newobstacle = false;
           }
	}

    void headCallback(const std_msgs::Float64& head)
	{	
	ang_robot=head.data;

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


	void distPeopCallback(const std_msgs::Float32& msg){
		
			distanciaPeople=msg.data;
	   
    	} 

	void distPeopCallback2(const std_msgs::Float32& msg){
			//distanciaPeople2=msg.data;
    	} 


  void angCamCallback2(const std_msgs::Float32& msg){
                ang_peop_cam=msg.data;
		if(ang_peop_cam!=-500 && mode_follow && tracking_people==false ){
		       cont_detect_peop+=1;
			missing_track=0;
			if(ang_peop_lidar<ang_peop_cam+7 && ang_peop_lidar> ang_peop_cam-7  && distanciaPeople2<aux_dist ){
				//cont_detect_peop+=1;
				aux_dist = distanciaPeople2;
				ROS_INFO("Received angle %f",ang_peop_lidar);
				tracked_cx=cx;
				tracked_cy=cy;
				tracked_pos.x=cx;
				tracked_pos.y=cy;
				tracked_pos.z= ang_peop_lidar;
				tracked_angle=ang_peop_lidar;
			}
			if(cont_detect_peop>7){
				tracking_people=true;
				cont_detect_peop=0;
					ROS_INFO("Tracked angle %f",ang_peop_lidar);
                                	tracked_distance=distanciaPeople2;
					
					tracking_people=true;
					aux_dist=5000;
					missing_track=0;
				tracked_pos.x=tracked_cx;
				tracked_pos.y=tracked_cy;
				tracked_pos.z= ang_peop_lidar;
				
					stop_follow=false;
					tracked_publisher.publish(tracked_pos);
                                	ctrl_front_follow= 0;
			        	ctrl_ang=0;
			        	vel_steer.linear.x= 0;
                                	vel_steer.angular.z= 0;
					cont_sp_follow=0;
					kf=0;
					index_wp=-1;//init follow
					dist_auxwp=0;
                                        
					//fp = fopen ("/home/xavier/catkin_ws/src/control_xy/people.txt" , "w+");

				}
		}
       }


/*
Pitakuru coordinate system and angles w.r.t Robot
		x 0deg
		|
		|
		|
	
  90deg	-y--------------- y  -90deg
		|
		|
		|
		|
		|
	 179deg -x -179 deg       
*/



void angPeopCallback4(const geometry_msgs::Vector3& msg){

cicles=20;

cx = msg.x;//pos people or object
cy = msg.y;//pos people or object
ang_peop_lidar = 90- atan2(cx, cy) * 180 / 3.1416;
//ang_peop_lidar = -90+ atan2(cx, cy) * 180 / 3.1416 ;
distanciaPeople2 = sqrt(cx*cx+cy*cy)*100;
ROS_INFO("%f",ang_peop_lidar);
if(mode_follow && danger!=true){

		if(cx!=0.01 && cy !=0.01 && tracking_people && cx<=(tracked_cx+radius_follow) && cx>=(tracked_cx-radius_follow) && cy<=(tracked_cy+radius_follow) && cy >=(tracked_cy-radius_follow)){//2
			
		
			//ang_peop_lidar = 90+ atan2(cx, cy) * 180 / 3.1416 ;
			//ang_peop_lidar = -90+ atan2(cx, cy) * 180 / 3.1416 ;
			ang_peop_lidar = 90- atan2(cx, cy) * 180 / 3.1416;
			distanciaPeople2 = sqrt(cx*cx+cy*cy)*100;
                        tracked_angle= ang_peop_lidar;
			tracked_distance = distanciaPeople2;

			if(distanciaPeople2<290){
				near();
				is_near=true;
			}else{
				is_near=false;
                                alerts_command.data=4;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     				alerts_publisher.publish(alerts_command);
				if(cont_sp_follow>=2){
					index_wp=cont_sp_follow-3;
				}
			}//endif not near
		
			missing_track=0;
			tracked_cx=cx;
			tracked_cy=cy;
			tracked_pos.x=cx;
			tracked_pos.y=cy;
			tracked_pos.z=tracked_angle;
			tracked_publisher.publish(tracked_pos);
                     	geometry_msgs::Twist vel_steer;		
			/////////////////////////new implement
			float dobs,angobs,npcx,npcy;
			dobs=sqrt(tracked_cx*tracked_cx+tracked_cy*tracked_cy);
			//angobs=atan2(-tracked_cy,-tracked_cx)*180/3.1416;
			//angobs=atan2(tracked_cx,tracked_cy)*180/3.1416;
			angobs  = 90- atan2(cx, cy) * 180 / 3.1416 ;// ;  -90+ atan2(cx, cy) * 180 / 3.1416 
			//angobs = -90+ atan2(cx, cy) * 180 / 3.1416 ;
			//px,py, ang_robot position robot

			npcx=px+dobs*(cos((angobs+ang_robot)*3.1416/180));//#rcx+ocx*(cos((angobs+angr)*3.1416/180))
			npcy=py+dobs*(sin((angobs+ang_robot)*3.1416/180));//#rcy+ocy*(sin((angobs+angr)*3.1416/180))
			//ROS_INFO("T%f,%f,%f,%f",tracked_cx,tracked_cy,npcx,npcy);
			if(sqrt((npcx-prev_cx)*(npcx-prev_cx)+(npcy-prev_cy)*(npcy-prev_cy))>0.75){ // se agrega el nuevo objeto
				people_point.header.frame_id="/my_frame";
				people_point.header.stamp = ros::Time::now();
				people_point.action= visualization_msgs::Marker::ADD;
				people_point.pose.orientation.w= 1.0;
				people_point.id=0;
				people_point.type=visualization_msgs::Marker::POINTS;
				people_point.scale.x=0.2;
				people_point.scale.y=0.2;
				people_point.color.g=1.0f;
				people_point.color.a=1.0;
				prev_cx=npcx;
				prev_cy=npcy;
			      spx_saved[cont_sp_follow]=npcx;
			      spy_saved[cont_sp_follow]=npcy;
			      cont_sp_follow++;
				geometry_msgs::Point p;
				p.x=npcx;
				p.y=npcy;
				p.z=1.0;
				people_point.points.push_back(p);
				marker_pub.publish(people_point);

				nav_msgs::Odometry odom;
				odom.header.stamp = ros::Time::now();
				odom.header.frame_id="people";
				odom.pose.pose.position.x=npcx;
				odom.pose.pose.position.y=npcy;
				odom.pose.pose.position.z=0.0;
				odom.pose.pose.orientation.w=1.0;
				pos_peop_pub.publish(odom);
				
			      ROS_INFO("added %f,%f,%f,%f,%f,%f",npcx,npcy,px,py,angobs,ang_robot);
			      fprintf(fp,"%f,%f,%f,%f,%f,%f\n",npcx,npcy,px,py,angobs,ang_robot);
			}
			tracking =true;
			ROS_INFO("tracked");
		    	
                }//end it s in range
		else{//losted
		    //if(is_near==false){
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
				alerts_command.data=7;// 5 danger 4 warning 3 karugamo 2 idle 1 lal
     				alerts_publisher.publish(alerts_command);
				tracked_publisher.publish(tracked_pos);
				alerts_command.data=4;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     				alerts_publisher.publish(alerts_command);
				tracking =false;
			}
		   // }
		}//losted

//changed from here
	
if(is_near==false){

  		///////////////New algorithm
		if(cont_sp_follow>=2){

		 	if(dist_auxwp<0.4){
				index_wp++;
				if(index_wp>=(cont_sp_follow-1)){
					cont_sp_follow-1;
					stop_follow=true;//arrived to last wp
				}
				float c=0.05;//must be 1/cicles
				float p0x=px;//pos robot x
				float p0y=py;//pos robot y
				float p1x=spx_saved[index_wp];//spx_saved[index_wp];//spx_follow_old;//first wp
				float p1y=spy_saved[index_wp];//spy_saved[index_wp];//spy_follow_old;//first wp
				float p2x=spx_saved[index_wp+1];//spx_saved[index_wp+1];//spx_follow_new;//second
				float p2y=spy_saved[index_wp+1];//spy_saved[index_wp+1];//spy_follow_new;//second wp
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
					angle= atan2((Ry-aux2),(Rx-aux1)) * 180 / 3.1416;//angle wrt robot
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
/////////////////changed here

             
					
				//ROS_INFO("***********");
				////////////
				errpx=spx_follow[indice]-px;
				errpy=spy_follow[indice]-py;
				sp_yaw=angle_follow[indice+1];
			
				if(sqrt((errpx*errpx)+(errpy*errpy))<0.3){
					indice++;
					if (indice>19){
						indice=19;
					}
				}
				error_yaw=(sp_yaw-ang_robot);//-(sp_yaw-ang_robot);
				if (error_yaw < -180.0 ){
					error_yaw=error_yaw+360;
				}else if (error_yaw > 180.0 ){
					error_yaw=error_yaw-360;
				}
				spVel=0.1*(error_yaw);//0.05*(error_yaw);
				nkp=140;//=0.0085;
				ctrl_yaw=(nkp*spVel);//
					if(ctrl_yaw>400){
						ctrl_yaw=400;
					}else if(ctrl_yaw<-400){
						ctrl_yaw=-400;
					}
			
			if(distanciaPeople2>100){
				float  norm_dist,dist_conv;
				dist_conv=distanciaPeople2;
				if(dist_conv>250){
				   dist_conv=250;
				   norm_dist=(dist_conv-100)/150;
				}else{
				   norm_dist=(dist_conv-100)/150;
				}
	
			 	//ctrl_front_follow=(1-smooth_accel)*(frontal_gain_follow*(distanciaPeople2-100))+(smooth_accel*ctrl_front_follow);
				ctrl_front_follow=(1-smooth_accel)*(frontal_gain_follow*norm_dist/*max_speed_follow*/)+(smooth_accel*ctrl_front_follow);
				//ROS_INFO("%f,%f",ctrl_front_follow,distanciaPeople2);
			   	if(ctrl_front_follow<0 ){
					ctrl_front_follow=0;
					vel_steer.linear.x=0;
			   	}
				if (ctrl_front_follow>max_speed_follow){
                          		ctrl_front_follow= max_speed_follow;
				}
                       }else{
			ctrl_front_follow=500;
			}
		}else{
			 ctrl_front_follow=0;
			 ctrl_yaw=0;
		}
			if(stop_follow==true){//stop if arrived  last wp
				ctrl_front_follow=0;
				ctrl_yaw=0;
			}
			vel_steer.linear.x= ctrl_front_follow;
			vel_steer.angular.z= ctrl_yaw;
			speed_publisher.publish(vel_steer);

	   }//end_isnear=false
		
}//end mode follow
}//end function







///////////////////

void near(){
		//cx = msg.x;
		//cy = msg.y;
		//ang_peop_lidar = 90- atan2(cx, cy) * 180 / 3.1416 ;//-90+ atan2(cx, cy) * 180 / 3.1416 ;
		//distanciaPeople2 = sqrt(cx*cx+cy*cy)*100;
		// ROS_INFO("R%f,%f,%f,%f",cx,cy,ang_peop_lidar,distanciaPeople2);
		

	   if(mode_follow && danger!=true){ //&& tracking_people){//1
	//	   ROS_INFO("R%f,%f",cx,cy);
	//	   ROS_INFO("P%f,%f",tracked_cx,tracked_cy);
		    if( cx!=0.01 && cy !=0.01 && ang_peop_lidar<85 && ang_peop_lidar>-85 && tracking_people && cx<=(tracked_cx+radius_follow) && cx>=(tracked_cx-radius_follow) && cy<=(tracked_cy+radius_follow) && cy >=(tracked_cy-radius_follow)){//2

			//correccion needed
			//ang_peop_lidar = -90+ atan2(cx, cy) * 180 / 3.1416 ;// ;  90- atan2(cx, cy) * 180 / 3.1416 
			ang_peop_lidar = 90- atan2(cx, cy) * 180 / 3.1416 ;// ;  -90+ atan2(cx, cy) * 180 / 3.1416 
			//ang_peop_lidar = 90- atan2(cx, cy) * 180 / 3.1416 ;//-90+ atan2(cx, cy) * 180 / 3.1416 ;

			distanciaPeople2 = sqrt(cx*cx+cy*cy)*100;
                        ROS_INFO("T%f,%f",tracked_cx,tracked_cy);
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
			//if (ang_peop_lidar>-4 && ang_peop_lidar<4){
			//	ctrl_ang=0;
                        //	vel_steer.angular.z=0;
                        //}else{	
				
				ctrl_ang= low_vel_gain_follow*ang_peop_lidar-ctrl_ang/2;
				
				if (ctrl_ang>500){
                        		ctrl_ang= 500;
				}else if (ctrl_ang<-500){
                        		ctrl_ang= -500;
				}
				vel_steer.angular.z=ctrl_ang;//low_vel_gain*msg.data;//*(distanciaPeople/40);
					
                        //}
			 
			 if(distanciaPeople2>100){
				float  norm_dist,dist_conv;
				dist_conv=distanciaPeople2;
				if(dist_conv>250){
				   dist_conv=250;
				   norm_dist=(dist_conv-100)/150;
				}else{
				   norm_dist=(dist_conv-100)/150;
				}
	
			 	//ctrl_front_follow=(1-smooth_accel)*(frontal_gain_follow*(distanciaPeople2-100))+(smooth_accel*ctrl_front_follow);
				ctrl_front_follow=(1-smooth_accel)*(frontal_gain_follow*norm_dist/*max_speed_follow*/)+(smooth_accel*ctrl_front_follow);
				//ROS_INFO("%f,%f",ctrl_front_follow,distanciaPeople2);
			   	if(ctrl_front_follow<0 ){
					ctrl_front_follow=0;
					vel_steer.linear.x=0;
			   	}
				if (ctrl_front_follow>max_speed_follow){
                          		ctrl_front_follow= max_speed_follow;
				}
				vel_steer.linear.x= ctrl_front_follow;
			   }else{
				vel_steer.linear.x=0;
				ctrl_front_follow=0;
			   }
			
		  
			//alerts_command.data=7;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     			//alerts_publisher.publish(alerts_command);
			speed_publisher.publish(vel_steer);
		  }
/*
else{
                        missing_track+=1;
			if (tracking_people==true){
                        	if(missing_track>=25){//thiscounter also can help to see if theres a lot of objects and its not able to follow	
					ROS_INFO("LOST");
					is_near=false;
					missing_track=0;
					cont_detect_peop=0;
			        	tracking_people=false;
					tracked_cx=0;
					tracked_cy=0; 
					aux_dist=5000;
					
					alerts_command.data=7;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     					alerts_publisher.publish(alerts_command);
					tracked_pos.x=-50;
					tracked_pos.y=-50;
					tracked_publisher.publish(tracked_pos);
					alerts_command.data=4;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     					alerts_publisher.publish(alerts_command);
				}

					vel_steer.linear.x= ctrl_front_follow;
                        		vel_steer.angular.z= ctrl_ang;
				        //tracked_pos.x=tracked_cx;
					//tracked_pos.y=tracked_cy;
					//tracked_pos.z=tracked_angle;
					//tracked_publisher.publish(tracked_pos);
					speed_publisher.publish(vel_steer);
			}else{
				//ctrl_front_follow= 0;
					ctrl_front_follow=(1-smooth_accel)*(-10)+(smooth_accel*ctrl_front_follow);//smooth slow down
					if(ctrl_front_follow<1){
						ctrl_front_follow= 0;				      
					}
					ctrl_ang= (1-smooth_accel)*(0)+(smooth_accel*ctrl_ang);//smooth slow down
		  			vel_steer.linear.x= ctrl_front_follow;
                        		vel_steer.angular.z= ctrl_ang;
					speed_publisher.publish(vel_steer);
					//alerts_command.data=7;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
				        alerts_command.data=4;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
     					alerts_publisher.publish(alerts_command);
					//tracked_pos.x=-50;
					//tracked_pos.y=-50;
					//tracked_publisher.publish(tracked_pos);
			 }
			
                        
		  }
*/
	       }//mode3
	   
    }  



///////////////////














    void scanCallback(const sensor_msgs::LaserScan::ConstPtr& scan)
	{
	    int count = scan->scan_time / scan->time_increment;
	    //float  break_distance=1.5;
            //float  break_danger=0.5;
		for(int j=269;j<=358;j++){
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

		for(int i=0;i<=90;i++){
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
			stop_follow=false;
			aux_dist=50000;
			is_near=false;
			fp = fopen ("/home/xavier/catkin_ws/src/control_xy/people.txt" , "w+");
			//alerts_command.data=7;//7 peop follow 5 danger 4 warning 3 karugamo 2 idle 1 manual
			index_wp=-1;//init follow
			dist_auxwp=0;
			ros::Duration(0.5).sleep(); // sleep for half a second
			
		}

		if(mode_manual){
			  if(free_way){
			  //if(true){
			   	ctrl_front_manual=(1-smooth_accel)*(joy->axes[1]*max_speed_manual)+(smooth_accel*ctrl_front_manual);
			   	//if(ctrl_front_manual<20 && ctrl_front_manual>-20){
				//	ctrl_front_manual=0;
			   	//}
			   	vel_steer.linear.x= ctrl_front_manual;
			   	//vel_steer.linear.x=-joy->axes[1]*-max_speed_manual;
			   	ctrl_side_manual=(1-smooth_accel)*(joy->axes[0]*max_speed_side_manual)+(smooth_accel*ctrl_side_manual);
			   
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
				ctrl_side_manual=(1-smooth_accel)*(joy->axes[0]*max_speed_side_manual)+(smooth_accel*ctrl_side_manual);
			   
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
	ros::Publisher marker_pub;
	ros::Publisher pos_peop_pub;
        geometry_msgs::Twist vel_steer;
	geometry_msgs::Vector3 tracked_pos;
        std_msgs::Float32 ang_people;
	visualization_msgs::Marker people_point;
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
       bool tracking,is_near,stop_follow;
	
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