// Bibliotecas

#include <ros.h>
#include <geometry_msgs/Twist.h>
#include <std_msgs/String.h>
#include <roboserv_description/Sensores.h>
#include <Servo.h>
#include <Ultrasonic.h>

#define pinMotor_L 9
#define pinMotor_R 10

#define pinTrig_L  6
#define pinEcho_L  7
#define pinTrig_F  5
#define pinEcho_F  4
#define pinTrig_R  A0
#define pinEcho_R  A1

void setarMotores(const geometry_msgs::Twist&);

Ultrasonic sensor_L (pinTrig_L, pinEcho_L);
Ultrasonic sensor_F (pinTrig_F, pinEcho_F);
Ultrasonic sensor_R (pinTrig_R, pinEcho_R);

Servo motor_L;
Servo motor_R;

ros::NodeHandle nh;

roboserv_description::Sensores dist;
std_msgs::String str_msg;

ros::Publisher sensorPub("distSensors",  &dist);
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
  nh.advertise(sensorPub);
  nh.subscribe(sub);
  float max_vel = 0.2;
  float min_vel = -0.2;
  float max_ang = 1;
  float min_ang = -1;
  float multiplier = 0.3;

  k = 90/(max(max_vel, max_ang * wheel_dist/2) - min(min_vel, min_ang * wheel_dist/2)) * multiplier;
}

float get_dist(int pinTrig, int pinEcho) {
  digitalWrite(pinTrig, LOW);
  delayMicroseconds(2);
  digitalWrite(pinTrig, HIGH);
  delayMicroseconds(10);
  digitalWrite(pinTrig, LOW);
  float duration = pulseIn(pinEcho, HIGH, 20000);
  float distance = duration*0.034/200;
  
  if (distance == 0 || distance > 4 ) { 
    distance = 4;
  }
  return distance;
}

void loop() {
  
  dist.SensorF = get_dist(pinTrig_F, pinEcho_F);
  dist.SensorL = get_dist(pinTrig_L, pinEcho_L);
  dist.SensorR = get_dist(pinTrig_R, pinEcho_R);
  
  sensorPub.publish(&dist);
  
  nh.spinOnce();
  
  delay(100);
}
