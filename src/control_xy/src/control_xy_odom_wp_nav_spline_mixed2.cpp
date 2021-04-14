
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
#include <control_xy/StateWheels.h>
#include <control_xy/States.h>
#include <visualization_msgs/Marker.h>
#include <nav_msgs/Odometry.h>
#include <nav_msgs/Path.h> 


class test_head
{
public:
    test_head(ros::NodeHandle nh)
    {
        m1_pub =nh.advertise<geometry_msgs::Vector3>(nh.resolveName("/m1_deriv"), 1);
        m2_pub =nh.advertise<geometry_msgs::Vector3>(nh.resolveName("/m2_deriv"), 1);
        speed_publisher=nh.advertise<geometry_msgs::Twist>(nh.resolveName("/cmd_vel"), 1);
        tracked_publisher=nh.advertise<geometry_msgs::Vector3>(nh.resolveName("/tracked"), 2);
        alerts_publisher=nh.advertise<std_msgs::Int16>(nh.resolveName("/alerts"), 1);
        marker_pub   = nh.advertise<visualization_msgs::Marker>(nh.resolveName("/visualization_marker"),1);
        pos_peop_pub = nh.advertise<nav_msgs::Odometry>(nh.resolveName("/peop_way"),1);
        yolo_peop_pub = nh.advertise<nav_msgs::Odometry>(nh.resolveName("/yolo_peop_way"),1);
        estim_pub = nh.advertise<nav_msgs::Odometry>(nh.resolveName("/estim_peop_way"),1);
        path_pub = nh.advertise<nav_msgs::Path>(nh.resolveName("/pathpeop"),1);
        state_pub = nh.advertise<control_xy::States>(nh.resolveName("/pitakuru_states"),1);

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
        //ang_subscriber_cam = nh.subscribe("ang_peop_detect_img", 1, &test_head::angCamCallback2,this);
        dist_subscriber2 = nh.subscribe("peopDist2", 1, &test_head::distPeopCallback2,this);
        obst_subscriber = nh.subscribe("/obstacle_closest", 1, &test_head::obstCallback,this);
        state_subscriber = nh.subscribe("/trigger_action", 1, &test_head::stateCallback,this);
        //sub_amperage = nh.subscribe("/amperage",1,&test_head::amperageCallback,this);
        sub_amperage = nh.subscribe("/stateWheels",1,&test_head::amperageCallback,this);
        volts_subscriber = nh.subscribe("/volts", 1, &test_head::voltsCallback,this);
        cost_subscriber = nh.subscribe("/costdetect", 1, &test_head::costCallback,this);
        yolo_subscriber = nh.subscribe("/peop_ang_yolo", 1, &test_head::yoloCallback,this);
        sub_estim = nh.subscribe("/estimated_people", 1, &test_head::estimCallback,this);
       
        //nh.param<float>("break_distance", break_distance, 1.5);
        nh.getParam("/control_xy/break_front_distance", break_front_distance);
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
        nh.getParam("/control_xy/max_speed_manual_heavy", max_speed_manual_heavy);
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
        nh.getParam("/control_xy/tresh_amp_up",tresh_amp_up);
        nh.getParam("/control_xy/tresh_amp_down",tresh_amp_down);
        nh.getParam("/control_xy/trigger_vel",trigger_vel);
        nh.getParam("/control_xy/trigger_current",trigger_current);
        nh.getParam("/control_xy/max_l_curr",max_r_curr);
        nh.getParam("/control_xy/vel_detect_scan",vel_detect_scan);
        nh.getParam("/control_xy/volts_charge",volts_charge);
        nh.getParam("/control_xy/avg_curr_tresh",avg_curr_tresh);
        nh.getParam("/control_xy/peak_curr_tresh",peak_curr_tresh);
        nh.getParam("/control_xy/peak_not_heavy_curr",peak_not_heavy_curr);
        nh.getParam("/control_xy/count_to_miss",count_to_miss);
        nh.getParam("/control_xy/gain_to_costmap",gain_to_costmap);
        nh.getParam("/control_xy/smooth_accel_costmap",smooth_accel_costmap);
        nh.getParam("/control_xy/vel_detect_costmap",vel_detect_costmap);
        nh.getParam("/control_xy/duration_to_lost",duration_to_lost);
        nh.getParam("/control_xy/min_break_distance",min_break_distance);
        nh.getParam("/control_xy/max_break_distance",max_break_distance);
        //nh.param<float>("break_danger", break_danger, 0.45);
        subScan_ = nh.subscribe("/scan", 1, &test_head::scanCallback,this);
        ROS_INFO_STREAM("******break_distance "<< break_front_distance << " break danger " << break_danger << " low vel gain " << low_vel_gain << " high vel gain " << high_vel_gain
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
        heavy=true;
        n_flag_r=false;
        d_flag_r=true;
        n_flag_l=false;
        d_flag_l=true;
        heavy_r=0;
        heavy_l=0;
        detected_heavy=false;
        tracking_lidar=false;
        tracking_yolo=false;
        find_again=false;
        changed_setting=false;
        count_again=0;
        aux_dist_again=5000;
        duration_change=0.30;
        low_voltage=false;
        counter_changed=0;
        started_track_yolo=false;
        lidar_failed=false;
        joy_counter=0;
        karugamo_counter=0;
       
    }
    ~test_head(){}
   

void stateCallback(const control_xy::TriggerAction& data){
        //ROS_INFO("Controlxy ");
        //ROS_INFO("%s ",data.trigger.c_str());
        if(data.trigger=="collision" && collision==false){
            collisioned();
            collision=true;
            ros::Duration(0.5).sleep(); // sleep for half a second
        //  ROS_INFO("Yuhu");
        //  ROS_INFO("%s ",data.trigger.c_str());
        }else if(data.trigger=="break_release_button_on" && collision ==true){
            remove_collision();
            mode_IDLE();
            ros::Duration(0.5).sleep(); // sleep for half a second
        } else if(data.trigger=="karugamo_button_on" && mode_follow==false  && collision == false){
            mode_people_follow();
            vel_steer.linear.x=0;
            vel_steer.linear.y= 1;
            vel_steer.angular.z=0;
            speed_publisher.publish(vel_steer);
            ros::Duration(0.4).sleep(); // sleep for half a second
            //ros::Duration(1.0).sleep(); // sleep for half a second
        } else if(data.trigger=="karugamo_button_on" && mode_follow==true  && collision ==false){
            mode_IDLE();
            ros::Duration(0.4).sleep(); // sleep for half a second
        }
       
    }
void setPointsCallback(const geometry_msgs::Twist& twist){
    nspx=twist.linear.x;
    nspy=twist.linear.y;
    sp_yaw=-atan2(nspx,nspy)*180/3.1416;
    ROS_INFO("%f,%f,%f",nspx,nspy,sp_yaw);
}

void check_low_volt(){
    if(low_voltage && lidar_failed ==false && danger==false  ){
        blink_red(0.6);
    }
}

void voltsCallback(const std_msgs::Float32& msg){
    //ROS_INFO("voltage %f",msg.data);
    if((msg.data+0.1)<volts_charge ){//&& mode_idle == true){
        //ros::Time time_now = ros::Time::now();
        //ros::Duration duration = time_now - time_blink_volts  
        counter_low_voltage++;
        if((abs(vel_m1)>0.15 || abs(vel_m2)>0.15) && counter_low_voltage>1 && (mode_manual ||mode_follow) && danger==false){
            if(low_voltage==false){
                alert_low_battery_sound();
                low_voltage=true;
                low_voltage=true;
                ROS_INFO("detected_low voltage");
                ros::Duration(0.05).sleep(); // sleep for 0.05 seconds
                alert_low_battery_sound();
            }
            
        }
       
    }else{
       
        counter_low_voltage=0;
    }
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

void costCallback(const geometry_msgs::Vector3& vector){  
    cost_obst=vector.x;
    //ROS_INFO("lcost %f",cost_obst);
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
            fprintf(fp,"%f %f\n",px,py );
            px_aux=px;
            py_aux=py;
            ROS_INFO("NP %f,%f",px,py);
        }
    }
   
}


void amperageCallback(const control_xy::StateWheels& msg){
    float flag;
    //float int_r_curr,int_l_curr,der_r_curr,der_l_curr,filt_r_curr,filt_r_curr;
    //float32 left_vel float32 right_vel float32 left_current float32 right_current time time_stamp
    float alfa = 0.9;
    float trig_vel=0.25;
    float dt =0.02;
    //float alf=0.7;
    float alf=0.75;
    geometry_msgs::Vector3 newmsg;
    vel_m1 = abs(msg.left_vel);
    vel_m2 = abs(msg.right_vel);
    if(abs(msg.right_vel)<trig_vel&& abs(msg.left_vel)<trig_vel){
        int_r_curr=0;
        der_r_curr=0;
        n_flag_r=false;
        d_flag_r=false;
        max_r_curr=0;
        avg_amp_r=0;
        fil_der_r_curr=0;
        heavy_r=0;
        heavy=true;
        //alert_manual_no_sound();
        detected_heavy=false;
    }else{
        int_r_curr=int_r_curr+msg.right_current*dt;
        der_r_curr=(msg.right_current-prev_r_curr)/dt;
        fil_der_r_curr= fil_der_r_curr*alf+ der_r_curr*(1-alf);
        prev_r_curr=msg.right_current;
        if(fil_der_r_curr>0.4 && detected_heavy==false){
            if(n_flag_r==false){
                time_last_to_heavy = ros::Time::now().toSec();
            }
            n_flag_r=true;
           
            //alert_collision_no_sound();
            if(msg.right_current>max_r_curr){
                max_r_curr=msg.right_current;
            }
        }else{
            //alert_manual_no_sound();
        }
        //if(der_r_curr<0.01 && d_flag==true && n_flag==true){
        if(fil_der_r_curr<0.01 && n_flag_l==true && detected_heavy==false){
           
            amp_count_r++;
            avg_amp_r=avg_amp_r+msg.right_current;
            if(amp_count_r>2 ){
                amp_count_r=0;
                avg_amp_r=avg_amp_r/4;
                d_flag_r=false;
               
                if(avg_amp_r>avg_curr_tresh && max_r_curr >peak_curr_tresh ){//&& int_r_curr>1.87){
                    //alert_karugamo_near_no_sound();
                    heavy_r=1;
                    detected_heavy=true;
                    ROS_INFO("probable heavy load right");
                    ROS_INFO("%f integ r_",int_r_curr);
                    ROS_INFO("%f max %f avg",max_r_curr,avg_amp_r);
                }else  if (max_l_curr <peak_not_heavy_curr){
                    heavy_r=2;
                }
            }
            //ROS_INFO("entered in change right");
        }
    }
    newmsg.x=msg.right_current;
    newmsg.y=fil_der_r_curr;
    newmsg.z=int_r_curr;
    m1_pub.publish(newmsg);
   
    if(abs(msg.left_vel)<trig_vel && abs(msg.right_vel)<trig_vel){
        int_l_curr=0;
        der_l_curr=0;
        n_flag_l=false;
        d_flag_l=false;
        max_l_curr=0;
        avg_amp_l=0;
        fil_der_l_curr=0;
        heavy_l=0;
        heavy=true;
        //alert_manual_no_sound();
        detected_heavy=false;
    }else{
        int_l_curr=int_l_curr+msg.left_current*dt;
        der_l_curr=(msg.left_current-prev_l_curr)/dt;
       
        fil_der_l_curr= fil_der_l_curr*alf+ der_l_curr*(1-alf);
        prev_l_curr=msg.left_current;
       
        if(fil_der_l_curr>0.4 && detected_heavy==false){
            n_flag_l=true;
            if(heavy_l ==0 && heavy_r ==0 ){
                //alert_collision_no_sound();
            }
           
            if(msg.left_current>max_l_curr){
                max_l_curr=msg.left_current;
            }
        }else{
            //alert_manual_no_sound();
        }
        //if(der_r_curr<0.01 && d_flag==true && n_flag==true){
        if(fil_der_l_curr<0.01 && n_flag_l==true && detected_heavy==false){
            //alert_idle_no_sound();
            //alert_danger_no_sound();
            amp_count_l++;
            avg_amp_l=avg_amp_l+msg.left_current;
            if(amp_count_l>2 ){
                amp_count_l=0;
                avg_amp_l=avg_amp_l/4;
                d_flag_l=false;
               
                if(avg_amp_l>avg_curr_tresh && max_l_curr >peak_curr_tresh){//&& int_r_curr>1.87){
                    heavy_l=1;
                    detected_heavy=true;
                    //alert_karugamo_near_no_sound();
                    ROS_INFO("probable heavy load right");
                    ROS_INFO("%f integ r_",int_l_curr);
                    ROS_INFO("%f max %f avg",max_l_curr,avg_amp_l);
                }else if (max_l_curr <peak_not_heavy_curr){
                    heavy_l=2;
                }  
            }
            ROS_INFO("entered in change right");
        }
    }

    if(heavy==true && heavy_l==1 || heavy_r==1 && detected_heavy==false && (ros::Time::now().toSec() - time_last_to_heavy)<6.9){
        //alert_karugamo_near_no_sound();
        heavy=true;
    }else if(detected_heavy==false && heavy_l==2 && heavy_r==2 && (ros::Time::now().toSec() - time_last_to_heavy)>4.3 && (ros::Time::now().toSec() - time_last_to_heavy)<6.3 && abs(msg.left_vel)>4.1 && abs(msg.right_vel)>4.1 ){
        heavy=false;
        //alert_idle_no_sound();
    }
    //ROS_INFO("%f time",ros::Time::now().toSec());
    newmsg.x=msg.left_current;
    newmsg.y=der_l_curr;
    newmsg.z=int_l_curr;
    m2_pub.publish(newmsg);    
}

void distPeopCallback(const std_msgs::Float32& msg){
    distanciaPeople=msg.data;
}

void distPeopCallback2(const std_msgs::Float32& msg){
    //distanciaPeople2=msg.data;
}



void estimCallback(const geometry_msgs::Vector3& msg){

    nav_msgs::Odometry odomp;
    odomp.header.stamp = ros::Time::now();
    odomp.header.frame_id="base_link";
    odomp.pose.pose.position.x=msg.x;
    odomp.pose.pose.position.y=msg.y;
    odomp.pose.pose.position.z=0.0;
    odomp.pose.pose.orientation.w=1.0;
    estim_pub.publish(odomp);
   
   
}


///yolo subs
void yoloCallback(const geometry_msgs::Vector3& msg){
    yolo_status=msg.x;
    dist_peop_cam=msg.y*100;
    ang_peop_cam=msg.z;
    float pcx=msg.y*cos(msg.z*3.1416/180);
    float pcy=msg.y*sin(msg.z*3.1416/180);
    //if(yolo_status==1 && tracking_people==true){//tracked
    nav_msgs::Odometry odomp;
    odomp.header.stamp = ros::Time::now();
    odomp.header.frame_id="base_link";
    odomp.pose.pose.position.x=pcx;
    odomp.pose.pose.position.y=pcy;
    odomp.pose.pose.position.z=0.0;
    odomp.pose.pose.orientation.w=1.0;
    yolo_peop_pub.publish(odomp);
}

/* void match_lidar_people(){
    if(ang_peop_cam!=-500 && mode_follow && tracking_people==false  ){
        cont_detect_peop+=1;
        //missing_track=0;
        ROS_INFO("yolo %f,%f,%f,%f",ang_peop_cam,ang_peop_lidar,distanciaPeople2,dist_peop_cam);
        if(ang_peop_lidar<ang_peop_cam+6 && ang_peop_lidar> ang_peop_cam-6  && distanciaPeople2<aux_dist && distanciaPeople2<=near_far_distance && distanciaPeople2>50 && ang_peop_cam>-45 && ang_peop_cam<45 && ang_peop_lidar>-45 && ang_peop_lidar<45 ){
           
            //missing_track=0;
            //cont_detect_peop+=1;
            aux_dist = distanciaPeople2;
            ROS_INFO("Received angle %f",ang_peop_lidar);
            tracked_cx=cx;
            tracked_cy=cy;
            tracked_pos.x=cx;
            tracked_pos.y=cy;
            tracked_pos.z= ang_peop_lidar;
            tracked_angle=ang_peop_lidar;
            //fprintf(fp2,"deteccion %f,%f,%f,%f\n",tracked_cx,tracked_cy,ang_peop_lidar,distanciaPeople2);
        }
        if(cont_detect_peop>10 && tracked_cx>0.3 && tracked_cx<near_far_distance && tracked_cy>-1.0 && tracked_cy<1.0){
                //mode_people_follow();
                tracking_people=true;
                cont_detect_peop=0;
                //ROS_INFO("Tracked angle %f",ang_peop_lidar);
                fprintf(fp2,"deteccion camara %f,%f,%f,%f\n",tracked_cx,tracked_cy,ang_peop_lidar,aux_dist);
                tracked_distance=distanciaPeople2;
                tracking_people=true;
                aux_dist=5000;
                missing_track=0;
                big_angle_error_lidar_yolo=false;
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
                ctrl_side_costmap=0;
                //fp = fopen ("/home/xavier/catkin_ws/src/control_xy/people.txt" , "w+");
        }else if(cont_detect_peop>12){
            cont_detect_peop=0;
            tracking_people=false;
            ROS_INFO("Fail");
            aux_dist=5000;
        }
    }
}

void match_lidar_people_again(){
    if(ang_peop_lidar!=-500 && mode_follow){
        cont_detect_peop+=1;
        //missing_track=0;
        ROS_INFO("yolo %f,%f,%f,%f",ang_peop_cam,ang_peop_lidar,distanciaPeople2,dist_peop_cam);
        if(ang_peop_lidar<ang_peop_cam+6 && ang_peop_lidar> ang_peop_cam-6  && distanciaPeople2<aux_dist && distanciaPeople2<=near_far_distance && distanciaPeople2>50 && ang_peop_cam>-40 && ang_peop_cam<40 && ang_peop_lidar>-40 && ang_peop_lidar<40 ){
           
            //missing_track=0;
            //cont_detect_peop+=1;
            aux_dist = distanciaPeople2;
            ROS_INFO("Received angle %f",ang_peop_lidar);
            tracked_cx=cx;
            tracked_cy=cy;
            tracked_pos.x=cx;
            tracked_pos.y=cy;
            tracked_pos.z= ang_peop_lidar;
            tracked_angle=ang_peop_lidar;
            //fprintf(fp2,"deteccion %f,%f,%f,%f\n",tracked_cx,tracked_cy,ang_peop_lidar,distanciaPeople2);
        }
        if(cont_detect_peop%8==0 && tracked_cx>0.3 && tracked_cx<near_far_distance && tracked_cy>-1.0 && tracked_cy<1.0){
                //mode_people_follow();
                tracking_people=true;
                cont_detect_peop=0;
                //ROS_INFO("Tracked angle %f",ang_peop_lidar);
                fprintf(fp2,"deteccion camara again %f,%f,%f,%f\n",tracked_cx,tracked_cy,ang_peop_lidar,aux_dist);
                tracked_distance=distanciaPeople2;
                tracking_people=true;
                aux_dist=5000;
                missing_track=0;
                big_angle_error_lidar_yolo=false;
                tracked_pos.x=tracked_cx;
                tracked_pos.y=tracked_cy;
                tracked_pos.z= ang_peop_lidar;
                stop_follow=false;
                tracked_publisher.publish(tracked_pos);
                cont_sp_follow=0;//experiemntal
                kf=0;
                index_wp=-1;//init follow
                dist_auxwp=0;
                state_stop=0;
                is_near==true;
                stop_functions=false;
                ctrl_side_costmap=0;
                //fp = fopen ("/home/xavier/catkin_ws/src/control_xy/people.txt" , "w+");
        }else if(cont_detect_peop%9==0){
            cont_detect_peop=0;
            tracking_people=false;
            ROS_INFO("Fail");
            aux_dist=5000;
        }
    }
} */


///end yolo sub



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
void blink_blue(int countr, int dur){
    if(countr%dur==0){
        if(status_led_blue){
            status_led_blue=false;
            alert_karugamo_near_no_sound();
        }else{
            status_led_blue=true;
            alert_turn_off_led();
        }
    }
}
void blink_blue2(float dur){
    ros::Time time_now = ros::Time::now();
    //ros::Duration(1.5).sleep();
    //ros::Time time_end = ros::Time::now();
    ros::Duration duration = time_now - time_blink_bl;
    //ROS_INFO("Slept for %lf secs", duration.toSec());
    //double tn = ros::Time::now().toSec();
    //ROS_INFO("time %d",tn-time_blink_bl);//tn-time_blink_bl);
    if((duration.toSec())>dur){
        //ROS_INFO("entered");
        time_blink_bl=time_now;
        if(status_led_blue){
            status_led_blue=false;
            alert_karugamo_near_no_sound();
        }else{
            status_led_blue=true;
            alert_turn_off_led();
        }
    }
}


void blink_red(float dur){
    ros::Time time_now = ros::Time::now();
    //ros::Duration(1.5).sleep();
    //ros::Time time_end = ros::Time::now();
    ros::Duration duration = time_now - time_blink_red;
    //ROS_INFO("Slept for %lf secs", duration.toSec());
    //double tn = ros::Time::now().toSec();
    //ROS_INFO("time %d",tn-time_blink_bl);//tn-time_blink_bl);
    if((duration.toSec())>dur){
        //ROS_INFO("entered");
        time_blink_red=time_now;
        if(status_led_red){
            status_led_red=false;
            //alert_danger_no_sound();
            alert_collision_no_sound();
        }else{
            status_led_red=true;
            alert_turn_off_led();
        }
    }
}



void blink_change(float dur){
    ros::Time time_now = ros::Time::now();
    ros::Duration duration = time_now - time_blink_bl;
    if((duration.toSec())>dur){
        time_blink_bl=time_now;
        counter_changed++;//this counter sends how many blinks have done
        if(status_led_blue){
            status_led_blue=false;
            alert_danger_no_sound();
        }else{
            status_led_blue=true;
            alert_turn_off_led();
        }
    }
}



void check_scan(){
    ros::Time time_now = ros::Time::now();
    ros::Duration duration = time_now - last_time_scan;
    if((duration.toSec())>0.9){
        lidar_failed=true;
        pitakuru_state_msg.state_scan="lidar_fail";
        ros::Duration duration2 = time_now - time_blink_scan;
        if(duration2.toSec()>0.1){
            time_blink_scan=time_now;
            if(status_led_yellow){
                status_led_yellow=false;
                alert_collision_no_sound();
            }else{
                status_led_yellow=true;
                alert_turn_off_led();
            }
        }
    }else{

        pitakuru_state_msg.state_scan="lidar_ok";
        if(lidar_failed){
            lidar_failed=false;
            if(mode_manual){
                alert_manual_no_sound();
            }
            if(mode_follow){
                alert_karugamo_near_no_sound();
            }
            if(mode_idle){
                alert_idle_no_sound();
            }
        }
    }
}


void check_obsta(){
    ros::Time time_now = ros::Time::now();
    ros::Duration duration = time_now - last_time_obstacle;
    if((duration.toSec())>0.85){
        pitakuru_state_msg.state_karugamo="no_people_lidar_detection";
        setZeroPosLidar();
        state_pub.publish(pitakuru_state_msg);
       /*  ros::Duration duration2 = time_now - time_blink_scan;
        if(duration2.toSec()>0.2){
            time_blink_scan=time_now;
            if(status_led_yellow){
                status_led_yellow=false;
                alert_collision_no_sound();
            }else{
                status_led_yellow=true;
                alert_turn_off_led();
            }
        } */
    }/* else{
        pitakuru_state_msg.state_scan="lidar_ok";
    } */
}


void restart_follow_variables_noctrl(){
    
    cont_sp_follow=0;//experiemntal
    index_wp=-1;//init follow
    dist_auxwp=0;
    state_stop=0;
    ctrl_add_side=0;
    ctrl_side_costmap=0;
}

void restart_follow_variables(){
    //mode_people_follow();
    tracking_people=true;
    entered_first_time_far=false;
    //cont_detect_peop=0;
    //ROS_INFO("Tracked angle %f",ang_peop_lidar);
    //fprintf(fp2,"deteccion camara %f,%f,%f,%f\n",tracked_cx,tracked_cy,ang_peop_lidar,aux_dist);
    //tracked_distance=distanciaPeople2;
    tracking_people=true;
    aux_dist=5000;
    missing_track=0;
    big_angle_error_lidar_yolo=false;
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
    ctrl_add_side=0;
    is_near==true;
    stop_functions=false;
    ctrl_side_costmap=0;
}
void calc_100hz(){
    save_counter++;
    karugamo_counter++;
    if(mode_idle && karugamo_counter%100==0){
        vel_steer.linear.x=0;
        vel_steer.angular.z=0;
        speed_publisher.publish(vel_steer);
    }
    cicles=20;
    ang_peop_lidar = 90- atan2(cx, cy) * 180 / 3.1416;
    //ang_peop_lidar = -90+ atan2(cx, cy) * 180 / 3.1416 ;
    distanciaPeople2 = sqrt(cx*cx+cy*cy)*100;
    //ROS_INFO("tracked %f",ang_peop_lidar)
    //ROS_INFO("m %s",mode_follow?"TRUE":"FALSE");
    //ROS_INFO("d %s",danger?"TRUE":"FALSE");
    // ROS_INFO("tracked %f",ang_peop_lidar)
    //ROS_INFO("tracked %f,%f",tracked_cx,tracked_cy);
    //ROS_INFO("detected %f,%f,%f",cx,cy,ang_peop_lidar);
    //ROS_INFO("lidar_people_status %f,%f,%f",cx,cy,lidar_people_status);
    //experimental

    /* if(ang_peop_cam!=-500 && mode_follow && tracking_people==false  ){
        ROS_INFO("trying to match");
        //match_lidar_people();
    } */
   
    counter_blink++;
    //ROS_INFO("m %s",mode_follow?"TRUE":"FALSE");
    //ROS_INFO("d %s",danger?"TRUE":"FALSE");
    if(lidar_people_status>0 && stop_functions==true && yolo_status>0){
        restart_follow_variables();//first_tracking
        ROS_INFO("restar folow variable");
    }
    if(entered_first_time_far==true && lidar_people_status>0 ){
        entered_first_time_far=false;
        //cont_sp_follow=0;
        ROS_INFO("restart folow variable far");
    }
    if(lidar_people_status>0){
        stop_functions=false;
    }
   
    if(mode_follow && danger!=true ){ //&& lidar_people_status>0){
        ROS_INFO("just_enter l%f,y%f",lidar_people_status,yolo_status);
        ROS_INFO("just_enter al%f,ay%f",ang_peop_lidar,ang_peop_cam);
        //ROS_INFO("d %s",danger?"TRUE":"FALSE");
        ROS_INFO("stp %s",stop_functions?"TRUE":"FALSE");
        ROS_INFO("joy s%f, f%f",joy_side,joy_front);
        //ROS_INFO("tracked1 %f",ang_peop_lidar);
            //if(cx!=-0.01 && cy !=-0.01 && tracking_people && cx<=(tracked_cx+radius_follow) && cx>=(tracked_cx-radius_follow) && cy<=(tracked_cy+radius_follow) && cy >=(tracked_cy-radius_follow) && stop_functions==false){//2
            //if(tracking_people && (yolo_status>0 || lidar_people_status>0) && stop_functions==false){
            //if(tracking_people && lidar_people_status>0 && stop_functions==false && big_angle_error_lidar_yolo==false){
            //if(tracking_people && lidar_people_status>0 && stop_functions==false){
            if(lidar_people_status>0 && stop_functions==false && distanciaPeople2<near_far_distance){//if lidar status>1
                //cont_detect_peop=0;
   
                //if( (lidar_people_status>1 ||  lidar_people_status<1)&& yolo_status >0){
                started_track_yolo=false;
                pitakuru_state_msg.state="KARUGAMO";
                pitakuru_state_msg.state_karugamo="tracking_lidar";
                pitakuru_state_msg.trackeds.linear.x=distanciaPeople2;
                pitakuru_state_msg.trackeds.linear.y=ang_peop_lidar;
                pitakuru_state_msg.trackeds.linear.z=lidar_people_status;
                pitakuru_state_msg.trackeds.angular.x=dist_peop_cam;
                pitakuru_state_msg.trackeds.angular.y=ang_peop_cam;
                pitakuru_state_msg.trackeds.angular.z=yolo_status;
                state_pub.publish(pitakuru_state_msg);
                nav_msgs::Odometry odomr;
                    odomr.header.stamp = ros::Time::now();
                    odomr.header.frame_id="base_link";
                    odomr.pose.pose.position.x=cx;
                    odomr.pose.pose.position.y=cy;
                    odomr.pose.pose.position.z=0.0;
                    odomr.pose.pose.orientation.w=1.0;
                    pos_peop_pub.publish(odomr);
                //if(dist_peop_cam>250 && distanciaPeople2<150 && yolo_status >0 || lidar_people_status<1){
                //        alert_collision_no_sound();
                //        ang_peop_lidar = ang_peop_cam ;// ;  -90+ atan2(cx, cy) * 180 / 3.1416
                //        distanciaPeople2 = dist_peop_cam;
                //}else if(lidar_people_status>0 ){
                        ang_peop_lidar = 90- atan2(cx,cy) * 180 / 3.1416 ;// ;  -90+ atan2(cx, cy) * 180 / 3.1416
                        distanciaPeople2 = sqrt(cx*cx+cy*cy)*100;
                //}
                //if(ang_peop_lidar-tracked_angle>30){}
                tracked_angle= ang_peop_lidar;
                last_time_tracking = ros::Time::now();
               
                //ROS_INFO("tracked %f, %f ",tracked_angle,distanciaPeople2);
                tracked_distance = distanciaPeople2;
                last_time_tracking = ros::Time::now();
                if(distanciaPeople2<near_far_distance){//near
                    near();
                    //ROS_INFO("near()");
                    if(lidar_failed==false && changed_setting==false && low_voltage ==false){
                        alert_karugamo_near_no_sound();
                    }
                    if(is_near==false){
                        fprintf(fp2,"Entre near \n");
                        is_near=true;
                        stop_functions=false;
                        if(lidar_failed==false && changed_setting==false && low_voltage ==false){
                            alert_karugamo_near_no_sound();
                        }
                        dist_auxwp=0;
                        //cont_sp_follow=0;//experimental
                    }
                }
                // else{//far
                //     if(lidar_failed==false && changed_setting==false && low_voltage ==false && stop_follow==false){
                //     alert_karugamo_far_no_sound();
                   
                //     }
                //     if(is_near==true){
                //         is_near=false;
                //         if(lidar_failed==false && changed_setting==false && low_voltage ==false && stop_follow==false){
                //         alert_karugamo_far_no_sound();
                //         //alert_karugamo_far_sound();
                //         //alert_warning_sound();
                //         alert_karugamo_waypoint_sound();
                //         ros::Duration(0.02).sleep(); // sleep for 0.05 seconds
                //         }
                //         stop_functions=false;
                //         if(cont_sp_follow>2){
                //             fprintf(fp2,"Entre far num sp follow %i e index %i  \n",cont_sp_follow,cont_sp_follow-3);
                //             index_wp=cont_sp_follow-3;
                //         }
                //     }
                //     far();
                //     ROS_INFO("far() in range");
                // }//endif not near
                //ROS_INFO("hello1");
                missing_track=0;
                tracked_cx=cx;
                tracked_cy=cy;
                tracked_pos.x=cx;
                tracked_pos.y=cy;
                tracked_pos.z=tracked_angle;
                tracked_publisher.publish(tracked_pos);
                //ROS_INFO("hello2");
                geometry_msgs::Twist vel_steer;    
                /////////////////////////new implement
                float dobs,angobs,npcx,npcy;
                dobs=sqrt(tracked_cx*tracked_cx+tracked_cy*tracked_cy);
                //angobs=atan2(-tracked_cy,-tracked_cx)*180/3.1416;
                //angobs=atan2(tracked_cx,tracked_cy)*180/3.1416;
                angobs  = 90- atan2(cx, cy) * 180 / 3.1416 ;// ;  -90+ atan2(cx, cy) * 180 / 3.1416
                //angobs = -90+ atan2(cx, cy) * 180 / 3.1416 ;
                //px,py, ang_robot position robot
                npcx=px + dobs*(cos((angobs+ang_robot)*3.1416/180));//#rcx+ocx*(cos((angobs+angr)*3.1416/180))
                npcy=py + dobs*(sin((angobs+ang_robot)*3.1416/180));//#rcy+ocy*(sin((angobs+angr)*3.1416/180))
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
                   
                    //ROS_INFO("added %f,%f,%f,%f,%f,%f",npcx,npcy,px,py,angobs,ang_robot);
                    //fprintf(fp2,"%f,%f,%f,%f,%f,%f,%i\n",npcx,npcy,px,py,angobs,ang_robot,cont_sp_follow);
                    fprintf(fp2,"a%f,%f,%f,%f,%f,%f,%i\n",npcx,npcy,px,py,angobs,ang_robot,cont_sp_follow);
                }
               
                //ROS_INFO("tracked");
                   
            }//end it s in range
            // else if(danger==false  && cont_sp_follow>2 ){
            //     if(is_near==true || entered_first_time_far==false){
            //             entered_first_time_far=true;
            //             is_near=false;
            //             ROS_INFO("Entre far num sp follow %i e index %i  \n",cont_sp_follow,cont_sp_follow-3);
            //             index_wp=cont_sp_follow-3;
            //             if(changed_setting==false && low_voltage ==false && stop_follow==false){
            //                 //alert_karugamo_far_no_sound();
            //                 alert_karugamo_waypoint_sound();
            //                 ros::Duration(0.02).sleep(); // sleep for 0.05 seconds
            //                 //alert_karugamo_far_sound();
            //             }
            //             stop_functions=false;
                        
            //     }
                
            //      far();
            //      ROS_INFO("far() not in range");
            // }
            else if(danger==false  && (lidar_people_status<0 || (lidar_people_status<0 && distanciaPeople2>=near_far_distance))&& stop_functions==false){//lostedlidar
                //if(is_near==false){
                missing_track+=1;
                ROS_INFO("miss %i",missing_track);
                
               
                //if(cont_sp_follow>2){
                //    far();
                //}else{
                    //ROS_INFO("blinking");
                    //blink_blue(counter_blink,20);
                    if(lidar_failed==false && low_voltage==false){
                        blink_blue2(0.25);
                    }
                    if(missing_track>2){
                    pitakuru_state_msg.state="KARUGAMO";
                    pitakuru_state_msg.state_karugamo="losting_with_lidar";
                    pitakuru_state_msg.trackeds.linear.x=distanciaPeople2;
                    pitakuru_state_msg.trackeds.linear.y=ang_peop_lidar;
                    pitakuru_state_msg.trackeds.linear.z=lidar_people_status;
                    pitakuru_state_msg.trackeds.angular.x=dist_peop_cam;
                    pitakuru_state_msg.trackeds.angular.y=ang_peop_cam;
                    pitakuru_state_msg.trackeds.angular.z=yolo_status;
                    state_pub.publish(pitakuru_state_msg);
                    }
                    ros::Time time_now = ros::Time::now();
                    ros::Duration duration = time_now - last_time_tracking;
                    if(duration.toSec()>duration_to_lost){
                        last_time_tracking= ros::Time::now();
                        pitakuru_state_msg.state="KARUGAMO";
                        pitakuru_state_msg.state_karugamo="lost";
                        //state_pub.publish(pitakuru_state_msg);
                        if(stop_functions==false){
                            alert_lost_voice_sound();
                        }
                        //if(missing_track>count_to_miss){//thiscounter also can help to see if theres a lot of objects and its not able to follow
                        //if(lidar_people_status<1){
                        if(is_near==true && tracking_people && stop_functions==false){
                            fprintf(fp2,"lost and near");
                            //ctrl_front_follow=speed_wp_lost;//experiemntal 10
                            //ctrl_front_follow=0;
                            ctrl_yaw=0;
                            //ctrl_yaw=(1-smooth_accel_karugamo_far)*(0)+(smooth_accel_karugamo_far*ctrl_yaw);
                            vel_steer.linear.x= ctrl_front_follow;
                            vel_steer.angular.z= ctrl_yaw;
                            vel_steer.linear.x=(vel_steer.linear.x/21)*0.1045;
                            vel_steer.angular.z=(vel_steer.angular.z/21)*0.1045;
                            speed_publisher.publish(vel_steer);
                            //alert_danger_no_sound();
                            //alert_collision_no_sound();
                            stop_functions=true;
                           
                            //is_near=false;
                            //alerts_command.data=3;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
                            //alerts_publisher.publish(alerts_command);
                            //if(cont_sp_follow>2){
                            //  fprintf(fp2,"Entre far por lost num sp follow %i e index %i  \n",cont_sp_follow,cont_sp_follow-3);
                            //  index_wp=cont_sp_follow-3;
                            //}
                            
                        }
                        stop_functions=true;
                        tracking_lidar=false;
                        tracking_yolo=false;
                        ROS_INFO("LOST");
                        
                        fprintf(fp2,"lost \n");
                        tracking_people=false;
                        missing_track=0;
                        tracked_cx=0;
                        tracked_cy=0;
                        aux_dist=5000;
                        ctrl_side_costmap=0;
                        ///tracked_pos.x=-50;
                        //tracked_pos.y=-50;
                        //tracked_publisher.publish(tracked_pos);
                        publish_lost_tracked();
                        missing_track=0;
                        cont_detect_peop=0;
                        sound_counter++;
                        if(sound_counter%6==0){
                            alert_search_voice_sound();
                            //alert_warning_sound();
                        }
                    }
                //}
            }//losted
           
        if(stop_functions==true&& tracking_people==false){
                //ROS_INFO("blinking");
                //blink_blue(counter_blink,20);
                if(lidar_failed==false && low_voltage==false){
                    blink_blue2(0.25);
                }
                    
                
                pitakuru_state_msg.state="KARUGAMO";
                pitakuru_state_msg.state_karugamo="losting_with_lidar";
                pitakuru_state_msg.trackeds.linear.x=distanciaPeople2;
                pitakuru_state_msg.trackeds.linear.y=ang_peop_lidar;
                pitakuru_state_msg.trackeds.linear.z=lidar_people_status;
                pitakuru_state_msg.trackeds.angular.x=dist_peop_cam;
                pitakuru_state_msg.trackeds.angular.y=ang_peop_cam;
                pitakuru_state_msg.trackeds.angular.z=yolo_status;
                state_pub.publish(pitakuru_state_msg);

                ros::Time time_now = ros::Time::now();
                ros::Duration duration = time_now - last_time_tracking;
                if(duration.toSec()>duration_to_lost){
                    last_time_tracking= ros::Time::now();
                    pitakuru_state_msg.state="KARUGAMO";
                    pitakuru_state_msg.state_karugamo="lost";
                    //state_pub.publish(pitakuru_state_msg);

                    //if(missing_track>count_to_miss){//thiscounter also can help to see if theres a lot of objects and its not able to follow
                    //if(lidar_people_status<1){
                    if(is_near==true && tracking_people && stop_functions==false){
                        fprintf(fp2,"lost and near2");
                        //ctrl_front_follow=speed_wp_lost;//experiemntal 10
                        //ctrl_front_follow=0;
                        ctrl_yaw=0;
                        //ctrl_yaw=(1-smooth_accel_karugamo_far)*(0)+(smooth_accel_karugamo_far*ctrl_yaw);
                        vel_steer.linear.x= ctrl_front_follow;
                        vel_steer.angular.z= ctrl_yaw;
                        vel_steer.linear.x=(vel_steer.linear.x/21)*0.1045;
                        vel_steer.angular.z=(vel_steer.angular.z/21)*0.1045;
                        speed_publisher.publish(vel_steer);
                        //alert_danger_no_sound();
                        //alert_collision_no_sound();
                        stop_functions=true;
                       
                        //is_near=false;
                        //alerts_command.data=3;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
                        //alerts_publisher.publish(alerts_command);
                        //if(cont_sp_follow>2){
                        //  fprintf(fp2,"Entre far por lost num sp follow %i e index %i  \n",cont_sp_follow,cont_sp_follow-3);
                        //  index_wp=cont_sp_follow-3;
                        //}
                    }
                    stop_functions=true;
                    tracking_lidar=false;
                    tracking_yolo=false;
                    ROS_INFO("LOST2");
                    fprintf(fp2,"lost2 \n");
                    tracking_people=false;
                    missing_track=0;
                    tracked_cx=0;
                    tracked_cy=0;
                    aux_dist=5000;
                    ctrl_side_costmap=0;
                    ///tracked_pos.x=-50;
                    //tracked_pos.y=-50;
                    //tracked_publisher.publish(tracked_pos);
                    publish_lost_tracked();
                    missing_track=0;
                    cont_detect_peop=0;
                    sound_counter++;
                    if(sound_counter%6==0){
                        //alert_warning_sound();
                        //alert_lost_voice_sound();
                        alert_search_voice_sound();

                    }
                }
                   
                       
                //ctrl_front_follow=0;
                //alert_collision_no_sound();
                if(danger){
                        ctrl_front_follow=0;
                    ctrl_yaw=0;
                    vel_steer.linear.x= ctrl_front_follow;
                    vel_steer.angular.z= ctrl_yaw;
                    vel_steer.linear.x=(vel_steer.linear.x/21)*0.1045;
                    vel_steer.angular.z=(vel_steer.angular.z/21)*0.1045;
                    speed_publisher.publish(vel_steer);
                }else{
                    ctrl_front_follow=(1-smooth_accel_stop)*(0)+(smooth_accel_stop*ctrl_front_follow);
                    ctrl_yaw=0;
                    vel_steer.linear.x= ctrl_front_follow;
                    vel_steer.angular.z= ctrl_yaw;
                    vel_steer.linear.x=(vel_steer.linear.x/21)*0.1045;
                    vel_steer.angular.z=(vel_steer.angular.z/21)*0.1045;
                    speed_publisher.publish(vel_steer);
                    tracked_pos.x=-50;
                    tracked_pos.y=-50;
                    //tracked_publisher.publish(tracked_pos);
                }
               
        }
        //changed from here
        //ROS_INFO("nada");
       
    }//end mode follow
}


