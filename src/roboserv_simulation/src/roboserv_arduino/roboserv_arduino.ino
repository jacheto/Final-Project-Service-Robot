// Bibliotecas

#include <ros.h>
#include <geometry_msgs/Twist.h>
#include <roboserv_description/Sensores.h>
#include <Servo.h>
#include <Ultrasonic.h>

#define pinMotor_L 9
#define pinMotor_R 10

#define pinTrig_L  6
#define pinEcho_L  7
#define pinTrig_FL 3
#define pinEcho_FL 2
#define pinTrig_F  5
#define pinEcho_F  4
#define pinTrig_FR A4
#define pinEcho_FR A5
#define pinTrig_R  A0
#define pinEcho_R  A1

void setarMotores(const geometry_msgs::Twist&);

Ultrasonic sensor_L (pinTrig_L, pinEcho_L);
Ultrasonic sensor_FL(pinTrig_FL, pinEcho_FL);
Ultrasonic sensor_F (pinTrig_F, pinEcho_F);
Ultrasonic sensor_FR(pinTrig_FR, pinEcho_FR);
Ultrasonic sensor_R (pinTrig_R, pinEcho_R);

Servo motor_L;
Servo motor_R;

ros::NodeHandle nh;
roboserv_description::Sensores dist;

ros::Publisher sensorPub("distSensors",  &dist);
ros::Subscriber<geometry_msgs::Twist> sub("cmd_vel_gate", setarMotores);

void setarMotores(const geometry_msgs::Twist& vel){
}

void setup() {
  motor_L.attach(pinMotor_L);
  motor_R.attach(pinMotor_R);
  nh.initNode();
  nh.advertise(sensorPub);
}

void loop() {
  
  long timing_L = sensor_L.timing();
  long timing_FL = sensor_FL.timing();
  long timing_F = sensor_F.timing();
  long timing_FR = sensor_FR.timing();
  long timing_R = sensor_R.timing();
  
  motor_L.write(90);
  motor_R.write(90);
  
  dist.SensorL  = sensor_L.convert(timing_L,   Ultrasonic::CM)/100;
  dist.SensorFL = sensor_FL.convert(timing_FL, Ultrasonic::CM)/100;
  dist.SensorF  = sensor_F.convert(timing_F,   Ultrasonic::CM)/100;
  dist.SensorFR = sensor_FR.convert(timing_FR, Ultrasonic::CM)/100;
  dist.SensorR  = sensor_R.convert(timing_R,   Ultrasonic::CM)/100;
  
  sensorPub.publish(&dist);
  
  nh.spinOnce();
  
  delay(200);
  
}
