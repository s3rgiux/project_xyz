#include "ros/ros.h"
#include <std_msgs/String.h>
#include <std_msgs/Int16.h>
#include <std_msgs/Float32.h>
#include <std_msgs/Float64.h>
#include <geometry_msgs/Twist.h>
#include <geometry_msgs/Vector3.h>
#include <geometry_msgs/PoseStamped.h>
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
#include <nav_msgs/Path.h>


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
        path_pub = nh.advertise<nav_msgs::Path>(nh.resolveName("/pathpeop"),1);
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
        nh.getParam("/control_xy/speed_wp_lost",speed_wp_lost);
        nh.getParam("/control_xy/near_far_distance",near_far_distance);
        nh.getParam("/control_xy/max_speed_side_manual", max_speed_side_manual);
        nh.getParam("/control_xy/smooth_accel_karugamo_near", smooth_accel_karugamo_near);
        nh.getParam("/control_xy/smooth_accel_karugamo_far", smooth_accel_karugamo_far);
        nh.getParam("/control_xy/smooth_accel_manual", smooth_accel_manual);
        nh.getParam("/control_xy/radius_follow", radius_follow);
        nh.getParam("/control_xy/max_defelct_angle", max_defelct_angle);
        nh.getParam("/control_xy/dist_robot_people", dist_robot_people);
	    nh.getParam("/control_xy/angle_gain_wp", angle_gain_wp);
        nh.getParam("/control_xy/max_dist_toacc", max_dist_toacc);
        nh.getParam("/control_xy/smooth_accel_stop",smooth_accel_stop);
        nh.getParam("/control_xy/smooth_accel_side_manual",smooth_accel_side_manual);
    
        
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
        is_near=true;
        stop_follow=false;
        detect_cont=0;
        state_stop=0; 
        counter_search=340;
		stop_functions=false;
		save_counter=0;
    }
    ~test_head(){}
    

void stateCallback(const control_xy::TriggerAction& data){
        //ROS_INFO("Controlxy ");
        //ROS_INFO("%s ",data.trigger.c_str());
        if(data.trigger=="collision"){
            collisioned();
            ros::Duration(1.0).sleep(); // sleep for half a second
        //  ROS_INFO("Yuhu");
        //  ROS_INFO("%s ",data.trigger.c_str());
        }else if(data.trigger=="break_release_button_on" && collision ==true){
            remove_collision();

            ros::Duration(1.0).sleep(); // sleep for half a second
        //  ROS_INFO("Yuhu");
        //  ROS_INFO("%s ",data.trigger.c_str());
        } else if(data.trigger=="karugamo_button_on" && mode_follow==false){
            mode_people_follow();
            ros::Duration(1.0).sleep(); // sleep for half a second
        } else if(data.trigger=="karugamo_button_on" && mode_follow==true){
            mode_IDLE();
            ros::Duration(1.0).sleep(); // sleep for half a second
        }
        
    }
void setPointsCallback(const geometry_msgs::Twist& twist){
    nspx=twist.linear.x;
    nspy=twist.linear.y;
    sp_yaw=-atan2(nspx,nspy)*180/3.1416;
    ROS_INFO("%f,%f,%f",nspx,nspy,sp_yaw);
}

void obstCallback(const std_msgs::Float32& msg){
    if(msg.data==1){
        newobstacle = true;
    }else{
        newobstacle = false;
    }
}