void far(){
     pitakuru_state_msg.state="KARUGAMO";
                        pitakuru_state_msg.state_karugamo="far";
                        pitakuru_state_msg.trackeds.linear.x=distanciaPeople2;
                        pitakuru_state_msg.trackeds.linear.y=ang_peop_lidar;
                        pitakuru_state_msg.trackeds.linear.z=lidar_people_status;
                        pitakuru_state_msg.trackeds.angular.x=dist_peop_cam;
                        pitakuru_state_msg.trackeds.angular.y=ang_peop_cam;
                        pitakuru_state_msg.trackeds.angular.z=yolo_status;
                        state_pub.publish(pitakuru_state_msg);
    if(lidar_failed==false && danger==false && changed_setting==false && low_voltage ==false && stop_follow==false){
        alert_karugamo_far_no_sound();
    }
    if(save_counter%290==0 && stop_follow==false ){
                //alert_lost_voice_sound();
                alert_karugamo_waypoint_sound();
    }else if(save_counter%290==0 && stop_follow==true ){
                //alert_lost_voice_sound();
                alert_lost_voice_sound();
    }
    if(is_near==false && stop_functions==false){
            if(save_counter%20==0){
                fprintf(fp2,"wp %f,%f,%f,%f,%f,%f,%f,%i\n",spx_saved[index_wp],spy_saved[index_wp],px,py,ctrl_front_follow,ctrl_yaw,ang_robot,index_wp);
                //alert_warning_sound();
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
                            restart_follow_variables_noctrl();
                            alert_lost_voice_sound();
                            ros::Duration(0.05).sleep(); // sleep for half a second
                            alert_lost_voice_sound();
                            ros::Duration(0.05).sleep(); // sleep for half a second
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
                        if(sqrt((errpx*errpx)+(errpy*errpy))<0.33){
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

                        spVel=0.1*(error_yaw);//0.0r5*(error_yaw);
                        nkp=angle_gain_wp;//=0.0085;
                        ctrl_yaw=(nkp*spVel)-ctrl_yaw/2;//experimental
                        //experiemntal
                        ctrl_add_side=(1-smooth_accel_side_manual)*(joy_side*max_speed_side_manual)+(smooth_accel_side_manual*ctrl_add_side);
                        ctrl_add_side=0;
                        //ctrl_side_costmap=(1-smooth_accel_side_manual)*(cost_obst*max_speed_side_manual)+(smooth_accel_side_manual*ctrl_side_costmap);
                        //ROS_INFO("cost%f",ctrl_side_costmap);
                        ctrl_yaw=ctrl_yaw+ctrl_add_side;//+//ctrl_side_costmap*gain_to_costmap;
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
                        //experiemntal
                        ctrl_add_front=(1-smooth_accel_manual)*(joy_front*max_speed_manual)+(smooth_accel_manual*ctrl_front_manual);
                            ctrl_front_follow=ctrl_front_follow+ctrl_add_front;
                       
                       
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
                        //experimental
                        ctrl_add_front=(1-smooth_accel_manual)*(joy_front*max_speed_manual)+(smooth_accel_manual*ctrl_front_manual);
                            ctrl_front_follow=ctrl_front_follow+ctrl_add_front;
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
                        //  if(counter_search%350==0){
                        //     counter_search=0;
                        //     state_stop++;
                        //     switch(state_stop){
                        //         /*
                        //         case 1:
                                   
                        //             sp_yaw=ang_robot;
                        //             saved_ang=ang_robot;
                        //             fprintf(fp2,"entre caso 1 ang %f \n",saved_ang);
                        //         break;
                        //         */
                        //         case 1:
                                   
                        //             sp_yaw=saved_ang;
                        //             fprintf(fp2,"entre caso 1 ang %f \n",saved_ang);
                        //         break;
                               
                        //         case 2:
                                   
                        //             sp_yaw=saved_ang+45;
                        //             if (sp_yaw < -180.0 ){
                        //                 sp_yaw=sp_yaw+360;
                        //             }else if (sp_yaw > 180.0 ){
                        //                 sp_yaw=sp_yaw-360;
                        //             }
                        //             fprintf(fp2,"entre caso 2 ang %f \n",sp_yaw);
                        //         break;
                        //         case 3:
                        //             sp_yaw=saved_ang;
                        //             fprintf(fp2,"entre caso 3 ang %f \n",sp_yaw);
                        //         break;
                        //         case 4:
                        //             state_stop=0;
                        //             sp_yaw=saved_ang-45;
                        //             if (sp_yaw < -180.0 ){
                        //                 sp_yaw=sp_yaw+360;
                        //             }else if (sp_yaw > 180.0 ){
                        //                 sp_yaw=sp_yaw-360;
                        //             }
                        //             fprintf(fp2,"entre caso 4 ang %f \n",sp_yaw);
                        //         break;
                        //         //case 5:
                        //         //    sp_yaw=saved_ang;
                        //         //    state_stop=0;
                        //         //  fprintf(fp2,"entre caso 5 ang %f \n",sp_yaw);
                        //     // break;  
                        //     }
                        // } 
                        // error_yaw=(sp_yaw-ang_robot);//-(sp_yaw-ang_robot);
                        // if (error_yaw < -180.0 ){
                        //     error_yaw=error_yaw+360;
                        // }else if (error_yaw > 180.0 ){
                        //     error_yaw=error_yaw-360;
                        // }
                        // spVel=0.1*(error_yaw);//0.05*(error_yaw);
                        // nkp=angle_gain_wp;//=0.0085;
                        // ctrl_yaw=(nkp*spVel)-ctrl_yaw/2;//
                        // if(ctrl_yaw>300){
                        //     ctrl_yaw=300;
                        // }else if(ctrl_yaw<-300){
                        //     ctrl_yaw=-300;
                        // }
                        //ctrl_front_follow=0;
                        ctrl_front_follow=(1-smooth_accel_stop)*(0)+(smooth_accel_stop*ctrl_front_follow);//experimental
                        ctrl_yaw=0;
                        vel_steer.linear.x= ctrl_front_follow;
                        vel_steer.angular.z= ctrl_yaw;
                        
                        if(low_voltage ==false  && changed_setting==false && lidar_failed==false){
                            blink_blue2(0.25);
                        }
                        if(ctrl_front_follow<400){
                            restart_follow_variables();
                        }
                        //alert_collision_no_sound();
                        //blink_blue(counter_blink,15);
                        //blink_bl=true;
                        //fprintf(fp2,"calc sp %f, ctrl %f \n",sp_yaw,ctrl_yaw);
                }
                    vel_steer.linear.x=(vel_steer.linear.x/21)*0.1045;
                    vel_steer.angular.z=(vel_steer.angular.z/21)*0.1045;
                    if(karugamo_counter%2==0){
                        speed_publisher.publish(vel_steer);
                    }
                   
        }//end_isnear=false
}

void angPeopCallback4(const geometry_msgs::Vector3& msg){
    cx = msg.x;//pos people or object
    cy = msg.y;//pos people or object
    lidar_people_status=msg.z;
    last_time_obstacle = ros::Time::now();
    //calc_100hz();
}//end function

void setZeroPosLidar(){
    cx = -50;//pos people or object
    cy = -50;//pos people or object
    lidar_people_status=-1;
}

void publish_lost_tracked(){
    tracked_pos.x=-50;
    tracked_pos.y=-50;
    tracked_pos.z=0;
    tracked_publisher.publish(tracked_pos);
}
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
       
       if(mode_follow && danger!=true && stop_functions==false){ //&& tracking_people){//1
           
            if(save_counter%12==0){
                fprintf(fp2,"near %f,%f,%f,%f,%i\n",px,py,0.0,ang_robot,index_wp);
            }
           
            if (1==1){
                //correccion needed
                //ang_peop_lidar = -90+ atan2(cx, cy) * 180 / 3.1416 ;// ;  90- atan2(cx, cy) * 180 / 3.1416
                //ang_peop_lidar = 90- atan2(cx,cy) * 180 / 3.1416 ;// ;  -90+ atan2(cx, cy) * 180 / 3.1416
                //distanciaPeople2 = sqrt(cx*cx+cy*cy)*100;
                //ROS_INFO("T%f,%f",tracked_cx,tracked_cy);
                //f((abs(ang_peop_cam-ang_peop_lidar)>29 || lidar_people_status>1) && yolo_status == 1){
                //if( lidar_people_status>1 && yolo_status >0){
                //    alert_collision_no_sound();
                //    ang_peop_lidar = ang_peop_cam ;// ;  -90+ atan2(cx, cy) * 180 / 3.1416
                //    distanciaPeople2 = dist_peop_cam;
                //}else{
                    ang_peop_lidar = 90- atan2(cx,cy) * 180 / 3.1416 ;// ;  -90+ atan2(cx, cy) * 180 / 3.1416
                    distanciaPeople2 = sqrt(cx*cx+cy*cy)*100;
                //}
               // ROS_INFO("near() an%f d%f",ang_peop_lidar,distanciaPeople2);
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

               
                //if(abs(ang_peop_cam-ang_peop_lidar)>19 && yolo_status == 1){
                //    alert_collision_no_sound();
                 //   ctrl_ang= low_vel_gain_follow*ang_peop_cam-ctrl_ang/2;
                //}else{
                    ctrl_ang= low_vel_gain_follow*ang_peop_lidar-ctrl_ang/2;
                //}
                //experiementa
                ctrl_add_side=(1-smooth_accel_side_manual)*(joy_side*max_speed_side_manual)+(smooth_accel_side_manual*ctrl_add_side);
                //ctrl_add_side=0;
                if((vel_m1 >= vel_detect_costmap || vel_m2 >= vel_detect_costmap )){//&&distanciaPeople2>dist_robot_people){
                    ctrl_side_costmap=(1-smooth_accel_side_manual)*(cost_obst*max_speed_side_manual)+(smooth_accel_side_manual*ctrl_side_costmap);
                }else{
                    ctrl_side_costmap=0;
                }
                //ctrl_side_costmap=0;
                //ROS_INFO("cost%f",ctrl_side_costmap);
                ctrl_ang=ctrl_ang+ctrl_add_side+ctrl_side_costmap*gain_to_costmap;
                //ctrl_ang=ctrl_ang+ctrl_side_costmap*gain_to_costmap;
                //ROS_INFO("ctrl ang() an%f s %f ,d%f",ctrl_ang,ctrl_add_side,ctrl_side_costmap);
                //
                float restriction=400;
                if (ctrl_ang>restriction){
                    ctrl_ang= restriction;
                }else if (ctrl_ang<-restriction){
                    ctrl_ang= -restriction;
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
                    if (heavy){
                        ctrl_front_follow=(1-smooth_accel_karugamo_near)*(frontal_gain_follow*norm_dist/*max_speed_follow*/)+(smooth_accel_karugamo_near*ctrl_front_follow);
                        //experimental
                        ctrl_add_front=(1-smooth_accel_manual)*(joy_front*max_speed_manual)+(smooth_accel_manual*ctrl_front_manual);
                        //ctrl_front_follow=ctrl_front_follow+ctrl_add_front-abs(ctrl_side_costmap*gain_to_costmap*0.1);
                        if(ctrl_front_follow>1000){
                            ctrl_front_follow=ctrl_front_follow+ctrl_add_front-abs(ctrl_side_costmap*gain_to_costmap*0.1);
                        }else{
                            ctrl_front_follow=ctrl_front_follow+ctrl_add_front;
                        }
                        // float nueva=abs(ctrl_side_costmap*gain_to_costmap*4);
                        // ROS_INFO("cost %f",nueva);
                        if(ctrl_front_follow<0){
                            ctrl_front_follow=0;
                            vel_steer.linear.x=0;
                        }
                        if (ctrl_front_follow>max_speed_follow){
                            ctrl_front_follow= max_speed_follow;
                        }
                    }else{
                        ctrl_front_follow=(1-smooth_accel_karugamo_near)*(max_speed_manual *norm_dist/*max_speed_follow*/)+(smooth_accel_karugamo_near*ctrl_front_follow);
                        //experimental
                        ctrl_add_front=(1-smooth_accel_manual)*(joy_front*max_speed_manual)+(smooth_accel_manual*ctrl_front_manual);
                        
                        //ctrl_front_follow=ctrl_front_follow+ctrl_add_front-abs(ctrl_side_costmap*gain_to_costmap*0.1);
                        if(ctrl_front_follow>1000){
                            ctrl_front_follow=ctrl_front_follow+ctrl_add_front-abs(ctrl_side_costmap*gain_to_costmap*0.1);
                        }else{
                            ctrl_front_follow=ctrl_front_follow+ctrl_add_front;
                        }
                        // float nueva=abs(ctrl_side_costmap*gain_to_costmap*0.8);
                        // ROS_INFO("cost %f",nueva);
                        if(ctrl_front_follow<0 ){
                            ctrl_front_follow=0;
                            vel_steer.linear.x=0;
                        }
                        if (ctrl_front_follow>max_speed_manual){
                            ctrl_front_follow= max_speed_manual;
                        }
                    }
                    
                    vel_steer.linear.x= ctrl_front_follow;
                }else{
                    ctrl_front_follow=(1-smooth_accel_stop)*(0)+(smooth_accel_stop*ctrl_front_follow);
                    vel_steer.linear.x=0;
                    ctrl_side_costmap=0;
                    //ctrl_front_follow=0;
                }
                //ROS_INFO("ctrl frnt()n%f ",ctrl_front_follow);
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
                if(karugamo_counter%2==0){
                    speed_publisher.publish(vel_steer);
                }
            }

        }//mode3
       
    }  



