
#include "ros/ros.h"
#include <std_msgs/String.h>
#include <std_msgs/Int16.h>
#include <std_msgs/Float32.h>
#include <std_msgs/Float64.h>
#include <geometry_msgs/Twist.h>
#include <geometry_msgs/Vector3.h>
#include <geometry_msgs/PoseStamped.h>
#include <geometry_msgs/PoseWithCovariance.h>
#include <geometry_msgs/PoseWithCovarianceStamped.h>
#include "sensor_msgs/LaserScan.h"
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
#include <actionlib_msgs/GoalStatusArray.h>

class test_head
{
public:
    test_head(ros::NodeHandle nh)
    {
        // robot speed command with Twisted(linear.x, angular.z, linear.y:flag, but not used)
        speed_publisher = nh.advertise<geometry_msgs::Twist>(nh.resolveName("/cmd_vel"), 1);
        //send_command to disble_enable motors
        enable_disable_pub = nh.advertise<std_msgs::String>(nh.resolveName("/enable_disable"), 1);
        // tracking target with lidar, Vector3(position x, y, z:angular)
        tracked_publisher = nh.advertise<geometry_msgs::Vector3>(nh.resolveName("/tracked"), 2);
        // it shows colors, sounds and blink or not
        alerts_publisher = nh.advertise<std_msgs::Int16>(nh.resolveName("/alerts"), 1);
        // pitakuru state + tracking target position? Twisted(linear(x,y:angle,z:tracking(positive) or not(negative)):lidar, angular(x,y,z:same usage):yolo)
        state_pub = nh.advertise<control_xy::States>(nh.resolveName("/pitakuru_states"),1);
        // used in auto pilot mode
        goal_status_subscriber = nh.subscribe("/move_base_flex/move_base/status", 1, &test_head::goalStatusCallback,this);
        // input from joystick controller (buttons, axes)
        joy_subscriber = nh.subscribe("/j0/joy", 1, &test_head::joyCallback,this);

        // lidar
        // tracking target with lidar, Vector3(position x, y)
        ang_subscriber2 = nh.subscribe("peopAng2", 2, &test_head::angPeopCallback,this);
        // costmap to avoid obstacles in people following mode calculated in cosmap/main.py?
        cost_subscriber = nh.subscribe("/costdetect", 1, &test_head::costCallback,this);
        cost_subscriber_auxiliar = nh.subscribe("/costdetect_aux", 1, &test_head::costCallbackAux,this);
        // raw lidar scaned points, for danger mode
        subScan_ = nh.subscribe("/scan", 1, &test_head::scanCallback,this);
        // button and bumper sensors states on pitakuru notificated from arduino
        state_subscriber = nh.subscribe("/trigger_action", 1, &test_head::stateCallback,this);
        // motor vel, current : estimate the load weight and change accel params
        sub_amperage = nh.subscribe("/stateWheels",1,&test_head::amperageCallback,this);
        // battery voltage
        volts_subscriber = nh.subscribe("/volts", 1, &test_head::voltsCallback,this);

        // yolo
        // tracking target poisition with YOLO, see in people_ext_sort.py
        yolo_subscriber = nh.subscribe("/peop_ang_yolo", 1, &test_head::yoloCallback,this);


        danger_suscriber = nh.subscribe("/Danger", 1, &test_head::dangerCallback,this);
        danger_back_suscriber = nh.subscribe("/danger_back", 1, &test_head::dangerBackCallback,this);

        nh.getParam("/control_xy/break_front_distance", break_front_distance);
        nh.getParam("/control_xy/break_danger", break_danger);
        nh.getParam("/control_xy/low_vel_gain_follow", low_vel_gain_follow);
        nh.getParam("/control_xy/frontal_gain_follow", frontal_gain_follow);
        nh.getParam("/control_xy/max_speed_follow", max_speed_follow);
        nh.getParam("/control_xy/max_speed_follow_heavy", max_speed_follow_heavy);
        nh.getParam("/control_xy/max_speed_side_follow", max_speed_side_follow);
        nh.getParam("/control_xy/max_speed_manual", max_speed_manual);
        nh.getParam("/control_xy/max_speed_manual_heavy", max_speed_manual_heavy);
        nh.getParam("/control_xy/near_far_distance",near_far_distance);
        nh.getParam("/control_xy/max_speed_side_manual", max_speed_side_manual);
        nh.getParam("/control_xy/smooth_accel_karugamo_near", smooth_accel_karugamo_near);
        nh.getParam("/control_xy/smooth_accel_manual", smooth_accel_manual);
        nh.getParam("/control_xy/dist_robot_people", dist_robot_people);
        nh.getParam("/control_xy/max_dist_toacc", max_dist_toacc);
        nh.getParam("/control_xy/smooth_accel_stop",smooth_accel_stop);
        nh.getParam("/control_xy/smooth_accel_side_manual",smooth_accel_side_manual);
        nh.getParam("/control_xy/smooth_accel_side_follow",smooth_accel_side_follow);
        nh.getParam("/control_xy/tresh_amp_up",tresh_amp_up);
        nh.getParam("/control_xy/tresh_amp_down",tresh_amp_down);
        nh.getParam("/control_xy/trigger_vel",trigger_vel);
        nh.getParam("/control_xy/trigger_current",trigger_current);
        nh.getParam("/control_xy/max_l_curr",high_thress_r_curr);
        nh.getParam("/control_xy/vel_detect_scan",vel_detect_scan);
        nh.getParam("/control_xy/volts_charge",volts_charge);
        nh.getParam("/control_xy/avg_curr_tresh",avg_curr_tresh);
        nh.getParam("/control_xy/heavy_curr_tresh",heavy_curr_tresh);
        nh.getParam("/control_xy/mid_curr_tresh",mid_curr_tresh);
        nh.getParam("/control_xy/peak_not_heavy_curr",peak_not_heavy_curr);
        nh.getParam("/control_xy/gain_to_costmap",gain_to_costmap);
        nh.getParam("/control_xy/smooth_accel_costmap",smooth_accel_costmap);
        nh.getParam("/control_xy/vel_detect_costmap",vel_detect_costmap);
        nh.getParam("/control_xy/duration_to_lost",duration_to_lost);
        nh.getParam("/control_xy/min_break_distance",min_break_distance);
        nh.getParam("/control_xy/max_break_distance",max_break_distance);
        nh.getParam("/control_xy/gain_follow_people",gain_follow_people);
        nh.getParam("/control_xy/use_ps4_controller",use_ps4_controller);
        nh.getParam("/control_xy/use_hokuyo",use_hokuyo);

        ROS_INFO_STREAM(" *  *  *  *  *  * break_distance "<< break_front_distance << " break danger " << break_danger 
        << " max_speed_follow " << max_speed_follow << " max_speed_manual " << max_speed_manual << " use_ps4 " << use_ps4_controller);
        missing_track = 0;
        ang_peop_yolo = -500;
        tracked_angle = 0;
        ang_peop_lidar = 0;
        distanciaPeople2 = 0;     
        mode_idle = true;
        mode_manual = false;
        mode_karugamo = false;
        mode_follow = false;
        tracking_people = false;
        mode_auto = false;
        danger = false;
        free_way = true;
        collision = false;
        is_near = true;
        detect_cont = 0;
        stopped_functions = false;
        heavy = true;
        detect_curr_inc_right = false;
        detect_curr_inc_left = false;
        heavy_by_right = 0;
        heavy_by_left = 0;
        detected_heavy = false;
        tracking_lidar = false;
        changed_setting = false;
        duration_change = 0.30;
        low_voltage = false;
        counter_changed = 0;
        lidar_failed = false;
        joy_counter = 0;
        karugamo_counter = 0;
        ctrl_add_side = 0; 
        ctrl_add_front = 0;
        last_mode_auto = false;
        has_wp1 = false;
        has_wp2 = false;
        reseting_map = false;
        saving_map = false;
        danger_back = false;
        motors_enabled = true;
        status_led_yellow = false;
    }
    ~test_head(){}
   


// auto pilot mode
void goalStatusCallback(const actionlib_msgs::GoalStatusArray::ConstPtr& status){
    int status_id = 0;
    
    if (!status -> status_list.empty() && mode_auto){
        int size_arr = sizeof(status -> status_list)/sizeof(status -> status_list[0]);
        ROS_INFO("tam_arr %i",size_arr);
    }
    if (!status -> status_list.empty() && mode_auto){
        
        int size_arr = sizeof(status -> status_list)/sizeof(status -> status_list[0]);
        actionlib_msgs::GoalStatus goalStatus = status -> status_list[0];
        status_id = goalStatus.status;
        if(status_id == 1 || velocity_motor1>0.05 || velocity_motor2>0.05){
            is_navigating = true;
            pitakuru_state_msg.state = "AUTONOMOUS_NAVIGATION";
            pitakuru_state_msg.state_navigation = "going_to_wp";
            state_pub.publish(pitakuru_state_msg);
            is_arrived_goal = false;
            count_arrived = 0;
        }else if(status_id == 3 && (velocity_motor1<0.05 && velocity_motor2<0.05) && danger == false){
            count_arrived++;
            if(is_navigating && count_arrived>10 && go_wp1){
                is_navigating = false;
                pitakuru_state_msg.state = "AUTONOMOUS_NAVIGATION";
                pitakuru_state_msg.state_navigation = "arrived_wp1";
                state_pub.publish(pitakuru_state_msg);
                is_arrived_goal = true;
                alert_arrived_wp1_voice_sound();
                ros::Duration(0.1).sleep(); 
            }else if(is_navigating && count_arrived>10 && go_wp2){
                is_navigating = false;
                pitakuru_state_msg.state = "AUTONOMOUS_NAVIGATION";
                pitakuru_state_msg.state_navigation = "arrived_wp2";
                state_pub.publish(pitakuru_state_msg);
                is_arrived_goal = true;
                alert_arrived_wp1_voice_sound();
                ros::Duration(0.1).sleep(); 
            }
        }
        
    }else{
        is_navigating = false;
        is_arrived_goal = false;
    }
}


// get arduino button states
void stateCallback(const control_xy::TriggerAction& data){
        // bumper sensor
        if(data.trigger == "collision" && collision == false){
            collisioned();
            collision = true;
            /* [TODO: remove this sleep] */
            ros::Duration(0.5).sleep(); 
        
        // black button
        }else if(data.trigger == "break_release_button_on" && collision == true){
            remove_collision();
            mode_IDLE();
            /* [TODO: remove this sleep] */
            ros::Duration(0.5).sleep(); 

        // yellow button
        } else if(data.trigger == "karugamo_button_on" && mode_follow == false  && collision == false){
            mode_people_follow();
            /* [TODO: move into a function: void stop_motor()] */
            vel_steer.linear.x = 0;
            vel_steer.linear.y = 1;
            vel_steer.angular.z = 0;
            speed_publisher.publish(vel_steer);
            /* [TODO: remove this sleep] */
            ros::Duration(0.4).sleep(); 
            
        } else if(data.trigger == "karugamo_button_on" && mode_follow == true  && collision == false){
            mode_IDLE();
            /* [TODO: remove this sleep] */
            ros::Duration(0.4).sleep(); 
        }
       
}

/* create a node to check voltage */
// if battery voltage is low, then blink led in red
void check_low_volt(){
    if(low_voltage && lidar_failed == false && danger == false  ){
        blink_red(0.6);
    }
}
// get battery voltage and check it low or not.
void voltsCallback(const std_msgs::Float32& msg){
    if((msg.data+0.1)<volts_charge ){
        counter_low_voltage++;
        if((abs(velocity_motor1) > 0.15 || abs(velocity_motor2) > 0.15) && counter_low_voltage > 1 && (mode_manual || mode_follow) && danger == false){
            if(low_voltage == false){
                alert_low_battery_sound();
                low_voltage = true;
                low_voltage = true;
                ROS_INFO("detected_low voltage");
                ros::Duration(0.05).sleep(); 
                alert_low_battery_sound();
            }
            
        }
    }else{
       
        counter_low_voltage = 0;
    }
}    

// store received costmap
void costCallback(const geometry_msgs::Vector3& vector){  
    cost_obst = vector.x;
}
// store received costmapauxiliar
void costCallbackAux(const geometry_msgs::Vector3& vector){  
    cost_obst_aux = vector.x;
}

// get motor encoder values and calculate load weight
/* [TODO:] create filter function */
/* [TODO:] create common functions for right and left wheels */
void amperageCallback(const control_xy::StateWheels& msg) {
    float flag;
    float trig_vel = 0.25;
    float dt = 0.02;
    float alf = 0.75;
    velocity_motor1 = msg.left_vel;
    velocity_motor2 = msg.right_vel;
    //It was done like that, because using absolute decimals were truncated
    if (velocity_motor1 < 0){ 
        velocity_motor1 = velocity_motor1 * -1;
    }
    if (velocity_motor2 < 0){
        velocity_motor2 = velocity_motor2 * -1;
    }
    if(abs(msg.right_vel) < trig_vel && abs(msg.left_vel) < trig_vel){
        integ_right_curr = 0;
        deriv_right_curr = 0;
        detect_curr_inc_right = false;
        high_thress_r_curr = 0;
        average_amperes_right = 0;
        filtered_deriv_right_curr = 0;
        heavy_by_right = 0;
        heavy = true;
        detected_heavy = false;
        pitakuru_state_msg.state_load = "almost_stop";
    }else{
        pitakuru_state_msg.state_load = "checking_for_load";
        integ_right_curr = integ_right_curr + msg.right_current * dt;
        deriv_right_curr = (msg.right_current-prev_right_curr)/dt;
        filtered_deriv_right_curr = filtered_deriv_right_curr * alf+ deriv_right_curr * (1-alf);
        prev_right_curr = msg.right_current;
        if(filtered_deriv_right_curr > 0.4 && detected_heavy == false){
            if(detect_curr_inc_right == false){
                time_last_to_heavy = ros::Time::now().toSec();
            }
            detect_curr_inc_right = true;
            if(msg.right_current > high_thress_r_curr){
                high_thress_r_curr = msg.right_current;
            }
        }
        
        if(filtered_deriv_right_curr < 0.01 && detect_curr_inc_right == true && detected_heavy == false){
           
            amp_measurem_right++;
            average_amperes_right = average_amperes_right + msg.right_current;
            if(amp_measurem_right > 3 ){
                amp_measurem_right = 0;
                average_amperes_right = average_amperes_right / 4;
                if(average_amperes_right > avg_curr_tresh && high_thress_r_curr > heavy_curr_tresh ){
                    
                    heavy_by_right = 1;
                    detected_heavy = true;

                    pitakuru_state_msg.state_load = "heavy_load_right";
                    
                } else if (average_amperes_right > avg_curr_tresh && high_thress_r_curr > mid_curr_tresh ){
                    heavy_by_right = 3;
                    detected_heavy = true;
                    pitakuru_state_msg.state_load = "mid_load_right";
                    
                } else if (high_tresh_l_curr < peak_not_heavy_curr){
                    heavy_by_right = 2;
                    
                }
            }
            
        }
    }
   
    if(abs(msg.left_vel) < trig_vel && abs(msg.right_vel) < trig_vel){
        integ_left_curr = 0;
        deriv_left_curr = 0;
        detect_curr_inc_left = false;
        high_tresh_l_curr = 0;
        average_amperage_left = 0;
        filtered_deriv_left_curr = 0;
        heavy_by_left = 0;
        heavy = true;
        detected_heavy = false;
    }else{
        integ_left_curr = integ_left_curr + msg.left_current * dt;
        deriv_left_curr = (msg.left_current-prev_l_curr)/dt;
       
        filtered_deriv_left_curr = filtered_deriv_left_curr * alf + deriv_left_curr * (1-alf);
        prev_l_curr = msg.left_current;
       
        if(filtered_deriv_left_curr > 0.4 && detected_heavy == false){
            detect_curr_inc_left = true;
           
            if(msg.left_current > high_tresh_l_curr){
                high_tresh_l_curr = msg.left_current;
            }
        }
        
        if(filtered_deriv_left_curr < 0.01 && detect_curr_inc_left == true && detected_heavy == false){
            amp_measurem_left++;
            average_amperage_left = average_amperage_left+msg.left_current;
            if(amp_measurem_left > 3 ){
                amp_measurem_left = 0;
                average_amperage_left = average_amperage_left/4; 
                if(average_amperage_left > avg_curr_tresh && high_tresh_l_curr >heavy_curr_tresh){
                    heavy_by_left = 1;
                    detected_heavy = true;
                    pitakuru_state_msg.state_load = "heavy_load_left";
                }else if(average_amperage_left > avg_curr_tresh && high_thress_r_curr>mid_curr_tresh ){
                    
                    heavy_by_right = 3;
                    detected_heavy = true;
                    pitakuru_state_msg.state_load = "mid_load_left";
                    
                }else if (high_tresh_l_curr < peak_not_heavy_curr){
                    heavy_by_left = 2;
                }  
            }
            ROS_INFO("entered in change right");
        }
    }

    if(heavy == true && (heavy_by_left == 1 || heavy_by_right == 1) && detected_heavy == false && (ros::Time::now().toSec() - time_last_to_heavy)<6.9){
        heavy = true;
        pitakuru_state_msg.state_load = "heavy_load_detected";
    }else if(heavy == true && (heavy_by_left == 3 || heavy_by_right == 3) && detected_heavy == false && (ros::Time::now().toSec() - time_last_to_heavy)<6.9){
        heavy = true;
        pitakuru_state_msg.state_load = "middle_load_detected";
    }else if(detected_heavy == false && heavy_by_left == 2 && heavy_by_right == 2 && (ros::Time::now().toSec() - time_last_to_heavy)>4.3 && (ros::Time::now().toSec() - time_last_to_heavy)<6.3 && abs(msg.left_vel)>4.1 && abs(msg.right_vel)>4.1 ){
        heavy = false;
        pitakuru_state_msg.state_load = "not_heavy_load_detected";       
    }   
}

// store target position with yolo
void yoloCallback(const geometry_msgs::Vector3& msg){
    yolo_status = msg.x;
    /* [TODO:] convert speed to rpm */
    dist_peop_cam = msg.y * 100;
    ang_peop_yolo = msg.z;
}


/* [TODO:] move these led function into switch.py */
void blink_blue2(float dur){
    ros::Time time_now = ros::Time::now();
    ros::Duration duration = time_now - time_blink_bl;
    if((duration.toSec())>dur){
        time_blink_bl = time_now;
        if(status_led_blue){
            status_led_blue = false;
            alert_karugamo_near_no_sound();
        }else{
            status_led_blue = true;
            alert_turn_off_led();
        }
    }
}


void blink_yellow(float dur){
    ros::Time time_now = ros::Time::now();
    ros::Duration duration = time_now - time_blink_yellow;
    if(duration.toSec() > dur){
        
        time_blink_yellow = time_now;
        if(status_led_yellow){
            status_led_yellow = false;
            alert_yellow_no_sound();
        }else{
            status_led_yellow = true;
            alert_turn_off_led();
        }
    }
}

void blink_green(float dur){
    ros::Time time_now = ros::Time::now();
    ros::Duration duration = time_now - time_blink_green;
    if(duration.toSec() > dur){
        
        time_blink_green = time_now;
        if(status_led_green){
            status_led_green = false;
            alert_idle_no_sound();
        }else{
            status_led_green = true;
            alert_turn_off_led();
        }
    }
}

void blink_red(float dur){
    ros::Time time_now = ros::Time::now();
    ros::Duration duration = time_now - time_blink_red;
    if(duration.toSec()>dur){
        
        time_blink_red = time_now;
        if(status_led_red){
            status_led_red = false;
            alert_collision_no_sound();
        }else{
            status_led_red = true;
            alert_turn_off_led();
        }
    }
}

// blink if velocity setting is changed
void blink_change(float dur){
    ros::Time time_now = ros::Time::now();
    ros::Duration duration = time_now - time_blink_bl;
    if(duration.toSec() > dur){
        time_blink_bl = time_now;
        counter_changed++;
        if(status_led_blue){
            status_led_blue = false;
            alert_danger_no_sound();
        }else{
            status_led_blue = true;
            alert_turn_off_led();
        }
    }
}


// check whether lidar is stopped
/* [TODO:] move this function into pitakuru/lidar_detect.py, reset lidar if it does not work and send alert command to switch.py */
void check_scan_msg(){
    ros::Time time_now = ros::Time::now();
    ros::Duration duration = time_now - last_time_scan;
    if(duration.toSec() > 0.9){
        lidar_failed = true;
        pitakuru_state_msg.state_scan = "lidar_fail";
        ros::Duration duration2 = time_now - time_blink_scan;
        if(duration2.toSec()>0.1){
            time_blink_scan = time_now;
            if(status_led_yellow){
                status_led_yellow = false;
                alert_collision_no_sound();
            }else{
                status_led_yellow = true;
                alert_turn_off_led();
            }
        }
    }else{
        pitakuru_state_msg.state_scan = "lidar_ok";
        if(lidar_failed){
            lidar_failed = false;
            if(mode_manual){
                alert_manual_no_sound();
            }
            if(mode_follow){
                alert_karugamo_near_no_sound();
            }
            if(mode_idle){
                alert_idle_no_sound();
            }
            if(collision){
                alert_collision_no_sound();
            }
            if(danger){
                alert_danger_no_sound();
            }
        }
    }
}

/* [TODO:] move this function main_sorted_kalman.py */
// notificate if obstacle_detector with lidar does not detect.
void check_people_obsta_msg(){
    ros::Time time_now = ros::Time::now();
    ros::Duration duration = time_now - last_time_obstacle_received;
    if(duration.toSec() > 0.9){
        pitakuru_state_msg.state_karugamo = "no_people_lidar_detection";
        setNoTrackPosLidar();
        state_pub.publish(pitakuru_state_msg);
        last_time_obstacle_received = ros::Time::now();
    }
}


// reset people following variables
/* [TODO:] move this function next to reset functions */
void restart_follow_variables(){
    tracking_people = true;
    tracking_people = true;
    missing_track = 0;
    tracked_pos.x = tracking_cx;
    tracked_pos.y = tracking_cy;
    tracked_pos.z = ang_peop_lidar;
    tracked_publisher.publish(tracked_pos);
    //ctrl_front_follow = 0;
    //ctrl_ang = 0;
    //vel_steer.linear.x = 0;
    //vel_steer.angular.z = 0;
    ctrl_add_side = 0;
    is_near = true;
    stopped_functions = false;
    ctrl_side_costmap = 0;
    sound_counter=0;
}

// calculate
// - target position
// - robot velocity
// - notification led, sound to arduino
void calc_100hz(){
    karugamo_counter++;
    if(!motors_enabled){
        blink_green(0.9);
    }
    if(danger == false && collision == false && mode_manual){
        ros::Time time_now = ros::Time::now();
        ros::Duration duration = time_now - last_time_btn_save_reset_pressed;
            if((duration.toSec()) < 17 && reseting_map){
                blink_yellow(0.25);
            }else if(reseting_map){
                reseting_map = false;
                alert_manual_no_sound();
            }
            if((duration.toSec())<30 && saving_map){
                blink_yellow(0.4);
            }else if(saving_map){
                saving_map = false;
                alert_manual_no_sound();
            }      
    }
    if(danger == false && collision == false && mode_auto && (velocity_motor1>0.15 || velocity_motor2>0.15)){
        blink_yellow(0.4);
        if(karugamo_counter % 390 == 0){
            alert_navigating_voice_sound();
            if(go_wp1){
                pitakuru_state_msg.state_navigation = "going_to_wp_1";
                state_pub.publish(pitakuru_state_msg);
            }else if(go_wp2){
                pitakuru_state_msg.state_navigation = "going_to_wp_2";
                state_pub.publish(pitakuru_state_msg);
            }
        }
    }else if(danger == false && collision == false && mode_auto && (velocity_motor1<0.15 || velocity_motor2<0.15) && is_arrived_goal == true){
        alert_yellow_no_sound();
    }else if(danger == false && collision == false && mode_auto && velocity_motor1<0.15 && velocity_motor2<0.15){
        alert_yellow_no_sound();
    }
    
    
    if(mode_idle && karugamo_counter % 20 == 0 ){
        vel_steer.linear.x = 0;
        vel_steer.angular.z = 0;
        speed_publisher.publish(vel_steer);
    }
    
    float velocity_tresh_sound = 1;
    float control_tresh_sound = 200;
    //if (mode_manual && velocity_motor1 > velocity_tresh_sound && velocity_motor2 > velocity_tresh_sound && (ctrl_front_manual > control_tresh_sound ||  control_tresh_sound > ctrl_front_manual > -control_tresh_sound ) ){
    if (mode_manual  && (ctrl_front_manual > control_tresh_sound ||  -control_tresh_sound > ctrl_front_manual ) ){
        if(karugamo_counter % 600 == 0 ){
            alert_saved_wp1_voice_sound();
        }
    }
    distanciaPeople2 = sqrt(center_x * center_x + center_y * center_y) * 100;
    ang_peop_lidar = 90 - atan2(center_x,center_y) * 180 / 3.1416 ; 
    if(distanciaPeople2 > near_far_distance){
        lidar_people_status=-1;
    }
    if(lidar_people_status > 0 && stopped_functions == true && yolo_status > 0){
        restart_follow_variables();
        ROS_INFO("restar folow variable");
        stopped_functions = false;
    }
   
    if(lidar_people_status>0){
        stopped_functions = false;
    }

    if (danger && danger_back == false){
    //if (danger){
        ctrl_front_manual = (1-smooth_accel_manual) * (joy_front * max_speed_manual_heavy)+(smooth_accel_manual * ctrl_front_manual);
        if(ctrl_front_manual<0){
            ctrl_side_manual = (1-smooth_accel_side_manual) * (joy_side * max_speed_side_manual) + (smooth_accel_side_manual * ctrl_side_manual);
            vel_steer.linear.x = ctrl_front_manual;
            vel_steer.angular.z = ctrl_side_manual;
            vel_steer.linear.x = ((vel_steer.linear.x / 21) * 0.1045) / 10;
            vel_steer.angular.z = ((vel_steer.angular.z / 21) * 0.1045) / 2;
            if(joy_counter % 4 == 0){
                speed_publisher.publish(vel_steer);
            }
        }else{
            vel_steer.linear.x = 0;
            vel_steer.angular.z = 0;
            if(joy_counter % 4 == 0){
                speed_publisher.publish(vel_steer);
            }
        }
    }
   
    if(mode_follow && danger != true ){ 
            if(lidar_people_status > 0 && stopped_functions == false && distanciaPeople2 < near_far_distance && ang_peop_lidar>-90 && ang_peop_lidar<90){
                tracked_angle = ang_peop_lidar;
                last_time_tracking = ros::Time::now();
                if(karugamo_counter % 400 == 0 ){
                    alert_danger_sound();
                }
                near();
                ROS_INFO("near()");
                if(lidar_failed == false && changed_setting == false && low_voltage == false){
                    alert_karugamo_near_no_sound();
                }
               
                pitakuru_state_msg.state = "KARUGAMO";
                pitakuru_state_msg.state_karugamo = "tracking_lidar";
                pitakuru_state_msg.state_shelf = "no_problem";
                pitakuru_state_msg.trackeds.linear.x = distanciaPeople2;
                pitakuru_state_msg.trackeds.linear.y = ang_peop_lidar;
                pitakuru_state_msg.trackeds.linear.z = lidar_people_status;
                pitakuru_state_msg.trackeds.angular.x = dist_peop_cam;
                pitakuru_state_msg.trackeds.angular.y = ang_peop_yolo;
                pitakuru_state_msg.trackeds.angular.z = yolo_status;
                state_pub.publish(pitakuru_state_msg);
                missing_track = 0;
                tracking_cx = center_x;
                tracking_cy = center_y;
                tracked_pos.x = center_x;
                tracked_pos.y = center_y;
                tracked_pos.z = tracked_angle;
                tracked_publisher.publish(tracked_pos);  
            }

            else if(danger == false  && (lidar_people_status < 0 || (lidar_people_status > 0 && distanciaPeople2 >= near_far_distance) || (ang_peop_lidar<-90 || ang_peop_lidar>90)) && stopped_functions == false){
                
                    if(lidar_failed == false && low_voltage == false){
                        blink_blue2(0.25);
                    }
                    
                    ros::Time time_now = ros::Time::now();
                    ros::Duration duration = time_now - last_time_tracking;
                    if(duration.toSec()>duration_to_lost){
                        last_time_tracking = ros::Time::now();
                        pitakuru_state_msg.state = "KARUGAMO";
                        pitakuru_state_msg.state_karugamo = "lost";
                        pitakuru_state_msg.state_shelf = "passed_lost_time";
                        pitakuru_state_msg.ctrl_front = ctrl_front_follow;
                        pitakuru_state_msg.ctrl_side = ctrl_ang;
                        state_pub.publish(pitakuru_state_msg);
                        alert_lost_voice_sound();
                        stopped_functions = true;
                        tracking_lidar = false;
                        ROS_INFO("LOST");
                        tracking_people = false;
                        missing_track = 0;
                        tracking_cx = 0;
                        tracking_cy = 0;
                        ctrl_side_costmap = 0;
                        publish_lost_tracked();
                        missing_track = 0;
                        
                    }else{
                        ctrl_front_follow = (1-smooth_accel_stop) * (0)+(smooth_accel_stop * ctrl_front_follow);
                        ctrl_yaw = 0;
                        vel_steer.linear.x = ctrl_front_follow;
                        vel_steer.angular.z = ctrl_yaw;
                        vel_steer.linear.x = ((vel_steer.linear.x/21) * 0.1045)/10;
                        vel_steer.angular.z = ((vel_steer.angular.z/21) * 0.1045)/2;
                        speed_publisher.publish(vel_steer);
                        pitakuru_state_msg.ctrl_front = ctrl_front_follow;
                        pitakuru_state_msg.ctrl_side = ctrl_ang;
                        pitakuru_state_msg.state_shelf = "in_process_to_lost";
                        state_pub.publish(pitakuru_state_msg);
                    }
                
            }
           
            if(stopped_functions == true && tracking_people == false){
                if(lidar_failed == false && low_voltage == false){
                    blink_blue2(0.25);
                }
                

                sound_counter++;
                if(sound_counter%500 == 0){
                    alert_search_voice_sound();
                }

                if(danger){
                    ctrl_front_follow = 0;
                    ctrl_yaw = 0;
                    vel_steer.linear.x = ctrl_front_follow;
                    vel_steer.angular.z = ctrl_yaw;
                    vel_steer.linear.x = ((vel_steer.linear.x/21) * 0.1045)/10;
                    vel_steer.angular.z = ((vel_steer.angular.z/21) * 0.1045)/2;
                    pitakuru_state_msg.ctrl_front = ctrl_front_follow;
                    pitakuru_state_msg.ctrl_side = ctrl_ang;
                    speed_publisher.publish(vel_steer);
                }else{
                    ctrl_front_follow = (1-smooth_accel_stop) * (0)+(smooth_accel_stop * ctrl_front_follow);
                    ctrl_yaw = 0;
                    vel_steer.linear.x = ctrl_front_follow;
                    vel_steer.angular.z = ctrl_yaw;
                    vel_steer.linear.x = ((vel_steer.linear.x/21) * 0.1045)/10;
                    vel_steer.angular.z = ((vel_steer.angular.z/21) * 0.1045)/2;
                    speed_publisher.publish(vel_steer);
                    pitakuru_state_msg.ctrl_front = ctrl_front_follow;
                    pitakuru_state_msg.ctrl_side = ctrl_ang;
                    tracked_pos.x = -.050;
                    tracked_pos.y = -.050;   
                }  
                pitakuru_state_msg.state = "KARUGAMO";
                pitakuru_state_msg.state_karugamo = "losting_with_lidar";
                pitakuru_state_msg.trackeds.linear.x = distanciaPeople2;
                pitakuru_state_msg.trackeds.linear.y = ang_peop_lidar;
                pitakuru_state_msg.trackeds.linear.z = lidar_people_status;
                pitakuru_state_msg.trackeds.angular.x = dist_peop_cam;
                pitakuru_state_msg.trackeds.angular.y = ang_peop_yolo;
                pitakuru_state_msg.trackeds.angular.z = yolo_status;
                pitakuru_state_msg.state_shelf = "in_stopped_functions";
                pitakuru_state_msg.ctrl_front = ctrl_front_follow;
                pitakuru_state_msg.ctrl_side = ctrl_ang;
                state_pub.publish(pitakuru_state_msg);    
            } 
    }
}


// store target position with lidar
void angPeopCallback(const geometry_msgs::Vector3& msg){
    center_x = msg.x;
    center_y = msg.y;
    lidar_people_status = msg.z;

    last_time_obstacle_received = ros::Time::now();    
}

// lost
void setNoTrackPosLidar(){
    center_x = -0.050;
    center_y = -0.050;
    lidar_people_status = -1;
}

void publish_lost_tracked(){
    tracked_pos.x = -0.050;
    tracked_pos.y = -0.050;
    tracked_pos.z = 0;
    tracked_publisher.publish(tracked_pos);
}

// tracking target is near to robot
/* move this function in karugamo mode function */
void near(){
       if(mode_follow && danger != true && stopped_functions == false){            
            //ang_peop_lidar = 90 - atan2(center_x,center_y) * 180 / 3.1416 ;
            //distanciaPeople2 = sqrt(center_x * center_x+center_y * center_y) * 100;
            //ROS_INFO("near() an%f d%f",ang_peop_lidar,distanciaPeople2);
            
            tracked_angle = ang_peop_lidar;
            missing_track = 0;
            tracking_cx = center_x;
            tracking_cy = center_y;
            tracked_pos.x = center_x;
            tracked_pos.y = center_y;
            tracked_pos.z = tracked_angle;
            tracked_publisher.publish(tracked_pos);
            geometry_msgs::Twist vel_steer;  
            ctrl_ang = low_vel_gain_follow * ang_peop_lidar - ctrl_ang/2;
            ctrl_add_side = (1 - smooth_accel_side_follow) * (joy_side * max_speed_side_follow) + (smooth_accel_side_follow * ctrl_add_side);
            pitakuru_state_msg.side_joystick = ctrl_add_side;
            //float cost_mix = 0;
            
            //if (cost_obst > cost_obst_aux){
            //   cost_mix = cost_obst;
            //}else{
            //    cost_mix = cost_obst_aux; 
            //}

            if(ctrl_front_follow  >= vel_detect_costmap){
                pitakuru_state_msg.state_costmap = "costmap_active";
                ctrl_side_costmap = (1 - smooth_accel_side_follow) * (cost_obst * max_speed_side_follow) + (smooth_accel_side_follow * ctrl_side_costmap);
                pitakuru_state_msg.costmap = ctrl_side_costmap;
            }else{
                ctrl_side_costmap = 0;
                pitakuru_state_msg.state_costmap = "costmap_inactive";
                pitakuru_state_msg.costmap = ctrl_side_costmap;
            }
            ctrl_ang = ctrl_ang + ctrl_add_side + ctrl_side_costmap * gain_to_costmap;
            if (ctrl_ang > max_speed_side_follow){
                ctrl_ang = max_speed_side_follow;
            }else if (ctrl_ang <- max_speed_side_follow){
                ctrl_ang = -max_speed_side_follow;
            }
            vel_steer.angular.z = ctrl_ang;

            if(distanciaPeople2 > dist_robot_people){
                float  norm_dist,dist_conv;
                dist_conv = distanciaPeople2;
                if(dist_conv>max_dist_toacc){
                    dist_conv = max_dist_toacc;
                    norm_dist = (dist_conv-dist_robot_people) / (max_dist_toacc-dist_robot_people);
                }else{
                    norm_dist = (dist_conv-dist_robot_people) / (max_dist_toacc-dist_robot_people);
                }
                if (heavy){
                    ctrl_front_follow = (1-smooth_accel_karugamo_near) * ( gain_follow_people * frontal_gain_follow * norm_dist) + (smooth_accel_karugamo_near * ctrl_front_follow);
                    ctrl_add_front = (1-smooth_accel_karugamo_near) * (joy_front * max_speed_follow_heavy)+(smooth_accel_karugamo_near * ctrl_front_manual);
                    
                    if(ctrl_front_follow > vel_detect_costmap){
                        ctrl_front_follow = ctrl_front_follow + ctrl_add_front - abs(ctrl_side_costmap * gain_to_costmap * 0.1);
                    }else{
                        ctrl_front_follow = ctrl_front_follow + ctrl_add_front;
                    }
                    if(ctrl_front_follow < 0){
                        ctrl_front_follow = 0;
                        vel_steer.linear.x = 0;
                    }
                    if (ctrl_front_follow > max_speed_follow_heavy){
                        ctrl_front_follow = max_speed_follow_heavy;
                    }
                }else{
                    ctrl_front_follow = (1 - smooth_accel_karugamo_near) * (gain_follow_people * max_speed_follow * norm_dist) + (smooth_accel_karugamo_near * ctrl_front_follow);
                    ctrl_add_front = (1 - smooth_accel_karugamo_near) * (joy_front * max_speed_follow)+(smooth_accel_karugamo_near * ctrl_front_manual);
                    if(ctrl_front_follow > vel_detect_costmap){
                        ctrl_front_follow = ctrl_front_follow+ctrl_add_front - abs(ctrl_side_costmap * gain_to_costmap * 0.1);
                    }else{
                        ctrl_front_follow = ctrl_front_follow+ctrl_add_front;
                    }
                    if(ctrl_front_follow < 0 ){
                        ctrl_front_follow = 0;
                        vel_steer.linear.x = 0;
                    }
                    if (ctrl_front_follow > max_speed_follow){
                        ctrl_front_follow = max_speed_follow;
                    }
                }
                
                vel_steer.linear.x = ctrl_front_follow;
            }else{
                ctrl_front_follow = (1 - smooth_accel_stop) * (0) + (smooth_accel_stop * ctrl_front_follow);
                vel_steer.linear.x = 0;
                ctrl_side_costmap = 0;
                
            }
            pitakuru_state_msg.ctrl_front = ctrl_front_follow;
            pitakuru_state_msg.ctrl_side = ctrl_ang;
            vel_steer.linear.x = ((vel_steer.linear.x/21) * 0.1045)/10;
            vel_steer.angular.z = ((vel_steer.angular.z/21) * 0.1045)/2;
            if(karugamo_counter %2 == 0){
                speed_publisher.publish(vel_steer);
            }
        }       
}  

void dangerBackCallback(const std_msgs::String& msg){
    // ROS_INFO("%s\n", msg.data.c_str());
    float velocity_tresh_stop = 1.0;
    float control_tresh_stop = -400.0;
    // ROS_INFO("%d\n", danger);
    // ROS_INFO("%d\n", velocity_motor1 > velocity_tresh_stop);
    // ROS_INFO("%d\n", velocity_motor2 > velocity_tresh_stop);
    // ROS_INFO("%f\n", velocity_motor1);
    // ROS_INFO("%f\n", velocity_motor2);
    // ROS_INFO("%f\n", velocity_tresh_stop);
    //if ( danger == false && msg.data == "Danger" && velocity_motor1 > velocity_tresh_stop && velocity_motor2 > velocity_tresh_stop && (ctrl_front_follow < control_tresh_stop || ctrl_front_manual < control_tresh_stop) ){
    if ( msg.data == "Danger" && velocity_motor1 > velocity_tresh_stop && velocity_motor2 > velocity_tresh_stop && (ctrl_front_follow < control_tresh_stop || ctrl_front_manual < control_tresh_stop) ){
        alert_danger_no_sound();
        alert_danger_voice_sound();
        danger = true;
        free_way = false;
        danger_back = true;
        detect_cont = 0;
        ctrl_front_follow = 0;
        ctrl_front_manual = 0;
        ctrl_side_manual = 0;
        vel_steer.linear.x = 0;
        vel_steer.linear.y = 0;
        vel_steer.angular.z = 0;
        for (int i=0;i<35;i++){
            alert_danger_no_sound();
            speed_publisher.publish(vel_steer);
            ros::Duration(0.02).sleep();
        }
        alert_danger_voice_sound();
        pitakuru_state_msg.state = "DANGER";
        pitakuru_state_msg.ctrl_front = ctrl_front_follow;
        pitakuru_state_msg.ctrl_side = ctrl_ang;
        state_pub.publish(pitakuru_state_msg);
    }//else if(danger == false && msg.data == "Clear"){
    else if(msg.data == "Clear"){    
        free_way = true;
        danger_back = false; 
    }

    danger_counter++;

    if(danger && danger_counter % 2 == 0 && ctrl_front_manual > 0){
        alert_danger_no_sound();
        vel_steer.linear.x = 0;
        vel_steer.angular.z = 0;
        speed_publisher.publish(vel_steer);
    }
}



void dangerCallback(const std_msgs::String& msg){
    // ROS_INFO("%s\n", msg.data.c_str());
    float velocity_tresh_stop = 1.0;
    float control_tresh_stop = 500.0;
    // ROS_INFO("%d\n", danger);
    // ROS_INFO("%d\n", velocity_motor1 > velocity_tresh_stop);
    // ROS_INFO("%d\n", velocity_motor2 > velocity_tresh_stop);
    // ROS_INFO("%f\n", velocity_motor1);
    // ROS_INFO("%f\n", velocity_motor2);
    // ROS_INFO("%f\n", velocity_tresh_stop);
    if ( danger == false && msg.data == "Danger" && velocity_motor1 > velocity_tresh_stop && velocity_motor2 > velocity_tresh_stop && (ctrl_front_follow > control_tresh_stop || ctrl_front_manual > control_tresh_stop) ){
        alert_danger_no_sound();
        alert_danger_voice_sound();
        danger = true;
        free_way = false;
        detect_cont = 0;
        ctrl_front_follow = 0;
        ctrl_front_manual = 0;
        ctrl_side_manual = 0;
        vel_steer.linear.x = 0;
        vel_steer.linear.y = 0;
        vel_steer.angular.z = 0;
        for (int i=0;i<15;i++){
            alert_danger_no_sound();
            speed_publisher.publish(vel_steer);
            ros::Duration(0.02).sleep();
        }
        alert_danger_voice_sound();
        pitakuru_state_msg.state = "DANGER";
        pitakuru_state_msg.ctrl_front = ctrl_front_follow;
        pitakuru_state_msg.ctrl_side = ctrl_ang;
        state_pub.publish(pitakuru_state_msg);
    }else if(danger == false && msg.data == "Clear"){
        free_way=true;
    }

    danger_counter++;

    if(danger && danger_counter % 2 == 0 && ctrl_front_manual > 0){
        alert_danger_no_sound();
        vel_steer.linear.x = 0;
        vel_steer.angular.z = 0;
        speed_publisher.publish(vel_steer);
    }
}



// to find the danger obstacle and notify
/* [TODO:] create a node for this function */ 
void scanCallback(const sensor_msgs::LaserScan::ConstPtr& scan){ 
    int num_detections_to_danger = 1;       
    last_time_scan = ros::Time::now();
} 

// alert_command.sound = COLLISION_SOUND
// pub.publish(alert_command)

// void alert_sound(int data_type) {
//     alerts_command.data = data_type;
//     alerts_publisher.publish(alerts_command);
// }


// alert with sound or led
void alert_collision_sound(){
    alerts_command.data = 6;
    alerts_publisher.publish(alerts_command);
}
void alert_collision_no_sound(){
    alerts_command.data = 76;
    alerts_publisher.publish(alerts_command);
}
void  alert_manual_sound(){
    alerts_command.data = 1;
    alerts_publisher.publish(alerts_command);
}
void  alert_manual_no_sound(){
    alerts_command.data = 71;
    alerts_publisher.publish(alerts_command);
}
void  alert_idle_sound(){
    alerts_command.data = 2;
    alerts_publisher.publish(alerts_command);
}
void  alert_idle_no_sound(){
    alerts_command.data = 72;
    alerts_publisher.publish(alerts_command);
}
void  alert_turn_off_led(){
    alerts_command.data = 100;
    alerts_publisher.publish(alerts_command);
}

void  alert_warning_sound(){
    alerts_command.data = 4;
    alerts_publisher.publish(alerts_command);
}
void  alert_warning_no_sound(){
    alerts_command.data = 74;
    alerts_publisher.publish(alerts_command);
}
void  alert_danger_sound(){
    alerts_command.data = 5;
    alerts_publisher.publish(alerts_command);
}
void  alert_danger_no_sound(){
    alerts_command.data = 75;
    alerts_publisher.publish(alerts_command);
}

void  alert_karugamo_near_sound(){
    alerts_command.data = 8;
    alerts_publisher.publish(alerts_command);
}
void  alert_karugamo_near_no_sound(){
    alerts_command.data = 78;
    alerts_publisher.publish(alerts_command);
}
void  alert_karugamo_far_sound(){
    alerts_command.data = 3;
    alerts_publisher.publish(alerts_command);
}
void  alert_yellow_no_sound(){
    alerts_command.data = 73;
    alerts_publisher.publish(alerts_command);
}

void  alert_speed1_sound(){
    alerts_command.data = 101;
    alerts_publisher.publish(alerts_command);
}
void  alert_speed2_sound(){
    alerts_command.data = 102;
    alerts_publisher.publish(alerts_command);
}
void  alert_speed3_sound(){
    alerts_command.data = 103;
    alerts_publisher.publish(alerts_command);
}
void  alert_speed4_sound(){
    alerts_command.data = 104;
    alerts_publisher.publish(alerts_command);
}
void  alert_speed5_sound(){
    alerts_command.data = 105;
    alerts_publisher.publish(alerts_command);
}

void  alert_karugamo_waypoint_sound(){
    alerts_command.data = 106;
    alerts_publisher.publish(alerts_command);
}
void  alert_low_battery_sound(){
    alerts_command.data = 108;
    alerts_publisher.publish(alerts_command);
}

void  alert_danger_voice_sound(){
    alerts_command.data = 107;
    alerts_publisher.publish(alerts_command);
}
void  alert_lost_voice_sound(){
    alerts_command.data = 109;
    alerts_publisher.publish(alerts_command);
}
void  alert_search_voice_sound(){
    alerts_command.data = 110;
    alerts_publisher.publish(alerts_command);
}

void  alert_navigating_voice_sound(){
    alerts_command.data = 111;
    alerts_publisher.publish(alerts_command);
}

void  alert_arrived_wp1_voice_sound(){
    alerts_command.data = 112;
    alerts_publisher.publish(alerts_command);
}
void  alert_arrived_wp2_voice_sound(){
    alerts_command.data = 113;
    alerts_publisher.publish(alerts_command);
}

void  alert_saved_wp1_voice_sound(){
    alerts_command.data = 114;
    alerts_publisher.publish(alerts_command);
}

void  alert_saved_wp2_voice_sound(){
    alerts_command.data = 115;
    alerts_publisher.publish(alerts_command);
}

void  alert_goto_wp1_voice_sound(){
    alerts_command.data = 116;
    alerts_publisher.publish(alerts_command);
}

void  alert_goto_wp2_voice_sound(){
    alerts_command.data = 117;
    alerts_publisher.publish(alerts_command);
}

void  alert_careful_voice_sound(){
    alerts_command.data = 118;
    alerts_publisher.publish(alerts_command);
}


// reset all variables when the state was changed
void reset_variables() {

}

// called when robot detect collision
void collisioned(){
    low_voltage = false;
    collision = true;
    vel_steer.linear.x = 0;
    vel_steer.linear.y = 0;
    vel_steer.angular.z = 0;
    speed_publisher.publish(vel_steer);
    vel_steer.linear.x = 0;
    vel_steer.linear.y = -1;
    vel_steer.angular.z = 0;
    speed_publisher.publish(vel_steer);
    vel_steer.linear.x = 0;
    vel_steer.linear.y = -1;
    vel_steer.angular.z = 0;
    speed_publisher.publish(vel_steer);
    alert_collision_sound();
    danger = true;
    mode_idle = false;
    mode_manual = false;
    mode_karugamo = false;
    mode_follow = false;
    free_way = false;
    tracking_people = false;
    ctrl_front_follow = 0;
    ctrl_ang = 0;
    ctrl_front_manual = 0;
    ctrl_side_manual = 0;
    stopped_functions = false;
    vel_steer.linear.x = 0;
    vel_steer.linear.y = -1;
    vel_steer.angular.z = 0;
    speed_publisher.publish(vel_steer);
    publish_lost_tracked();
    pitakuru_state_msg.state = "COLLISION";
    state_pub.publish(pitakuru_state_msg);
    last_mode_auto = false;
}

// called when pushed black button after collision
void remove_collision(){
    low_voltage = false;
    collision = false;
    mode_idle = true;
    mode_manual = false;
    mode_karugamo = false;
    mode_follow = false;
    danger = false;
    free_way = true;
    tracking_people = false;
    ctrl_front_follow = 0;
    ctrl_ang = 0;
    ctrl_front_manual = 0;
    ctrl_side_manual = 0;
    stopped_functions = false;
    alert_idle_sound();
    vel_steer.linear.x = 0;
    vel_steer.linear.y = 0;
    vel_steer.angular.z = 0;
    vel_steer.linear.x = 0;
    vel_steer.linear.y = -1;
    vel_steer.angular.z = 0;
    speed_publisher.publish(vel_steer);
    tracked_angle = 0;
    ang_peop_lidar = 0;
    distanciaPeople2 = 0;
    publish_lost_tracked();
    pitakuru_state_msg.state = "IDLE";
    state_pub.publish(pitakuru_state_msg);
    last_mode_auto = false;
}


// reset variables when the state transit to autopilot mode
void do_nothing(){
    detect_curr_inc_left = false;
    detect_curr_inc_right = false;
    low_voltage = false;
    mode_idle = false;
    mode_karugamo = false;
    mode_manual = false;
    mode_follow = false;
    tracking_people = false;
    mode_auto = true;
    danger = false;
    free_way = true;
    stopped_functions = false;
    ROS_INFO("do_nothing");
    ctrl_front_follow = 0;
    ctrl_ang = 0;
    ctrl_front_manual = 0;
    ctrl_side_manual = 0;
    detect_cont = 0;
    vel_steer.linear.x = 0;
    vel_steer.linear.y = 1;
    vel_steer.angular.z = 0;
    speed_publisher.publish(vel_steer);
    publish_lost_tracked();    
    detect_cont = 0;
    low_voltage = false;
}


// reset variables when the state transit to autopilot mode 2
void mode_AUTONOMOUS(){
    detect_curr_inc_left = false;
    detect_curr_inc_right = false;
    low_voltage = false;
    mode_idle = false;
    mode_karugamo = false;
    mode_manual = false;
    mode_follow = false;
    mode_auto = true;
    tracking_people = false;
    danger = false;
    free_way = true;
    stopped_functions = false;
    alert_yellow_no_sound();
    ctrl_front_follow = 0;
    ctrl_ang = 0;
    ctrl_front_manual = 0;
    ctrl_side_manual = 0;
    detect_cont = 0;
    vel_steer.linear.x = 0;
    vel_steer.linear.y = 1;
    vel_steer.angular.z = 0;
    speed_publisher.publish(vel_steer);
    publish_lost_tracked(); 
    pitakuru_state_msg.state = "AUTONOMOUS_NAVIGATION";
    state_pub.publish(pitakuru_state_msg);
    detect_cont = 0;
    low_voltage = false;
    last_mode_auto = true;
}

// reset variables when the state transit to manual
void mode_MANUAL(){
    detect_curr_inc_left = false;
    detect_curr_inc_right = false;
    low_voltage = false;
    mode_idle = false;
    mode_karugamo = false;
    mode_manual = true;
    mode_follow = false;
    tracking_people = false;
    mode_auto = false;
    danger = false;
    free_way = true;
    stopped_functions = false;
    ROS_INFO("Mode Manual");
    alerts_command.data = 1;
    alerts_publisher.publish(alerts_command);
    ctrl_front_follow = 0;
    ctrl_ang = 0;
    ctrl_front_manual = 0;
    ctrl_side_manual = 0;
    detect_cont = 0;
    vel_steer.linear.x = 0;
    vel_steer.linear.y = 1;
    vel_steer.angular.z = 0;
    speed_publisher.publish(vel_steer);
    publish_lost_tracked();
    pitakuru_state_msg.state = "MANUAL";
    state_pub.publish(pitakuru_state_msg);
    detect_cont = 0;
    low_voltage = false;
    last_mode_auto = false;
}

// reset variables when the state transit to idle mode
void mode_IDLE(){
    danger_back = false;
    vel_steer.linear.x = 0;
    vel_steer.linear.y = 0;
    vel_steer.angular.z = 0;
    speed_publisher.publish(vel_steer);
    vel_steer.linear.x = 0;
    vel_steer.linear.y = 1;
    vel_steer.angular.z = 0;
    speed_publisher.publish(vel_steer);
    stopped_functions = false;
    low_voltage = false;
    free_way = true;
    mode_idle = true;
    mode_karugamo = false;
    mode_manual = false;
    mode_auto = false;
    danger = false;
    mode_follow = false;
    tracking_people = false;
    tracking_people = false;
    danger = false;
    ROS_INFO("Mode IDLE");
    ctrl_front_follow = 0;
    ctrl_ang = 0;
    ctrl_yaw = 0;
    ctrl_front_manual = 0;
    ctrl_side_manual = 0;
    alert_idle_sound();
    for (int i = 0;i<2;i++){
        vel_steer.linear.x = 0;
        vel_steer.linear.y = 0;
        vel_steer.angular.z = 0;
        speed_publisher.publish(vel_steer);
    }
    publish_lost_tracked();
    pitakuru_state_msg.state = "IDLE";
    state_pub.publish(pitakuru_state_msg);
    low_voltage = false;
    last_mode_auto = false;
}

// reset variables when the state transit to karugamo mode
void mode_people_follow()
{
    low_voltage = false;
    mode_idle = false;
    mode_karugamo = false;
    mode_manual = false;
    mode_follow = true;
    tracking_people = false;
    mode_auto = false;
    danger = false;
    free_way = true;
    ctrl_front_follow = 0;
    ctrl_ang = 0;
    ctrl_yaw = 0;
    ctrl_add_side = 0;
    ctrl_front_manual = 0;
    ctrl_side_manual = 0;
    stopped_functions = false;
    alert_karugamo_near_sound();
    ROS_INFO("Mode People Follow");
    is_near = true;
    stopped_functions = true;
    publish_lost_tracked();
    pitakuru_state_msg.state = "KARUGAMO";
    pitakuru_state_msg.state_karugamo = "lost";
    state_pub.publish(pitakuru_state_msg);
    pitakuru_state_msg.state_karugamo = "losting_with_lidar";
    state_pub.publish(pitakuru_state_msg);
    low_voltage = false;
    last_mode_auto = false;   
}

void blink_green_sleep(float t){
    alert_idle_no_sound();
    ros::Duration(t).sleep();
    alert_turn_off_led();
    ros::Duration(t).sleep();
}

void disable_motors(){
    enable_disable_msg.data = "disable";
    enable_disable_pub.publish(enable_disable_msg);
    motors_enabled = false;
}

void enable_motors(){
    enable_disable_msg.data = "enable";
    enable_disable_pub.publish(enable_disable_msg);
    motors_enabled = true;
    
}

void joyCallback(const sensor_msgs::Joy::ConstPtr& joy){
        joy_counter++;
        float speed_button;
        float btn_x,btn_square,btn_circle,btn_triangle;
        float btn_save_wp1,btn_save_wp2,btn_goto_wp1,btn_goto_wp2,btn_l3,btn_r3;
        float btn_reset_map,btn_saving_map;
        btn_save_wp1 = false;
        btn_save_wp2 = false;
        btn_goto_wp1 = false;
        btn_goto_wp2 = false;
        btn_reset_map = false;
        btn_saving_map = false;
        if(use_ps4_controller == 1){
            speed_button = joy -> axes[7];
            btn_x = joy -> buttons[1];
            btn_triangle = joy -> buttons[3];
            btn_square = joy -> buttons[0];
            btn_circle = joy -> buttons[2];
            btn_save_wp1 = joy -> buttons[8];
            btn_save_wp2 = joy -> buttons[9];
            btn_goto_wp1 = joy -> buttons[6];
            btn_goto_wp2 = joy -> buttons[7];
            btn_l3 = joy -> buttons[11];
            btn_r3 = joy -> buttons[12];
            btn_reset_map = joy -> buttons[4];
            btn_saving_map = joy -> buttons[5];
        }else{
            speed_button = joy -> axes[5];
            btn_x = joy -> buttons[2];
            btn_triangle = joy -> buttons[1];
            btn_square = joy -> buttons[0];
            btn_circle = joy -> buttons[3];
            btn_save_wp1 = joy -> buttons[10];
            btn_save_wp2 = joy -> buttons[11];
            btn_goto_wp1 = joy -> buttons[6];
            btn_goto_wp2 = joy -> buttons[7];
            btn_reset_map = joy -> buttons[4];
            btn_saving_map = joy -> buttons[5];
            btn_l3 = joy -> buttons[8];
            btn_r3 = joy -> buttons[9];
        }
        if (motors_enabled){
            if(btn_circle == 1  && collision == false && danger != true){
            mode_MANUAL();
            ros::Duration(0.5).sleep(); 
            }else if(btn_x == 1 && collision == false && danger != true){
                mode_people_follow();
                vel_steer.linear.x = 0;
                vel_steer.linear.y = 1;
                vel_steer.angular.z = 0;
                speed_publisher.publish(vel_steer);
                ros::Duration(0.5).sleep(); 
            }else if(btn_triangle && collision == false ){
                mode_IDLE();
                ros::Duration(0.2).sleep(); 
            }else if(reseting_map == false&& btn_reset_map&& mode_manual && collision == false && danger == false){
                reseting_map = true;
                last_time_btn_save_reset_pressed = ros::Time::now();
                ros::Duration(0.3).sleep(); 
            }else if(btn_saving_map&& mode_manual && collision == false && danger == false){
                saving_map = true;
                last_time_btn_save_reset_pressed = ros::Time::now();
                ros::Duration(0.3).sleep(); 
            }else if(btn_square && free_way && danger != true&& collision == false ){
                mode_AUTONOMOUS();   
                do_nothing();
                ros::Duration(0.2).sleep(); 
            }else if(btn_save_wp1 == 1){
                pitakuru_state_msg.state_navigation =  "save_wp_1";
                state_pub.publish(pitakuru_state_msg);
                alert_saved_wp1_voice_sound();
                ros::Duration(0.1).sleep(); 
                pitakuru_state_msg.state_navigation =  "saved_wp_1";
                state_pub.publish(pitakuru_state_msg);
                has_wp1 = true;
            }else if(btn_save_wp2 == 1){
                pitakuru_state_msg.state_navigation =  "save_wp_2";
                state_pub.publish(pitakuru_state_msg);
                alert_saved_wp2_voice_sound();
                ros::Duration(0.1).sleep(); 
                pitakuru_state_msg.state_navigation =  "saved_wp_2";
                state_pub.publish(pitakuru_state_msg);
                has_wp2 =  true;
            }else if(btn_goto_wp1 == 1&&mode_auto && has_wp1){
                pitakuru_state_msg.state_navigation =  "goto_wp_1";
                state_pub.publish(pitakuru_state_msg);
                alert_goto_wp1_voice_sound();
                ros::Duration(0.1).sleep(); 
                pitakuru_state_msg.state_navigation =  "going_to_wp_1";
                state_pub.publish(pitakuru_state_msg);
                go_wp1 =  true;
                go_wp2 =  false;
            }else if(btn_goto_wp2 == 1 && mode_auto && has_wp2){
                pitakuru_state_msg.state_navigation = "goto_wp_2";
                state_pub.publish(pitakuru_state_msg);
                alert_goto_wp2_voice_sound();
                ros::Duration(0.1).sleep(); 
                pitakuru_state_msg.state_navigation =  "going_to_wp_2";
                state_pub.publish(pitakuru_state_msg);
                go_wp2 =  true;
                go_wp1 =  false;
            }else if(btn_l3 == 1){
                
            }
        }
        
        
        if(btn_r3 == 1){
            if(motors_enabled){
                disable_motors();
            }else{
                enable_motors();
                mode_IDLE();
            }
            ros::Duration(0.5).sleep();
            
        }

        joy_front = joy -> axes[1];
        joy_side = joy -> axes[0];
        ros::Duration duration = ros::Time::now() - last_time_changed;
        
        if(counter_changed < 8&& changed_setting == true && stopped_functions == false){
            blink_change(duration_change);
        }else if(changed_setting == true && counter_changed > 7){
            counter_changed = 0;
            changed_setting = false;
            if(mode_manual){
                alert_manual_no_sound();
            }else if(mode_karugamo){
                alert_karugamo_near_no_sound();
            }
        }
        
        if(speed_button != 0 && (mode_manual || mode_follow) && lidar_failed == false ){
                
                changed_setting = true;
                last_time_changed = ros::Time::now();
                ROS_INFO("Changed speed , follow  %f , manual %f",max_speed_follow,max_speed_manual);
                if(mode_follow == true){
                    max_speed_follow = max_speed_follow + (speed_button * 400);
                    max_speed_follow_heavy = max_speed_follow_heavy+(speed_button * 400);
                    duration_change -= speed_button * 0.1;
                    frontal_gain_follow = max_speed_follow+200;

                    if(speed_button > 0.5){
                        break_front_distance += 0.05;
                        ROS_INFO("Changed break_distance_front %f ",break_front_distance);
                        if(break_front_distance > max_break_distance){
                            break_front_distance =  max_break_distance;
                        }
                    }else if(speed_button <- 0.5){
                        break_front_distance -= 0.05;
                        ROS_INFO("Changed break_distance_front %f ",break_front_distance);
                        if(break_front_distance<min_break_distance){
                            break_front_distance = min_break_distance;
                        }
                    }
                     
                }
                if(mode_manual){
                    duration_change -= speed_button * 0.1;
                    max_speed_manual = max_speed_manual + (speed_button * 400);
                    max_speed_manual_heavy =  max_speed_manual_heavy + (speed_button * 400);
                    if(speed_button > 0.5){
                        break_front_distance += 0.05;
                        ROS_INFO("Changed break_distance_front %f ",break_front_distance);
                        if(break_front_distance > max_break_distance){
                            break_front_distance =  max_break_distance;
                        }
                    }else if(speed_button < -0.5){
                        break_front_distance -= 0.05;
                        ROS_INFO("Changed break_distance_front %f ",break_front_distance);
                        if(break_front_distance < min_break_distance){
                            break_front_distance =  min_break_distance;
                        }
                    }
                }
                if(duration_change < 0.1){
                    duration_change =  0.1;
                }else if (duration_change > 0.5){
                    duration_change = 0.5;
                }
                
                if(max_speed_follow > 2800){
                    max_speed_follow = 2800;
                }else if(max_speed_follow < 1200){
                    max_speed_follow = 1200;
                }
                if(max_speed_follow_heavy > 2800){
                    max_speed_follow_heavy =  2800;
                }else if(max_speed_follow_heavy < 1200){
                    max_speed_follow_heavy =  1200;
                }
                if(max_speed_manual > 2800){
                    max_speed_manual =  2800;
                }else if(max_speed_manual < 1200){
                    max_speed_manual = 1200;
                }
                if(max_speed_manual_heavy > 2400){
                    max_speed_manual_heavy =  2400;
                }else if(max_speed_manual_heavy < 1200){
                    max_speed_manual_heavy =  1200;
                }
                if(mode_manual){
                        if(max_speed_manual == 2800){
                        alert_speed5_sound();
                        }
                        else  if(max_speed_manual == 2400){
                        alert_speed4_sound();
                        }
                        else  if(max_speed_manual == 2000){
                        alert_speed3_sound();
                        }
                        else  if(max_speed_manual == 1600){
                        alert_speed2_sound();
                        }
                        else  if(max_speed_manual == 1200){
                        alert_speed1_sound();
                        }
                }

                if(mode_follow){
                        if(max_speed_follow == 2800){
                        alert_speed5_sound();
                        }
                        else  if(max_speed_follow == 2400){
                        alert_speed4_sound();
                        }
                        else  if(max_speed_follow == 2000){
                        alert_speed3_sound();
                        }
                        else  if(max_speed_follow == 1600){
                        alert_speed2_sound();
                        }
                        else  if(max_speed_follow == 1200){
                        alert_speed1_sound();
                        }
                }
                ros::Duration(0.2).sleep(); 
        }
        if(mode_manual){
            if(danger == false){
                
                if(heavy){
                    ctrl_front_manual = (1 - smooth_accel_manual) * (joy -> axes[1] * max_speed_manual_heavy)+(smooth_accel_manual * ctrl_front_manual);
                }else{
                    ctrl_front_manual = (1 - smooth_accel_manual) * (joy -> axes[1] * max_speed_manual)+(smooth_accel_manual * ctrl_front_manual);
                }
                
                vel_steer.linear.x = ctrl_front_manual;
                //if(90 > ctrl_front_manual && ctrl_front_manual > -90){
                //    vel_steer.linear.x = 0.0;
                //}
                float treshold_detection_decceleration = 250;//this must be lower than the threshold stop
                float treshold_stop = 405;
                float joystick_thresh = 0.1;
                if ((joystick_thresh > joy_front &&  ctrl_front_manual > treshold_detection_decceleration) ){
                    if( treshold_stop > ctrl_front_manual){
                        vel_steer.linear.x = 0.0;
                        ctrl_front_manual = 0;
                    }
                }else if (joy_front > -joystick_thresh && -(treshold_detection_decceleration - (treshold_detection_decceleration / 2))  > ctrl_front_manual){
                    if(ctrl_front_manual > -treshold_stop ){
                        vel_steer.linear.x = 0.0;
                        ctrl_front_manual = 0;
                    }
                }
                ctrl_side_manual = (1 - smooth_accel_side_manual) * (joy -> axes[0] * max_speed_side_manual)+(smooth_accel_side_manual * ctrl_side_manual);
                vel_steer.angular.z = ctrl_side_manual;

                float treshold_detection_decceleration_side = 50;//this must be lower than the threshold stop
                float treshold_stop_side = 70;
                float joystick_thresh_side = 0.1;
                if ((joystick_thresh_side > joy_side &&  ctrl_side_manual > treshold_detection_decceleration_side) ){
                    if( treshold_stop_side > ctrl_side_manual){
                        vel_steer.angular.z = 0.0;
                        ctrl_side_manual = 0;
                    }
                }else if (joy_side > -joystick_thresh_side && - (treshold_detection_decceleration_side - (treshold_detection_decceleration_side / 2))  > ctrl_side_manual){
                    if(  ctrl_side_manual > -treshold_stop_side ){
                        vel_steer.angular.z = 0.0;
                        ctrl_side_manual = 0;
                    }
                }

                vel_steer.linear.x = ((vel_steer.linear.x / 21) * 0.1045) / 10;
                vel_steer.angular.z = ((vel_steer.angular.z / 21) * 0.1045) / 2;
                if(joy_counter % 4 == 0){
                    speed_publisher.publish(vel_steer);
                    state_pub.publish(pitakuru_state_msg);
                }
            }/*else{
       
                ctrl_front_manual = (1-smooth_accel_manual) * (joy -> axes[1] * max_speed_manual_heavy)+(smooth_accel_manual * ctrl_front_manual);
                if(ctrl_front_manual<0){
                    ctrl_side_manual = (1-smooth_accel_side_manual) * (joy -> axes[0] * max_speed_side_manual) + (smooth_accel_side_manual * ctrl_side_manual);
                    vel_steer.linear.x = ctrl_front_manual;
                    vel_steer.angular.z = ctrl_side_manual;
                    vel_steer.linear.x = ((vel_steer.linear.x / 21) * 0.1045) / 10;
                    vel_steer.angular.z = ((vel_steer.angular.z / 21) * 0.1045) / 2;
                    if(joy_counter%8 == 0){
                        speed_publisher.publish(vel_steer);
                    }
                }else{
                    vel_steer.linear.x = 0;
                    vel_steer.angular.z = 0;
                    if(joy_counter%8 == 0){
                        speed_publisher.publish(vel_steer);
                    }
                }          
            }   */         
        }
}
   
private:
    ros::Subscriber ang_subscriber2;    
    ros::Publisher alerts_publisher;
    ros::Publisher tracked_publisher;
    ros::Publisher speed_publisher;
    std_msgs::Int16 alerts_command;
    ros::Subscriber state_subscriber;
    ros::Subscriber joy_subscriber;
    ros::Subscriber subScan_;
    ros::Subscriber sub_amperage;
    ros::Publisher  state_pub;
    ros::Subscriber volts_subscriber;
    ros::Subscriber cost_subscriber;    
    ros::Subscriber cost_subscriber_auxiliar; 
    ros::Subscriber yolo_subscriber;
    ros::Subscriber goal_status_subscriber;
    ros::Subscriber danger_suscriber;
    ros::Subscriber danger_back_suscriber;
    ros::Publisher enable_disable_pub;
    std_msgs::String enable_disable_msg;
    geometry_msgs::Twist vel_steer;
    geometry_msgs::Vector3 tracked_pos;
    control_xy::States pitakuru_state_msg;

