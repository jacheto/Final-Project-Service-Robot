// Bibliotecas

#include <ros.h>
#include <geometry_msgs/Twist.h>
#include <Servo.h>

#define pinMotor_L 9
#define pinMotor_R 10

void setarMotores(const geometry_msgs::Twist&);

Servo motor_L;
Servo motor_R;

ros::NodeHandle nh;


ros::Subscriber<geometry_msgs::Twist> sub("cmd_vel_gate", setarMotores);

float k;
float wheel_dist = 0.38;

void setarMotores(const geometry_msgs::Twist& vel){
  
  int vel_L = (int) (90 - (vel.linear.x - vel.angular.z * wheel_dist/2) * k);
  int vel_R = (int) (90 - (vel.linear.x + vel.angular.z * wheel_dist/2) * k);

  motor_L.write(vel_L);
  motor_R.write(vel_R);
}

void setup() {
  motor_L.attach(pinMotor_L);
  motor_R.attach(pinMotor_R);
  nh.initNode();
  nh.subscribe(sub);
  float max_vel = 0.2;
  float min_vel = -0.2;
  float max_ang = 1;
  float min_ang = -1;
  float multiplier = 0.3;

  k = 90/(max(max_vel, max_ang * wheel_dist/2) - min(min_vel, min_ang * wheel_dist/2)) * multiplier;
}

void loop() {
  nh.spinOnce();
  
  
}
