#include "ros/ros.h"
#include <std_msgs/String.h>
#include <std_msgs/Int16.h>
#include <std_msgs/Float32.h>
#include <std_msgs/Float64.h>
#include <geometry_msgs/Twist.h>
#include "sensor_msgs/LaserScan.h"
#include <tf/transform_broadcaster.h>
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
	    //light_publisher=nh.advertise<std_msgs::String>(nh.resolveName("manual_control/lights"), 10);
	    //steering_publisher=nh.advertise<std_msgs::Int16>(nh.resolveName("/steering"), 2);
                speed_publisher=nh.advertise<geometry_msgs::Twist>(nh.resolveName("/cmd_vel"), 2);
	        head_subscriber = nh.subscribe("/euler", 1, &test_head::headCallback,this);
		//subTwist_ = nh.subscribe("motor_control/twist",1,&test_head::speedCallback,this); 
		odometry_sub = nh.subscribe("odom",1,&test_head::ReceiveOdometry,this);
		joy_subscriber = nh.subscribe("joy", 3, &test_head::joyCallback,this);
		//subScan_ = nh.subscribe("scan", 1, &test_head::scanCallback,this);
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
	}
	~test_head(){}
	
	void speedCallback(const geometry_msgs::Twist& twist)
	{
	}

    void headCallback(const std_msgs::Float64& head)
	{	
	        sp_yaw=50;
	        //sp_yaw2=-atan2(err_x,err_y)*180/3.1416;
			yaw=head.data;//head.data;//quitamos el offset
			//error_yaw=alfa*error_yaw+(1-alfa)*(sp_yaw-yaw);
			error_yaw=(sp_yaw-yaw);
			float alfan=0.8;
			//err2=err2*alfan+(1-alfan)*atan2(2.5*signo*n_aux2,velx)*180/3.14159;  //0.5*(sp_yaw2-filter_yaw);///(-1*velx);
	        
			if (error_yaw < -180.0 ){
	        	error_yaw=error_yaw+360;
			}else if (error_yaw > 180.0 ){
	        	error_yaw=error_yaw-360;
			}
			float nkp=0.0095;//=0.0085;
			float nkd=0.04;
			float nki=0.002;
			intErr=intErr+error_yaw;
			if(intErr>7){
			  intErr=7;
			}
			if(intErr<-7){
			  intErr=-7;
			}
			ctrl_yaw=(nkp*(error_yaw))-nkd*velyaw+nki*intErr;//+0.5*(error_yaw-last_error));//+0.5*(error_yaw-last_error));//2*(error_yaw);
			
				if(ctrl_yaw<0.06&&ctrl_yaw>-0.06){
				ctrl_yaw=0;
				}
				else if(ctrl_yaw>0.35){
			    		ctrl_yaw=0.35; 
				}else if(ctrl_yaw<-0.35){
					ctrl_yaw=-0.35; 
				}
                                printf("%f,%f \n",ctrl_yaw,intErr);
			        vel_steer.angular.z= ctrl_yaw;
				speed_publisher.publish(vel_steer);	
	}

	void ReceiveOdometry(const nav_msgs::Odometry::ConstPtr& msg){
	    velyaw=msg->twist.twist.angular.z;
            /*px=msg->pose.pose.position.x;
    	    py=msg->pose.pose.position.y;  
    	    filter_yaw=msg->twist.twist.linear.y;
    	    velx=msg->twist.twist.linear.x;
    	    if (ruta_learn==true){
    	    	norm=sqrt((px-px_aux)*(px-px_aux)+(py-py_aux)*(py-py_aux));
    	    	if (norm>0.05){//0.87){
					float newAng=(filter_yaw+90);
					if (newAng < -180.0 ){
	        			newAng=newAng+360;
					}else if (newAng > 180.0 ){
	        			newAng=newAng-360;
					}
					newAng=newAng*3.1416/180;

    	    		fprintf(fp, "%f %f %f %f %f 2 \n",px,py,px-0.4*sin(newAng),py+0.4*cos(newAng),filter_yaw );//ambos carriles mas una bandera 2 para sin cambios
    	    		px_aux=px;
    	    		py_aux=py;
    	    		ROS_INFO("NP %f,%f",px,py);	 
    	    	}
    	    }
    	    count_odo++;
    	    if(count_odo%300==0){
    	    	printf("P%f,%f\n",px,py );
    	    }*/
      }





    void scanCallback(const sensor_msgs::LaserScan::ConstPtr& scan)
	{
	    int count = scan->scan_time / scan->time_increment;
	    float  break_distance_=0.8;
			for(int i = 0; i < (6/2)+1; i++){
				if (scan->ranges[i] <= 0.8){
					ROS_INFO("Obstacle");
					return;
			    }
			}
			for(int k = (360-(6/2)); k < count; k++){
				if (scan->ranges[k] <= 0.8){
					//pubEmergencyStop_.publish(speed);
					ROS_INFO("Obstacle");
					return;
			    }
			}
		
	}


    void loadRoute(){
    	    

    }

    void joyCallback(const sensor_msgs::Joy::ConstPtr& joy)
	{
		
		}

			
		
		
	
private:

    ros::Subscriber head_subscriber;
    ros::Publisher light_publisher;
    std_msgs::String light_command;
    ros::Publisher steering_publisher;
    std_msgs::Int16 steering_command;
    ros::Publisher speed_publisher;
    std_msgs::Int16 speed_command;
	ros::Subscriber subTwist_;
	ros::Subscriber odometry_sub;
	ros::Subscriber joy_subscriber;
	ros::Subscriber subScan_;
        geometry_msgs::Twist vel_steer;
    int ca;
	int direction;
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
float intErr;

};

int main(int argc, char **argv)
{
    ros::init(argc, argv, "heading_follow_node");
    ros::NodeHandle nh; 

    test_head test_head_obj(nh);
    //ros::Rate rate(0.5); //0.5 Hz, every 2 second
	ros::Rate rate(80); //100 Hz, every .01 second
    //printf("%f",-atan2(5,1)*180/3.1416);
	while(ros::ok())
	{
		
		ros::spinOnce();
		rate.sleep();
	}
    return 0;
}
