// Bibliotecas

#include <ros.h>
#include <geometry_msgs/Twist.h>
#include <std_msgs/String.h>
#include <roboserv_description/Sensores.h>
#include <Servo.h>
#include <Ultrasonic.h>

// R  S  L
// RF F LF

#define pinMotor_L 9
#define pinMotor_R 10

#define pinTrig_F  5
#define pinEcho_F  4

#define pinTrig_L  6
#define pinEcho_L  7

#define pinTrig_R  A0
#define pinEcho_R  A1

#define pinTrig_T  A2
#define pinEcho_T  A3

void setarMotores(const geometry_msgs::Twist&);

Ultrasonic sensor_F (pinTrig_F, pinEcho_F);
Ultrasonic sensor_L (pinTrig_L, pinEcho_L);
Ultrasonic sensor_R (pinTrig_R, pinEcho_R);
Ultrasonic sensor_T (pinTrig_T, pinEcho_T);

Servo motor_L;
Servo motor_R;

ros::NodeHandle nh;

roboserv_description::Sensores dist;
std_msgs::String str_msg;

ros::Publisher sensorPub("distSensors",  &dist);
ros::Subscriber<geometry_msgs::Twist> sub("cmd_vel_gate", setarMotores);

float wheel_dist = 0.38;


void setarMotores(const geometry_msgs::Twist& vel){
  
  int vel_L = (int) (90 - 90 * (vel.linear.x - vel.angular.z * wheel_dist/2) );
  int vel_R = (int) (90 - 90 * (vel.linear.x + vel.angular.z * wheel_dist/2) );
  if (vel_L < 0)    vel_L = 0;
  if (vel_L > 180)  vel_L = 180;
  if (vel_R < 0)    vel_R = 0;
  if (vel_R > 180)  vel_R = 180;
  
  motor_L.write(vel_L);
  motor_R.write(vel_R);
}

void setup() {
  motor_L.attach(pinMotor_L);
  motor_R.attach(pinMotor_R);
  nh.initNode();
  nh.advertise(sensorPub);
  nh.subscribe(sub);
}

float get_dist(int pinTrig, int pinEcho) {
  digitalWrite(pinTrig, LOW);
  delayMicroseconds(2);
  digitalWrite(pinTrig, HIGH);
  delayMicroseconds(10);
  digitalWrite(pinTrig, LOW);
  long t0 = micros();
  long max_time_us = 10000;
  float duration = pulseIn(pinEcho, HIGH, max_time_us);
  float distance = duration*0.034/200;
  
  if (distance == 0 || distance > 4 ) { 
    distance = 4;
  }
  long t1 = micros();
  
  long t_restante = max_time_us - (t1 - t0);
  if(t_restante > 0){
    delayMicroseconds(max_time_us - (t1 - t0));
  }
  return distance;
}

void loop() {
  
  dist.SensorF = get_dist(pinTrig_F, pinEcho_F);
  dist.SensorL = get_dist(pinTrig_L, pinEcho_L);
  dist.SensorR = get_dist(pinTrig_R, pinEcho_R);
  //dist.SensorT = get_dist(pinTrig_T, pinEcho_T);
  
  sensorPub.publish(&dist);
  
  nh.spinOnce();
  
  delay(100);
}