    bool danger, mode_idle,mode_karugamo,mode_manual,mode_follow,free_way,collision,mode_auto;
    float ctrl_yaw,distanciaPeople2,break_front_distance,break_danger,max_speed_follow,max_speed_manual,max_speed_manual_heavy,ctrl_ang;
    float low_vel_gain_follow,ctrl_side_manual,max_speed_side_manual;
    bool tracking_people;
    float ang_peop_yolo,ang_peop_lidar,tracked_angle,tracking_cx,tracking_cy;
    int missing_track;
    float frontal_gain_follow,ctrl_front_follow;
    float ctrl_front_manual,center_x,center_y;
    int detect_cont;
    bool is_near,stopped_functions,heavy;
    int sound_counter,danger_counter;
    float near_far_distance;
    int amp_measurem_left,amp_measurem_right;
    float dist_robot_people,smooth_accel_manual,smooth_accel_karugamo_near,max_dist_toacc;
    float smooth_accel_stop,smooth_accel_side_manual;
    float ctrl_add_front,ctrl_add_side;
    float joy_front,joy_side,average_amperage_left,average_amperes_right;
    float tresh_amp_up,tresh_amp_down,trigger_vel,trigger_current;
    float integ_right_curr,integ_left_curr,deriv_right_curr,deriv_left_curr,prev_right_curr,prev_l_curr;
    bool detect_curr_inc_right,detect_curr_inc_left, detected_heavy;
    float filtered_deriv_right_curr,high_thress_r_curr,filtered_deriv_left_curr,high_tresh_l_curr;
    int  heavy_by_right,heavy_by_left;
    double time_last_to_heavy;
    float velocity_motor1,velocity_motor2,vel_detect_scan,volts_charge,mid_curr_tresh,heavy_curr_tresh,avg_curr_tresh,peak_not_heavy_curr;
    float cost_obst,cost_obst_aux,ctrl_side_costmap,gain_to_costmap,smooth_accel_costmap,dist_peop_cam,yolo_status;
    bool tracking_lidar;
    float lidar_people_status,max_speed_side_follow;
    float max_speed_follow_heavy;
    float vel_detect_costmap;
    bool status_led_blue,status_led_yellow,status_led_red,status_led_green;
    double duration_to_lost;
    ros::Time time_blink_bl,time_blink_scan,time_blink_red,time_blink_yellow,time_blink_green;
    ros::Time  last_time_tracking;
    ros::Time  last_time_scan;
    ros::Time  last_time_obstacle_received;
    ros::Time  last_time_changed;
    ros::Time  last_time_btn_save_reset_pressed;
    bool changed_setting;
    float duration_change;
    bool low_voltage,lidar_failed;
    int counter_changed,counter_low_voltage,joy_counter,karugamo_counter;
    float min_break_distance,max_break_distance,smooth_accel_side_follow;
    float gain_follow_people;
    float use_ps4_controller,use_hokuyo;
    bool is_navigating,is_arrived_goal,go_wp1,go_wp2;
    int count_arrived;
    bool last_mode_auto;
    bool has_wp1,has_wp2;
    bool reseting_map,saving_map;
    bool danger_back,motors_enabled;
};

int main(int argc, char **argv)
{
    ros::init(argc, argv, "heading_follow_node");
    ros::NodeHandle nh;
    test_head test_head_obj(nh);
    ros::Rate rate(100); 
    for (int i = 1;i < 64; i++){
        test_head_obj.blink_green_sleep(0.2);
    }
    test_head_obj.mode_IDLE();
    while(ros::ok())
    {
        ros::spinOnce();
        test_head_obj.calc_100hz();
        test_head_obj.check_scan_msg();
        test_head_obj.check_people_obsta_msg();
        test_head_obj.check_low_volt();
        rate.sleep();
    }
    return 0;
}