void headCallback(const std_msgs::Float64& head){   
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
        if(ang_peop_cam!=-500 && mode_follow && tracking_people==false  ){
            cont_detect_peop+=1;
            missing_track=0;
            if(ang_peop_lidar<ang_peop_cam+8 && ang_peop_lidar> ang_peop_cam-8  && distanciaPeople2<aux_dist && distanciaPeople2<=near_far_distance && distanciaPeople2>50 && ang_peop_cam>-30 && ang_peop_cam<30 && ang_peop_lidar>-30 && ang_peop_lidar<30 ){
                //cont_detect_peop+=1;
                aux_dist = distanciaPeople2;
                ROS_INFO("Received angle %f",ang_peop_lidar);
                tracked_cx=cx;
                tracked_cy=cy;
                tracked_pos.x=cx;
                tracked_pos.y=cy;
                tracked_pos.z= ang_peop_lidar;
                tracked_angle=ang_peop_lidar;
                fprintf(fp2,"deteccion %f,%f,%f,%f\n",tracked_cx,tracked_cy,ang_peop_lidar,distanciaPeople2);
            }
            if(cont_detect_peop>5 && tracked_cx>0.5 && tracked_cx<near_far_distance && tracked_cy>-0.7 && tracked_cy<0.7){
                    mode_people_follow();
                    tracking_people=true;
                    cont_detect_peop=0;
                    ROS_INFO("Tracked angle %f",ang_peop_lidar);
                    fprintf(fp2,"deteccion camara %f,%f,%f,%f\n",tracked_cx,tracked_cy,ang_peop_lidar,aux_dist);
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
                    cont_sp_follow=0;//experiemntal
                    kf=0;
                    index_wp=-1;//init follow
                    dist_auxwp=0; 
                    state_stop=0;
                    is_near==true;  
                    stop_functions=false;         
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
    
  90deg -y--------------- y  -90deg
        |
        |
        |
        |
        |
     179deg -x -179 deg       
*/

void angPeopCallback4(const geometry_msgs::Vector3& msg){
save_counter++;
cicles=20;
cx = msg.x;//pos people or object
cy = msg.y;//pos people or object
ang_peop_lidar = 90- atan2(cx, cy) * 180 / 3.1416;
//ang_peop_lidar = -90+ atan2(cx, cy) * 180 / 3.1416 ;
distanciaPeople2 = sqrt(cx*cx+cy*cy)*100;
//ROS_INFO("tracked %f",ang_peop_lidar)
//ROS_INFO("m %s",mode_follow?"TRUE":"FALSE");
//ROS_INFO("d %s",danger?"TRUE":"FALSE");
// ROS_INFO("tracked %f",ang_peop_lidar)
//ROS_INFO("tracked %f,%f",tracked_cx,tracked_cy);

if(mode_follow && danger!=true){
    //ROS_INFO("tracked1 %f",ang_peop_lidar);
        if(cx!=-0.01 && cy !=-0.01 && tracking_people && cx<=(tracked_cx+radius_follow) && cx>=(tracked_cx-radius_follow) && cy<=(tracked_cy+radius_follow) && cy >=(tracked_cy-radius_follow) && stop_functions==false){//2
            //ang_peop_lidar = 90+ atan2(cx, cy) * 180 / 3.1416 ;
            //ang_peop_lidar = -90+ atan2(cx, cy) * 180 / 3.1416 ;
            
            ang_peop_lidar = 90- atan2(cx, cy) * 180 / 3.1416;
            distanciaPeople2 = sqrt(cx*cx+cy*cy)*100;
            //if(ang_peop_lidar-tracked_angle>30){}
            tracked_angle= ang_peop_lidar;
            ROS_INFO("tracked %f",tracked_angle);
            tracked_distance = distanciaPeople2;
            if(distanciaPeople2<near_far_distance){
                near();
                alert_karugamo_near_no_sound();
                if(is_near==false){
                    fprintf(fp2,"Entre near \n");
                    is_near=true;
		            stop_functions=false;
                    //alert_karugamo_near_no_sound();
                    dist_auxwp=0;
                    //cont_sp_follow=0;//experimental
                }
            }else{
                alert_karugamo_far_no_sound();
                if(is_near==true){
                    is_near=false;
                    alert_karugamo_far_no_sound();
			        stop_functions=false;
                    if(cont_sp_follow>2){
                        fprintf(fp2,"Entre far num sp follow %i e index %i  \n",cont_sp_follow,cont_sp_follow-3);
                        index_wp=cont_sp_follow-3;
                    }
                }
            }//endif not near
            ROS_INFO("hello1");
            missing_track=0;
            tracked_cx=cx;
            tracked_cy=cy;
            tracked_pos.x=cx;
            tracked_pos.y=cy;
            tracked_pos.z=tracked_angle;
            tracked_publisher.publish(tracked_pos);
            ROS_INFO("hello2");
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
                //fprintf(fp2,"%f,%f,%f,%f,%f,%f,%i\n",npcx,npcy,px,py,angobs,ang_robot,cont_sp_follow);
                fprintf(fp2,"a%f,%f,%f,%f,%f,%f,%i\n",npcx,npcy,px,py,angobs,ang_robot,cont_sp_follow);
            }
            tracking =true;
            ROS_INFO("tracked");
                
                }//end it s in range
        else if(danger==false){//losted
            //if(is_near==false){
            missing_track+=1;
                if(missing_track>28){//thiscounter also can help to see if theres a lot of objects and its not able to follow
                if(is_near==true && tracking_people && stop_functions==false){
					fprintf(fp2,"lost and near");
                    ctrl_front_follow=speed_wp_lost;
		            //ctrl_front_follow=0;
                    ctrl_yaw=0;
                    //ctrl_yaw=(1-smooth_accel_karugamo_far)*(0)+(smooth_accel_karugamo_far*ctrl_yaw);
                    vel_steer.linear.x= ctrl_front_follow;
                    vel_steer.angular.z= ctrl_yaw;
                    vel_steer.linear.x=(vel_steer.linear.x/21)*0.1045;
                    vel_steer.angular.z=(vel_steer.angular.z/21)*0.1045;
                    speed_publisher.publish(vel_steer);
                    //alert_danger_no_sound();
                    alert_collision_no_sound();
					stop_functions=true;

                    //is_near=false;
                    //alerts_command.data=3;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
                    //alerts_publisher.publish(alerts_command);
                    //if(cont_sp_follow>2){
                    //  fprintf(fp2,"Entre far por lost num sp follow %i e index %i  \n",cont_sp_follow,cont_sp_follow-3);
                    //  index_wp=cont_sp_follow-3;
                    //}
                }
                ROS_INFO("LOST");
                fprintf(fp2,"lost \n");
                tracking_people=false;
                missing_track=0;
                tracked_cx=0;
                tracked_cy=0;
                aux_dist=5000;
                tracked_pos.x=-50;
                tracked_pos.y=-50;
                missing_track=0;
                cont_detect_peop=0;
                sound_counter++;
                
                if(sound_counter%10==0){
                    alert_warning_sound();
                }
                tracking =false;
                
		
            }
            if(stop_functions==true&& tracking_people==false){
			//ctrl_front_follow=0;
                    alert_collision_no_sound();
			        ctrl_front_follow=(1-smooth_accel_stop)*(0)+(smooth_accel_stop*ctrl_front_follow);
                	ctrl_yaw=0;
                	vel_steer.linear.x= ctrl_front_follow;
                	vel_steer.angular.z= ctrl_yaw;
                    vel_steer.linear.x=(vel_steer.linear.x/21)*0.1045;
                    vel_steer.angular.z=(vel_steer.angular.z/21)*0.1045;
                	speed_publisher.publish(vel_steer);
		    }
           // }
        }//losted

//changed from here
    
if(is_near==false && stop_functions==false){
	if(save_counter%20==0){
		fprintf(fp2,"wp %f,%f,%f,%f,%f,%f,%f,%i\n",spx_saved[index_wp],spy_saved[index_wp],px,py,ctrl_front_follow,ctrl_yaw,ang_robot,index_wp);
	}
	
    if(stop_follow==false){
        ///////////////New algorithm
        if(cont_sp_follow>=2){
            if(dist_auxwp<0.4 && stop_follow==false){
                index_wp=index_wp+1;
                fprintf(fp2,"next wp %f,%f,%f,%f,%f,%f,%i\n",spx_saved[index_wp],spy_saved[index_wp],px,py,0.0,ang_robot,index_wp);
                //fprintf(fp2,"avance a index %i con posicion %f,%f \n",index_wp,px,py);
                if(index_wp>=(cont_sp_follow-1)){
                    index_wp=cont_sp_follow-1;//experimental
                    stop_follow=true;//arrived to last wp
                    fprintf(fp2,"llegue a fin con index %i ang %f \n",index_wp,ang_robot);
                    saved_ang=ang_robot;
                    sp_yaw=saved_ang;
					return;
                }else{
					calc_spline();//call to calc spline	
				}
                //angle_last=ang_robot
            }
            
            dist_auxwp=sqrt((spx_follow[19]-px)*(spx_follow[19]-px)+(spy_follow[19]-py)*(spy_follow[19]-py));//calc dist for next loop
            //fprintf(fp2,"err_dist_aux %f \n",dist_auxwp);
                    float auxdis=700000;
                for(int i=0;i<cicles;i++){//search for the nearest point in the created spline
                    float errdist=sqrt((spx_follow[i]-px)*(spx_follow[i]-px)+(spy_follow[i]-py)*(spy_follow[i]-py));
                    if(errdist<auxdis){
                        indice=i+1;
                        auxdis=errdist;
                        //fprintf(fp2,"err_dist_aux %f,%i,%i  \n",dist_auxwp,cont_sp_follow,indice);
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
                /////////////////experimental
                if(error_yaw>max_defelct_angle || error_yaw<-max_defelct_angle){
		    fprintf(fp2,"too much error_ang %f, index %i, cont %i \n",error_yaw,index_wp,cont_sp_follow);
                    if(index_wp<cont_sp_follow){
                        index_wp=index_wp+1;
                        calc_spline();
                    }
                }
                /////////////////experiemental

                spVel=0.1*(error_yaw);//0.05*(error_yaw);
                nkp=angle_gain_wp;//=0.0085;
                ctrl_yaw=(nkp*spVel)-ctrl_yaw/2;//experimental
                    if(ctrl_yaw>400){
                        ctrl_yaw=400;
                    }else if(ctrl_yaw<-400){
                        ctrl_yaw=-400;
                    }
            
            if(distanciaPeople2>100 && tracking_people ==true){
                float  norm_dist,dist_conv;
                dist_conv=distanciaPeople2;
                if(dist_conv>250){
                   dist_conv=250;
                   norm_dist=(dist_conv-100)/150;
                }else{
                   norm_dist=(dist_conv-100)/150;
                }
    
                //ctrl_front_follow=(1-smooth_accel)*(frontal_gain_follow*(distanciaPeople2-100))+(smooth_accel*ctrl_front_follow);
                //ctrl_front_follow=(1-smooth_accel)*(frontal_gain_follow*norm_dist/*max_speed_follow*/)+(smooth_accel*ctrl_front_follow);
                //ctrl_front_follow=400;
                ctrl_front_follow=(1-smooth_accel_karugamo_far)*(speed_wp_lost)+(smooth_accel_karugamo_far*ctrl_front_follow);
                //ROS_INFO("%f,%f",ctrl_front_follow,distanciaPeople2);
                if(ctrl_front_follow<0 ){
                    ctrl_front_follow=0;
                    vel_steer.linear.x=0;
                }
                if (ctrl_front_follow>max_speed_follow){
                    ctrl_front_follow= max_speed_follow;
                }
            }else{
                ctrl_front_follow=(1-smooth_accel_karugamo_far)*(speed_wp_lost)+(smooth_accel_karugamo_far*ctrl_front_follow);
            }
        }else{
            // ctrl_front_follow=0;
            //ctrl_front_follow=(1-smooth_accel_karugamo_far)*(0)+(smooth_accel_karugamo_far*ctrl_front_follow);
            ctrl_front_follow=(1-smooth_accel_stop)*(0)+(smooth_accel_stop*ctrl_front_follow);//experimental
            ctrl_yaw=0;
            ROS_INFO("stop cont_sp_follow %i \n",cont_sp_follow);
        }
            vel_steer.linear.x= ctrl_front_follow;
            vel_steer.angular.z= ctrl_yaw;
    }

        if(stop_follow==true){//stop if arrived  last wp  
                counter_search++;
                if(counter_search%350==0){
                    counter_search=0;
                    state_stop++;
                    switch(state_stop){
                        /*
                        case 1:
                            
                            sp_yaw=ang_robot;
                            saved_ang=ang_robot;
                            fprintf(fp2,"entre caso 1 ang %f \n",saved_ang);
                        break;
                        */
                        case 1:
                            
                            sp_yaw=saved_ang;
                            fprintf(fp2,"entre caso 1 ang %f \n",saved_ang);
                        break;
                        
                        case 2:
                            
                            sp_yaw=saved_ang+45;
                            if (sp_yaw < -180.0 ){
                                sp_yaw=sp_yaw+360;
                            }else if (sp_yaw > 180.0 ){
                                sp_yaw=sp_yaw-360;
                            }
                            fprintf(fp2,"entre caso 2 ang %f \n",sp_yaw);
                        break;
                        case 3:
                            sp_yaw=saved_ang;
                            fprintf(fp2,"entre caso 3 ang %f \n",sp_yaw);
                        break;
                        case 4:
                            state_stop=0;
                            sp_yaw=saved_ang-45;
                            if (sp_yaw < -180.0 ){
                                sp_yaw=sp_yaw+360;
                            }else if (sp_yaw > 180.0 ){
                                sp_yaw=sp_yaw-360;
                            }
                            fprintf(fp2,"entre caso 4 ang %f \n",sp_yaw);
                        break;
                        //case 5:
                        //    sp_yaw=saved_ang;
                        //    state_stop=0;
                        //  fprintf(fp2,"entre caso 5 ang %f \n",sp_yaw);
                       // break;  
                    }
                }
                error_yaw=(sp_yaw-ang_robot);//-(sp_yaw-ang_robot);
                if (error_yaw < -180.0 ){
                    error_yaw=error_yaw+360;
                }else if (error_yaw > 180.0 ){
                    error_yaw=error_yaw-360;
                }
                spVel=0.1*(error_yaw);//0.05*(error_yaw);
                nkp=angle_gain_wp;//=0.0085;
                ctrl_yaw=(nkp*spVel)-ctrl_yaw/2;//
                if(ctrl_yaw>300){
                    ctrl_yaw=300;
                }else if(ctrl_yaw<-300){
                    ctrl_yaw=-300;
                }
                //ctrl_front_follow=0;
                ctrl_front_follow=(1-smooth_accel_stop)*(0)+(smooth_accel_stop*ctrl_front_follow);//experimental
                //ctrl_yaw=0;
                vel_steer.linear.x= ctrl_front_follow;
                vel_steer.angular.z= ctrl_yaw;
                alert_collision_no_sound();
                //fprintf(fp2,"calc sp %f, ctrl %f \n",sp_yaw,ctrl_yaw);
        }
            vel_steer.linear.x=(vel_steer.linear.x/21)*0.1045;
            vel_steer.angular.z=(vel_steer.angular.z/21)*0.1045;
            speed_publisher.publish(vel_steer);
}//end_isnear=false
}//end mode follow
}//end function



void calc_spline(){
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
        ROS_INFO("Rcalc %f,%f,%f \n",Rx,Ry,angle);
        fprintf(fp2,"Rcalc %f,%f,%f \n",Rx,Ry,angle);
        posestamped.header.frame_id="/my_frame";
        posestamped.header.stamp = ros::Time::now();
        posestamped.pose.position.x=Rx;
        posestamped.pose.position.y=Ry;
        path.header.stamp = ros::Time::now();
        path.header.frame_id="/my_frame";
        path.poses.push_back(posestamped);
        path_pub.publish(path);
    }

}



///////////////////

void near(){

        //cx = msg.x;
        //cy = msg.y;
        //ang_peop_lidar = 90- atan2(cx, cy) * 180 / 3.1416 ;//-90+ atan2(cx, cy) * 180 / 3.1416 ;
        //distanciaPeople2 = sqrt(cx*cx+cy*cy)*100;
        // ROS_INFO("R%f,%f,%f,%f",cx,cy,ang_peop_lidar,distanciaPeople2);
       if(mode_follow && danger!=true && stop_functions==false){ //&& tracking_people){//1
            //     ROS_INFO("R%f,%f",cx,cy);
            //     ROS_INFO("P%f,%f",tracked_cx,tracked_cy);
            if(save_counter%20==0){
            fprintf(fp2,"near %f,%f,%f,%f,%i\n",px,py,0.0,ang_robot,index_wp);
            }
            if( cx!=-0.01 && cy !=-0.01 && ang_peop_lidar<120 && ang_peop_lidar>-120 && tracking_people && cx<=(tracked_cx+radius_follow) && cx>=(tracked_cx-radius_follow) && cy<=(tracked_cy+radius_follow) && cy >=(tracked_cy-radius_follow)){//2
                //correccion needed
                //ang_peop_lidar = -90+ atan2(cx, cy) * 180 / 3.1416 ;// ;  90- atan2(cx, cy) * 180 / 3.1416 
                ang_peop_lidar = 90- atan2(cx,cy) * 180 / 3.1416 ;// ;  -90+ atan2(cx, cy) * 180 / 3.1416 
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
                

                ctrl_ang= low_vel_gain_follow*ang_peop_lidar-ctrl_ang/2;

                if (ctrl_ang>500){
                    ctrl_ang= 500;
                }else if (ctrl_ang<-500){
                    ctrl_ang= -500;
                }
                vel_steer.angular.z=ctrl_ang;//low_vel_gain*msg.data;//*(distanciaPeople/40);

                if(distanciaPeople2>dist_robot_people){//dist_robot_people
                    float  norm_dist,dist_conv;
                    dist_conv=distanciaPeople2;
                    if(dist_conv>max_dist_toacc){
                        dist_conv=max_dist_toacc;
                        norm_dist=(dist_conv-dist_robot_people)/(max_dist_toacc-dist_robot_people);
                    }else{
                     norm_dist=(dist_conv-dist_robot_people)/(max_dist_toacc-dist_robot_people);
                    }

                    //ctrl_front_follow=(1-smooth_accel)*(frontal_gain_follow*(distanciaPeople2-100))+(smooth_accel*ctrl_front_follow);
                    ctrl_front_follow=(1-smooth_accel_karugamo_near)*(frontal_gain_follow*norm_dist/*max_speed_follow*/)+(smooth_accel_karugamo_near*ctrl_front_follow);
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
                    ctrl_front_follow=(1-smooth_accel_stop)*(0)+(smooth_accel_stop*ctrl_front_follow);
                    vel_steer.linear.x=0;
                    //ctrl_front_follow=0;
                }
                //if(stop_follow==true||tracking_people==false){
                //if(stop_follow==true){
                //if(tracking_people==false){
                //    vel_steer.linear.x=0;
                //    vel_steer.angular.z=0;
                //}
                //stop_follow=false;
                vel_steer.linear.x=(vel_steer.linear.x/21)*0.1045;
                vel_steer.angular.z=(vel_steer.angular.z/21)*0.1045;
                //alerts_command.data=7;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
                //alerts_publisher.publish(alerts_command);
                speed_publisher.publish(vel_steer);
            }

        }//mode3
       
    }  



///////////////////


    void scanCallback(const sensor_msgs::LaserScan::ConstPtr& scan)
    {
        int count = scan->scan_time / scan->time_increment;
        //float  break_distance=1.5;
            //float  break_danger=0.5;
        if(detect_cont>1){
                danger=true;
                free_way=false;
                ROS_INFO("Danger1");
                danger_counter++;
                alert_danger_no_sound();
                if(danger_counter%60==0){
                    alert_danger_sound();
                }
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
        }else{
            free_way=true;
        }
        for(int j=269;j<=358;j++){
            if (scan->ranges[j] <= break_danger && scan->ranges[j] >0.24 && mode_idle==false){
               detect_cont++;   
                return;
             }  
        }
        for(int i=0;i<=90;i++){
            if (scan->ranges[i] <= break_danger && scan->ranges[i] >0.24 && mode_idle==false){
               detect_cont++;
               return;
                }
            
        }
        for(int j=328;j<=358;j++){
            if (scan->ranges[j] <= break_distance && scan->ranges[j] >0.24 && mode_idle==false){
                 detect_cont++;
                     return;
             }
        }
        for(int i=0;i<=30;i++){
            if (scan->ranges[i] <= break_distance && scan->ranges[i] >0.24 && mode_idle==false){
               detect_cont++;
               return;
              }
/////
            else{
                detect_cont=0;
                free_way=true;
                if(mode_manual && danger){
                    danger=false;
                    alert_manual_sound();
                }if(mode_karugamo && danger){
                    danger=false;
                    alert_karugamo_near_sound();
                }
                if(mode_follow && danger){
                    danger=false;
                    alert_karugamo_near_sound();
                    //alert_danger_sound();
                }if(mode_auto && danger){
                    danger=false;
                    alert_karugamo_near_sound();
                    
                }
                    //danger=false;
            }
////////
                 }
        


/////////
    }


//////// alerts
void alert_collision_sound(){
    alerts_command.data=6;//6 collision 5 danger 4 warning 3 karugamo 2 idle 1 manual
    alerts_publisher.publish(alerts_command);
}
void alert_collision_no_sound(){
    alerts_command.data=76;//6 collision 5 danger 4 warning 3 karugamo 2 idle 1 manual
    alerts_publisher.publish(alerts_command);
}
void  alert_manual_sound(){
    alerts_command.data=1;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
    alerts_publisher.publish(alerts_command);
}
void  alert_manual_no_sound(){
    alerts_command.data=71;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
    alerts_publisher.publish(alerts_command);
}
void  alert_idle_sound(){
    alerts_command.data=2;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
    alerts_publisher.publish(alerts_command);
}
void  alert_idle_no_sound(){
    alerts_command.data=72;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
    alerts_publisher.publish(alerts_command);
}

void  alert_warning_sound(){
    alerts_command.data=4;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
    alerts_publisher.publish(alerts_command);
}
void  alert_warning_no_sound(){
    alerts_command.data=74;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
    alerts_publisher.publish(alerts_command);
}
void  alert_danger_sound(){
    alerts_command.data=5;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
    alerts_publisher.publish(alerts_command);
}
void  alert_danger_no_sound(){
    alerts_command.data=75;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
    alerts_publisher.publish(alerts_command);
}

void  alert_karugamo_near_sound(){
    alerts_command.data=8;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
    alerts_publisher.publish(alerts_command);
}
void  alert_karugamo_near_no_sound(){
    alerts_command.data=78;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
    alerts_publisher.publish(alerts_command);
}
void  alert_karugamo_far_sound(){
    alerts_command.data=3;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
    alerts_publisher.publish(alerts_command);
}
void  alert_karugamo_far_no_sound(){
    alerts_command.data=73;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
    alerts_publisher.publish(alerts_command);
}



//////// alerts

void collisioned(){
    collision =true;
    vel_steer.linear.x= 0;
    vel_steer.angular.z= 0;
    speed_publisher.publish(vel_steer);
    alert_collision_sound();
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
    vel_steer.linear.x= 0;
    vel_steer.angular.z= 0;
    speed_publisher.publish(vel_steer);
}

void remove_collision(){
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
    alert_idle_sound();
    vel_steer.linear.x= 0;
    vel_steer.angular.z= 0;
    speed_publisher.publish(vel_steer);
    tracked_angle=0;
    ang_peop_lidar=0;
    distanciaPeople2=0;
    tracked_distance=0;
}


void mode_MANUAL(){
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
    ctrl_front_follow= 0;
    ctrl_ang= 0;
    ctrl_front_manual= 0;
    ctrl_side_manual= 0;
    vel_steer.linear.x= 0;
    vel_steer.angular.z= 0;
    speed_publisher.publish(vel_steer);
}
void mode_IDLE()
{
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
    ctrl_yaw = 0;
    ctrl_front_manual= 0;
    ctrl_side_manual= 0;
    alert_idle_sound();
    for (int i=0;i<10;i++){
        vel_steer.linear.x= 0;
        vel_steer.angular.z= 0;
        speed_publisher.publish(vel_steer);
    }
}

void mode_people_follow()
{
    mode_idle=false;
    mode_karugamo=false;
    mode_manual=false;
    mode_follow=true;
    tracking_people=false;
    start_route = false;
    mode_auto=false;
    ctrl_front_follow= 0;
    ctrl_ang= 0;
    ctrl_yaw = 0;
    ctrl_front_manual= 0;
    ctrl_side_manual= 0;
    cont_sp_follow=0;
    kf=1;
    counter_search=340;
    alert_karugamo_near_sound();
    ROS_INFO("Mode People Follow");
    stop_follow=false;
    aux_dist=50000;
    is_near=true;
    fp2 = fopen ("/home/xavier/catkin_ws/src/control_xy/people.txt" , "w+");
    fprintf(fp2,"pobx,poby,px,py,ang,angr,num \n");
    //alerts_command.data=7;//7 peop follow 5 danger 4 warning 3 karugamo 2 idle 1 manual
    index_wp=-1;//init follow
    dist_auxwp=0;
    stop_functions=false;
    
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
        //  save_waypoint=true;
        //  ros::Duration(0.4).sleep(); // sleep for half a second
        //  
//
        }else if(joy->buttons[2]==1 && free_way==true && collision == false){//danger!=true && free_way==true){//circulo
            mode_IDLE();
            ros::Duration(0.5).sleep(); // sleep for half a second
            
        //}else if(joy->buttons[1]==1 && danger!=true && collision == false){//equis
        }else if(joy->buttons[1]==1 && collision == false){//equis
            mode_MANUAL();

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
            mode_people_follow();
            vel_steer.linear.x=0;
            vel_steer.angular.z=0;
            speed_publisher.publish(vel_steer);
            ros::Duration(0.5).sleep(); // sleep for half a second
        }

        if(mode_manual){
              if(free_way){
              //if(true){
                ctrl_front_manual=(1-smooth_accel_manual)*(joy->axes[1]*max_speed_manual)+(smooth_accel_manual*ctrl_front_manual);
                //if(ctrl_front_manual<20 && ctrl_front_manual>-20){
                //  ctrl_front_manual=0;
                //}
                vel_steer.linear.x= ctrl_front_manual;
                //vel_steer.linear.x=-joy->axes[1]*-max_speed_manual;
                ctrl_side_manual=(1-smooth_accel_side_manual)*(joy->axes[0]*max_speed_side_manual)+(smooth_accel_side_manual*ctrl_side_manual);
               
                //if(ctrl_side_manual<7 && ctrl_side_manual>-7){
                //    ctrl_side_manual=0;
                //}
                vel_steer.angular.z=ctrl_side_manual;
               
                if(joy->axes[7]!=0){
                        vel_steer.linear.x=joy->axes[7]*max_speed_manual;
                }
                if(joy->axes[6]!=0){
                        vel_steer.angular.z=joy->axes[6]*-800;
                }
                vel_steer.linear.x=(vel_steer.linear.x/21)*0.1045;
                vel_steer.angular.z=(vel_steer.angular.z/21)*0.1045;
                speed_publisher.publish(vel_steer);
        }else{//else free way
        
            ctrl_front_manual=(1-smooth_accel_manual)*(joy->axes[1]*max_speed_manual)+(smooth_accel_manual*ctrl_front_manual);
            if(ctrl_front_manual<0){
                ctrl_side_manual=(1-smooth_accel_side_manual)*(joy->axes[0]*max_speed_side_manual)+(smooth_accel_side_manual*ctrl_side_manual);
                if(ctrl_side_manual<7 && ctrl_side_manual>-7){
                    ctrl_side_manual=0;
                }
                vel_steer.linear.x= ctrl_front_manual;
                vel_steer.angular.z=ctrl_side_manual;
                vel_steer.linear.x=(vel_steer.linear.x/21)*0.1045;
                vel_steer.angular.z=(vel_steer.angular.z/21)*0.1045;
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
    ros::Publisher path_pub;
    geometry_msgs::Twist vel_steer;
    geometry_msgs::Vector3 tracked_pos;
    std_msgs::Float32 ang_people;
    visualization_msgs::Marker people_point;
    nav_msgs::Path path;
    geometry_msgs::PoseStamped posestamped;


    bool save_waypoint,start_tray,col_avoid_mode,danger, mode_idle,mode_karugamo,mode_manual,mode_follow,free_way,collision,mode_auto;
    float angulo_seguimiento,sp_yaw,sp_yaw2,ctrl_yaw,error_yaw,yaw,distanciaPeople,distanciaPeople2,break_distance,break_danger,max_speed_karugamo,max_speed_follow,max_speed_manual,ctrl_ang,ctrl_lin;
    float px,py,norm,norm2,x_ini,y_ini,x_p,y_p,px2,py2,spx,spy,err_x,err_y,err_xx,err_yy,low_vel_gain,high_vel_gain,low_vel_gain_follow,high_vel_gain_follow,smooth_accel,ctrl_side_manual,max_speed_side_manual;
    char rx[80],ry[80],rx2[80],ry2[80],pa[80],yag[80];
    float sp_rx[1000],sp_ry[1000],sp_rx2[1000],sp_ry2[1000],param[1000],sp_yaww[1000];
    float spx_follow[25],spy_follow[25],angle_follow[25],prev_cx,prev_cy;
    float spx_saved[10000],spy_saved[10000];
    int count,count2,ca,direction,count_odo,cont_detect_peop,cont_sp_follow,kf;
    FILE * fp;
    FILE * fp2;
    bool obstaculo,changed,crucero,ruta_learn,loaded_route,start_route,arrived,obstacle_front,obstacle_front1,obstacle_front2,newobstacle,tracking_people;
    float px_aux,py_aux,n_aux,last_error,alfa,velx,err2,velyaw,intErr,velCtrl,nspx,nspy,errPos,ang_peop_cam,ang_peop_lidar,tracked_angle,tracked_distance,radius_follow,tracked_cx,tracked_cy;
    int num_sp,k_idx,carril,velocity,contadorvel,mode,indx,h,conta,missing_track;
    ros::Time time_obst,time_cruce,time_obst_last,time_cruce_last;
    float errpx,errpy,spVel,nkp,nkd,nki,errVelYaw,nvkp,nvkd,spPos,distAct,errPVel,spPVel;
    float ctrl_vel,frontal_gain_follow,frontal_gain_karugamo,frontal_gain_manual,ctrl_front_follow,ctrl_front_karugamo;
    float ctrl_front_manual,cx,cy,aux_dist,ang_robot;

    float spx_follow_old,spy_follow_old,spx_follow_new,spy_follow_new,dist_auxwp;
    int indice,index_wp,numwp,cicles,detect_cont;
    bool tracking,is_near,stop_follow,stop_functions;
    int sound_counter,danger_counter;
    int counter_search,state_stop;
    float saved_ang,speed_wp_lost;
    float near_far_distance;
    float angle_last,max_defelct_angle;
	int save_counter;
    float dist_robot_people,smooth_accel_manual,smooth_accel_karugamo_near,smooth_accel_karugamo_far,angle_gain_wp,max_dist_toacc;
    float smooth_accel_stop,smooth_accel_side_manual;
};

int main(int argc, char **argv)
{
    ros::init(argc, argv, "heading_follow_node");
    ros::NodeHandle nh; 

    test_head test_head_obj(nh);
    //ros::Rate rate(0.5); //0.5 Hz, every 2 second
    ros::Rate rate(60); //100 Hz, every .01 second
    //printf("%f",-atan2(5,1)*180/3.1416);
    while(ros::ok())
    {
        
        ros::spinOnce();
        rate.sleep();
    }
    return 0;
}