///////////////////

///
void follow_yolo(){    
    if(mode_follow && danger!=true && stop_functions==false){ //&& tracking_people){//1
       
        if(save_counter%12==0){
            fprintf(fp2,"near %f,%f,%f,%f,%i\n",px,py,0.0,ang_robot,index_wp);
        }
       
        if (1==1){

                ang_peop_lidar = ang_peop_cam;// ;  -90+ atan2(cx, cy) * 180 / 3.1416
                distanciaPeople2 = dist_peop_cam;
            //}

            tracked_angle= ang_peop_cam;
            tracked_distance = ang_peop_cam;
     
            ctrl_ang= low_vel_gain_follow*ang_peop_lidar-ctrl_ang/2;
            //}
            //experiementa
            ctrl_add_side=(1-smooth_accel_side_manual)*(joy_side*max_speed_side_manual)+(smooth_accel_side_manual*ctrl_side_manual);
           
            if(vel_m1 >= vel_detect_costmap || vel_m2 >= vel_detect_costmap){
                ctrl_side_costmap=(1-smooth_accel_side_manual)*(cost_obst*max_speed_side_manual)+(smooth_accel_side_manual*ctrl_side_costmap);
            }else{
                ctrl_side_costmap=0;
            }
            //ROS_INFO("cost%f",ctrl_side_costmap);
            ctrl_ang=ctrl_ang+ctrl_add_side+ctrl_side_costmap*gain_to_costmap;
            //
            float restriction=450;
            if (ctrl_ang>restriction){
                ctrl_ang= restriction;
            }else if (ctrl_ang<-restriction){
                ctrl_ang= -restriction;
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
                if (heavy){
                    ctrl_front_follow=(1-smooth_accel_karugamo_near)*(frontal_gain_follow*norm_dist/*max_speed_follow*/)+(smooth_accel_karugamo_near*ctrl_front_follow);
                    //experimental
                    ctrl_add_front=(1-smooth_accel_manual)*(joy_front*max_speed_manual)+(smooth_accel_manual*ctrl_front_manual);
                    ctrl_front_follow=ctrl_front_follow+ctrl_add_front;
                    if(ctrl_front_follow<0){
                        ctrl_front_follow=0;
                        vel_steer.linear.x=0;
                    }
                    if (ctrl_front_follow>max_speed_follow){
                        ctrl_front_follow= max_speed_follow;
                    }
                }else{
                    ctrl_front_follow=(1-smooth_accel_karugamo_near)*(max_speed_manual *norm_dist/*max_speed_follow*/)+(smooth_accel_karugamo_near*ctrl_front_follow);
                    //experimental
                    ctrl_add_front=(1-smooth_accel_manual)*(joy_front*max_speed_manual)+(smooth_accel_manual*ctrl_front_manual);
                    ctrl_front_follow=ctrl_front_follow+ctrl_add_front;
                    if(ctrl_front_follow<0 ){
                        ctrl_front_follow=0;
                        vel_steer.linear.x=0;
                    }
                    if (ctrl_front_follow>max_speed_manual){
                        ctrl_front_follow= max_speed_manual;
                    }
                }
                vel_steer.linear.x= ctrl_front_follow;
            }else{
                ctrl_front_follow=(1-smooth_accel_stop)*(0)+(smooth_accel_stop*ctrl_front_follow);
                vel_steer.linear.x=0;
                ctrl_side_costmap=0;
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
            if(karugamo_counter%4==0){
                speed_publisher.publish(vel_steer);
            }
        }

    }//mode3
       
}  
////

void scanCallback(const sensor_msgs::LaserScan::ConstPtr& scan){
    //if(!collision || vel_m1 >= 0.0 || vel_m2 >=  0.0){
        // for(int j=0;j<=720;j++){
        //     if( scan->ranges[j]  <= break_front_distance && scan->ranges[j] >0.14 ){
        //           ROS_INFO("less thnan break in %i ,at %f ,vel %f , man %f , fol %f",j ,scan->ranges[j],vel_steer.linear.x,ctrl_front_manual,ctrl_front_follow);  
        //     }
        // }  
    last_time_scan=ros::Time::now();
    counter_blink++;
    if(danger && collision == false ){
        danger_counter++;
        alert_danger_no_sound();
        if(danger_counter%100==0){
            //alert_danger_sound();
            alert_danger_voice_sound();
            ros::Duration(0.02).sleep(); // sleep for 0.05 seconds
            pitakuru_state_msg.state="DANGER";
                pitakuru_state_msg.state_karugamo="losting_with_lidar";
               
                state_pub.publish(pitakuru_state_msg);
        }
    }
    if(danger == false && collision == false ){
        //int count = scan->scan_time / scan->time_increment;
        //float  break_distance=1.5;
            //float  break_danger=0.5;
         
        //if(detect_cont>1 && mode_idle == false && (vel_m1 >= vel_detect_scan || vel_m2 >= vel_detect_scan)){
        if(detect_cont>1 && mode_idle == false && (ctrl_front_manual> 600 || ctrl_front_follow > 600)){
        //if(detect_cont>0 ){
                danger=true;
                free_way=false;
                ROS_INFO("Danger1");
                //alert_danger_voice_sound();
                detect_cont=0;
                ctrl_front_manual=0;
                    ctrl_side_manual=0;
                    vel_steer.linear.x= 0;
                    vel_steer.angular.z= 0;
                    speed_publisher.publish(vel_steer);
                ros::Duration(0.05).sleep(); // sleep for 0.05 seconds
                alert_danger_voice_sound();
                ros::Duration(0.02).sleep(); // sleep for 0.05 seconds
                /*
                danger_counter++;
                alert_danger_no_sound();
                if(danger_counter%65==0){
                    alert_danger_sound();
                }
                */
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
                ros::Duration(0.1).sleep(); // sleep for half a second
        } else{
            free_way=true;
            //detect_cont=0
        }
        //int min=200;
        //ROS_INFO("no500 %f",scan->ranges[500]);
        //ROS_INFO("no500 %f",scan->ranges[279]);  
         /* for(int j=0;j<=720;j++){
            if( scan->ranges[j]  <= break_danger && scan->ranges[j] >0.14 ){
                  ROS_INFO("less thnan break in %i",j);  
            }
        }  */
       
        if( ctrl_front_manual> 600 || ctrl_front_follow > 600){
            for(int j=0;j<=720;j++){

                if(j>280&&j<440){
                    if (scan->ranges[j] <= break_front_distance && scan->ranges[j] >0.14 ){

                        detect_cont++;
                        ROS_INFO("found in %i",j);
                        pitakuru_state_msg.state_danger="detected_break_danger1";
                       
                        //ROS_INFO("print after");
                    }
                    if(detect_cont>1){  
                        return;
                    }
                }else{
                    if (scan->ranges[j] <= break_danger && scan->ranges[j] >0.14 ){
                        detect_cont++;
                        ROS_INFO("close in %i",j);
                        pitakuru_state_msg.state_danger="detected_break_danger1";
                       
                        //return;
                        //ROS_INFO("print after");
                    }
                    if(detect_cont>1){  
                        return;
                    }

                }
            }
            detect_cont=0;//si llego hast aca no encontro nada
            //free_way=true;
        }
       


/////////
    }
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
void  alert_turn_off_led(){
    alerts_command.data=100;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
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

void  alert_speed1_sound(){
    alerts_command.data=101;// 
    alerts_publisher.publish(alerts_command);
}
void  alert_speed2_sound(){
    alerts_command.data=102;// 
    alerts_publisher.publish(alerts_command);
}
void  alert_speed3_sound(){
    alerts_command.data=103;// 
    alerts_publisher.publish(alerts_command);
}
void  alert_speed4_sound(){
    alerts_command.data=104;// 
    alerts_publisher.publish(alerts_command);
}
void  alert_speed5_sound(){
    alerts_command.data=105;// 
    alerts_publisher.publish(alerts_command);
}


void  alert_karugamo_waypoint_sound(){
    alerts_command.data=106;// 
    alerts_publisher.publish(alerts_command);
}
void  alert_low_battery_sound(){
    alerts_command.data=108;// 
    alerts_publisher.publish(alerts_command);
}

void  alert_danger_voice_sound(){
    alerts_command.data=107;// 
    alerts_publisher.publish(alerts_command);
}
void  alert_lost_voice_sound(){
    alerts_command.data=109;// 
    alerts_publisher.publish(alerts_command);
}
void  alert_search_voice_sound(){
    alerts_command.data=110;// 
    alerts_publisher.publish(alerts_command);
}


//////// alerts

void collisioned(){
    low_voltage=false;
    collision =true;
    vel_steer.linear.x= 0;
    vel_steer.linear.y=0;//disable motors
    vel_steer.angular.z= 0;
    speed_publisher.publish(vel_steer);
    vel_steer.linear.x= 0;
    vel_steer.linear.y=-1;//disable motors
    vel_steer.angular.z= 0;
    speed_publisher.publish(vel_steer);
    vel_steer.linear.x= 0;
    vel_steer.linear.y=-1;//disable motors
    vel_steer.angular.z= 0;
    speed_publisher.publish(vel_steer);
    alert_collision_sound();
    danger=true;
    mode_idle=false;
    mode_manual=false;
    mode_karugamo=false;
    mode_follow=false;
    free_way=false;
    tracking_people=false;
    cont_detect_peop=0;
    ctrl_front_follow= 0;
    ctrl_ang= 0;
    ctrl_front_manual= 0;
    ctrl_side_manual= 0;
    aux_dist=5000;
    stop_functions=false;
    vel_steer.linear.x= 0;
    vel_steer.linear.y=-1;//disable motors
    vel_steer.angular.z= 0;
    speed_publisher.publish(vel_steer);
    publish_lost_tracked();
    pitakuru_state_msg.state="COLLISION";
    state_pub.publish(pitakuru_state_msg);
}

void remove_collision(){
    low_voltage=false;
    collision = false;
    mode_idle=true;
    mode_manual=false;
    mode_karugamo=false;
    mode_follow=false;
    danger=false;
    free_way=true;
    tracking_people=false;
    cont_detect_peop=0;
    ctrl_front_follow= 0;
    ctrl_ang= 0;
    ctrl_front_manual= 0;
    ctrl_side_manual= 0;
    stop_functions=false;
    alert_idle_sound();
    vel_steer.linear.x= 0;
    vel_steer.linear.y=0;//disable motors
    vel_steer.angular.z= 0;
    vel_steer.linear.x= 0;
    vel_steer.linear.y=-1;//enable motors
    vel_steer.angular.z= 0;
    speed_publisher.publish(vel_steer);
    tracked_angle=0;
    ang_peop_lidar=0;
    aux_dist=5000;
    distanciaPeople2=0;
    tracked_distance=0;
    publish_lost_tracked();
    pitakuru_state_msg.state="IDLE";
    state_pub.publish(pitakuru_state_msg);
}


void mode_MANUAL(){
    n_flag_l=false;
    d_flag_l=true;
    n_flag_r=false;
    d_flag_r=true;
    low_voltage=false;
    mode_idle=false;
    mode_karugamo=false;
    mode_manual=true;
    mode_follow=false;
    tracking_people=false;
    cont_detect_peop=0;
    start_route = false;
    mode_auto=false;
    danger=false;
    free_way=true;
    stop_functions=false;
    ROS_INFO("Mode Manual");
    alerts_command.data=1;// 5 danger 4 warning 3 karugamo 2 idle 1 manual
    alerts_publisher.publish(alerts_command);
    ctrl_front_follow= 0;
    ctrl_ang= 0;
    ctrl_front_manual= 0;
    ctrl_side_manual= 0;
    aux_dist=5000;
    detect_cont=0;
    vel_steer.linear.x= 0;
    vel_steer.linear.y=1;//1;//enable motors
    vel_steer.angular.z= 0;
    speed_publisher.publish(vel_steer);
    publish_lost_tracked();
    pitakuru_state_msg.state="MANUAL";
    state_pub.publish(pitakuru_state_msg);
    detect_cont=0;
    low_voltage=false;
}
void mode_IDLE()
{
     
    vel_steer.linear.x= 0;
    vel_steer.linear.y=0;//
    vel_steer.angular.z= 0;
    speed_publisher.publish(vel_steer);
    vel_steer.linear.x= 0;
    vel_steer.linear.y=1;//-1;//disable motors
    vel_steer.angular.z= 0;
    speed_publisher.publish(vel_steer);
    stop_functions=false;
    low_voltage=false;
    free_way=true;
    mode_idle=true;
    mode_karugamo=false;
    mode_manual=false;
    danger=false;
    mode_follow=false;
    tracking_people=false;
    tracking_people=false;
    cont_detect_peop=0;
    start_route = false;
    danger=false;
    ROS_INFO("Mode IDLE");
    ctrl_front_follow= 0;
    ctrl_ang= 0;
    ctrl_yaw = 0;
    ctrl_front_manual= 0;
    ctrl_side_manual= 0;
    aux_dist=5000;
    alert_idle_sound();
    for (int i=0;i<2;i++){
        vel_steer.linear.x= 0;
        vel_steer.linear.y=0;//disable motors
        vel_steer.angular.z= 0;
        speed_publisher.publish(vel_steer);
    }
    publish_lost_tracked();
    pitakuru_state_msg.state="IDLE";
    state_pub.publish(pitakuru_state_msg);
    low_voltage=false;
}

void mode_people_follow()
{
    entered_first_time_far=false;
    low_voltage=false;
    mode_idle=false;
    mode_karugamo=false;
    mode_manual=false;
    mode_follow=true;
    tracking_people=false;
    cont_detect_peop=0;
    start_route = false;
    mode_auto=false;
    danger=false;
    free_way=true;
    ctrl_front_follow= 0;
    ctrl_ang= 0;
    ctrl_yaw = 0;
    started_track_yolo=false;
    ctrl_front_manual= 0;
    ctrl_side_manual= 0;
    cont_sp_follow=0;
    stop_functions=false;
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
    aux_dist=5000;
    stop_functions=true;
    publish_lost_tracked();
    pitakuru_state_msg.state="KARUGAMO";
    pitakuru_state_msg.state="KARUGAMO";
    pitakuru_state_msg.state_karugamo="lost";
    state_pub.publish(pitakuru_state_msg);
    pitakuru_state_msg.state_karugamo="losting_with_lidar";
    state_pub.publish(pitakuru_state_msg);
    low_voltage=false;
   
}


void blink_green_sleep(float t){
    alert_idle_no_sound();
    ros::Duration(t).sleep();
    alert_turn_off_led();
    ros::Duration(t).sleep();
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
        joy_counter++;
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
            vel_steer.linear.y= 1;
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
            vel_steer.linear.y= 1;
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
       
        }else if(joy->buttons[2]==1 && free_way && collision == false){//danger!=true && free_way==true){//circulo
            mode_IDLE();
            ros::Duration(0.5).sleep(); // sleep for half a second
        //}else if(joy->buttons[1]==1 && danger!=true && collision == false){//equis
        }else if(joy->buttons[1]==1 && collision == false){//equis
            mode_MANUAL();
            ros::Duration(0.5).sleep(); // sleep for half a second
        }else if(joy->buttons[3] && danger!=true && collision == false ){//triangulo    
             
           
        }else if(joy->buttons[0] && free_way && collision == false){//square
            mode_people_follow();
            vel_steer.linear.x=0;
            vel_steer.linear.y= 1;
            vel_steer.angular.z=0;
            speed_publisher.publish(vel_steer);
            ros::Duration(0.5).sleep(); // sleep for half a second
        }
        joy_front=joy->axes[1];
        joy_side=joy->axes[0];
        ros::Duration duration = ros::Time::now() - last_time_changed;
        //if((duration.toSec())<2.5&& changed_setting==true && stop_functions==false){
        if(counter_changed<8&& changed_setting==true && stop_functions==false){
            //counter_changed++;
            blink_change(duration_change);
        }else if(changed_setting==true && counter_changed>7){
            counter_changed=0;
            changed_setting=false;
            if(mode_manual){
                alert_manual_no_sound();
            }else if(mode_karugamo){
                //alert_ka
                alert_karugamo_near_no_sound();
            }
        }
       
        if(joy->axes[7]!=0 && (mode_manual || mode_follow) && lidar_failed==false ){//side pads
                //blink_change(0.25);
                changed_setting=true;
                last_time_changed=ros::Time::now();
                ROS_INFO("Changed speed , follow  %f , manual %f",max_speed_follow,max_speed_manual);
                if(mode_follow==true){
                    max_speed_follow=max_speed_follow+(joy->axes[7]*400);
                    duration_change-=joy->axes[7]*0.1;
                    frontal_gain_follow=max_speed_follow+200;

                    if(joy->axes[7]>0.5){//pressed up
                        break_front_distance+=0.05;
                        ROS_INFO("Changed break_distance_front %f ",break_front_distance);
                        if(break_front_distance>max_break_distance){
                            break_front_distance=max_break_distance;
                           
                        }
                    }else if(joy->axes[7]<-0.5){
                        break_front_distance-=0.05;
                        ROS_INFO("Changed break_distance_front %f ",break_front_distance);
                        if(break_front_distance<min_break_distance){
                            break_front_distance=min_break_distance;
                        }
                    }
                     
                }
                if(mode_manual){
                    duration_change-=joy->axes[7]*0.1;
                    max_speed_manual=max_speed_manual+(joy->axes[7]*400);
                    max_speed_manual_heavy=max_speed_manual_heavy+(joy->axes[7]*400);
                    if(joy->axes[7]>0.5){//pressed up
                        break_front_distance+=0.05;
                        ROS_INFO("Changed break_distance_front %f ",break_front_distance);
                        if(break_front_distance>max_break_distance){
                            break_front_distance=max_break_distance;
                           
                        }
                    }else if(joy->axes[7]<-0.5){
                        break_front_distance-=0.05;
                        ROS_INFO("Changed break_distance_front %f ",break_front_distance);
                        if(break_front_distance<min_break_distance){
                            break_front_distance=min_break_distance;
                        }
                    }
                }
                if(duration_change<0.1){
                    duration_change=0.1;
                }else if (duration_change>0.5){
                    duration_change=0.5;
                }
                
                if(max_speed_follow>2800){
                    max_speed_follow=2800;
                }else if(max_speed_follow<1200){
                    max_speed_follow=1200;
                }
                if(max_speed_manual>2800){
                    max_speed_manual=2800;
                }else if(max_speed_manual<1200){
                    max_speed_manual=1200;
                }
                if(max_speed_manual_heavy>2400){
                    max_speed_manual_heavy=2400;
                }else if(max_speed_manual_heavy<800){
                    max_speed_manual_heavy=800;
                }
                if(mode_manual){
                        if(max_speed_manual==2800){
                        alert_speed5_sound();
                        }
                        else  if(max_speed_manual==2400){
                        alert_speed4_sound();
                        }
                        else  if(max_speed_manual==2000){
                        alert_speed3_sound();
                        }
                        else  if(max_speed_manual==1600){
                        alert_speed2_sound();
                        }
                        else  if(max_speed_manual==1200){
                        alert_speed1_sound();
                        }
                }

                if(mode_follow){
                        if(max_speed_follow==2800){
                        alert_speed5_sound();
                        }
                        else  if(max_speed_follow==2400){
                        alert_speed4_sound();
                        }
                        else  if(max_speed_follow==2000){
                        alert_speed3_sound();
                        }
                        else  if(max_speed_follow==1600){
                        alert_speed2_sound();
                        }
                        else  if(max_speed_follow==1200){
                        alert_speed1_sound();
                        }
                }
                

                ros::Duration(0.2).sleep(); // sleep for half a second
        }
        if(mode_manual){
              if(free_way){
              //if(true){
                if(heavy){
                    ctrl_front_manual=(1-smooth_accel_manual)*(joy->axes[1]*max_speed_manual_heavy)+(smooth_accel_manual*ctrl_front_manual);
                }else{
                    ctrl_front_manual=(1-smooth_accel_manual)*(joy->axes[1]*max_speed_manual)+(smooth_accel_manual*ctrl_front_manual);
                }
                //if(ctrl_front_manual<20 && ctrl_front_manual>-20){
                //  ctrl_front_manual=0;
                //}
                vel_steer.linear.x= ctrl_front_manual;
                //vel_steer.linear.x=-joy->axes[1]*-max_speed_manual;
                ctrl_side_manual=(1-smooth_accel_side_manual)*(joy->axes[0]*max_speed_side_manual)+(smooth_accel_side_manual*ctrl_side_manual);
                
                
                vel_steer.angular.z=ctrl_side_manual;//+ctrl_side_costmap;
                //vel_steer.angular.z=0;
                
                vel_steer.linear.x=(vel_steer.linear.x/21)*0.1045;
                vel_steer.angular.z=(vel_steer.angular.z/21)*0.1045;
                if(joy_counter%8==0){
                    speed_publisher.publish(vel_steer);
                }
        }else{//else free way
       
            ctrl_front_manual=(1-smooth_accel_manual)*(joy->axes[1]*max_speed_manual_heavy)+(smooth_accel_manual*ctrl_front_manual);
            if(ctrl_front_manual<0){
                ctrl_side_manual=(1-smooth_accel_side_manual)*(joy->axes[0]*max_speed_side_manual)+(smooth_accel_side_manual*ctrl_side_manual);
                //if(ctrl_side_manual<7 && ctrl_side_manual>-7){
                //    ctrl_side_manual=0;
                //}
                vel_steer.linear.x= ctrl_front_manual;
                vel_steer.angular.z=ctrl_side_manual;
                vel_steer.linear.x=(vel_steer.linear.x/21)*0.1045;
                vel_steer.angular.z=(vel_steer.angular.z/21)*0.1045;
                //vel_steer.angular.z=0;
                if(joy_counter%8==0){
                    speed_publisher.publish(vel_steer);
                }
            }else{
                vel_steer.linear.x= 0;
                vel_steer.angular.z= 0;
                if(joy_counter%8==0){
                    speed_publisher.publish(vel_steer);
                }
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
    ros::Subscriber sub_amperage;
    ros::Subscriber sub_estim;
    ros::Publisher marker_pub;
    ros::Publisher pos_peop_pub;
    ros::Publisher path_pub;
    ros::Publisher m1_pub;
    ros::Publisher m2_pub;
    ros::Publisher yolo_peop_pub;
    ros::Publisher state_pub;

    ros::Publisher estim_pub;

    ros::Subscriber volts_subscriber;
    ros::Subscriber cost_subscriber;    
    ros::Subscriber yolo_subscriber;
   
    geometry_msgs::Twist vel_steer;
    geometry_msgs::Vector3 tracked_pos;
    std_msgs::Float32 ang_people;
    visualization_msgs::Marker people_point;
    nav_msgs::Path path;
    geometry_msgs::PoseStamped posestamped;
    control_xy::States pitakuru_state_msg;


    bool save_waypoint,start_tray,col_avoid_mode,danger, mode_idle,mode_karugamo,mode_manual,mode_follow,free_way,collision,mode_auto;
    float angulo_seguimiento,sp_yaw,sp_yaw2,ctrl_yaw,error_yaw,yaw,distanciaPeople,distanciaPeople2,break_front_distance,break_danger,max_speed_karugamo,max_speed_follow,max_speed_manual,max_speed_manual_heavy,ctrl_ang,ctrl_lin;
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
    bool tracking,is_near,stop_follow,stop_functions,heavy;
    int sound_counter,danger_counter;
    int counter_search,state_stop;
    float saved_ang,speed_wp_lost;
    float near_far_distance;
    float angle_last,max_defelct_angle;
int save_counter,amp_count_l,amp_count_r;
    float dist_robot_people,smooth_accel_manual,smooth_accel_karugamo_near,smooth_accel_karugamo_far,angle_gain_wp,max_dist_toacc;
    float smooth_accel_stop,smooth_accel_side_manual;
    float ctrl_add_front,ctrl_add_side;
    float joy_front,joy_side,avg_amp_l,avg_amp_r;
    float tresh_amp_up,tresh_amp_down,trigger_vel,trigger_current;
    float int_r_curr,int_l_curr,der_r_curr,der_l_curr,filt_r_curr,filt_l_curr,prev_r_curr,prev_l_curr;
    bool n_flag_r,d_flag_r,n_flag_l,d_flag_l, detected_heavy;
    float fil_der_r_curr,max_r_curr,fil_der_l_curr,max_l_curr;
    int  heavy_r,heavy_l,count_to_miss;
    double time_last_to_heavy;
    float vel_m1,vel_m2,vel_detect_scan,volts_charge,peak_curr_tresh,avg_curr_tresh,peak_not_heavy_curr;
    float cost_obst,ctrl_side_costmap,gain_to_costmap,smooth_accel_costmap,dist_peop_cam,yolo_status;
    bool tracking_lidar,tracking_yolo,tracking_yolo_lidar,find_again;
    float lidar_people_status;
    int count_again,counter_blink;
    float new_tracked_cx,new_tracked_cy,aux_dist_again,new_tracked_angle;
    float vel_detect_costmap;
    bool status_led_blue,status_led_green,status_led_yellow,status_led_red;
    double duration_to_lost;
    ros::Time time_blink_bl,time_blink_volts,time_blink_scan,time_blink_red;
    ros::Time  last_time_tracking;
    ros::Time  last_time_scan;
    ros::Time  last_time_obstacle;
    ros::Time  last_time_changed;
    ros::Time  start_time_track_yolo;
    bool big_angle_error_lidar_yolo;
    int count_angle_err;
    bool changed_setting;
    float duration_change;
    bool test;
    bool low_voltage,started_track_yolo,lidar_failed,entered_first_time_far;
    int counter_changed,counter_low_voltage,joy_counter,karugamo_counter;
    float min_break_distance,max_break_distance;
};

int main(int argc, char **argv)
{
    ros::init(argc, argv, "heading_follow_node");
    ros::NodeHandle nh;
    test_head test_head_obj(nh);
    //ros::Rate rate(0.5); //0.5 Hz, every 2 second
    ros::Rate rate(100); //100 Hz, every .01 second
    //printf("%f",-atan2(5,1)*180/3.1416);
    //ros::Duration(5.0).sleep(); // sleep for half a second
    //ros::Duration(22.0).sleep();
    for (int i=1;i<44;i++){
        test_head_obj.blink_green_sleep(0.2);
    }
   
    test_head_obj.mode_IDLE();
    //test_head_obj.alert_turn_off_led();
    while(ros::ok())
    {
        ros::spinOnce();
        test_head_obj.calc_100hz();
        test_head_obj.check_scan();
        test_head_obj.check_obsta();
        test_head_obj.check_low_volt();
        rate.sleep();
    }
    return 0;
}

