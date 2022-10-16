# BALL AND BEAM SYSTEM 
   This project will focus on designing a controller so that the ball’s position can be manipulated for the ball - plate system.

## Prequities 
- Learn about Open loop and closed loop systems 
- learn about PID controllers 
- Learn how to use the Dynamics to plot the Error-time ot Position- desired postion graph


## ROADMAP

- Find the values of proportional , integral & derivatives errors from the Dynamics of the equation  
- Get the actuator equation using PID equation 
- Make sure that the tuning parameters you choose give the system a rise timeof about 3 seconds and maximum overshoot of less than 5%.
- Use Aurdino UNO & Servo motor & Sound detection sensors for the project 
- 


## Code

```javascript
BALL AND BEAM 

#include <Servo.h>
Servo s;
const int echo=2;
const int trig=3;
const int servo=6;
float d=0;
float t=0;
float y=0;
const float kp=5;
const float kd=10;
const float ki=0;
float u=0;
float e=0;
float ei=0;
float ed=0;
float eo=0;
const float r=20;
float dt=0.1;
float up;
float down;



  
void setup() {
  pinMode(echo,INPUT);
  pinMode(trig,OUTPUT);
  s.attach(servo);
  s.write(55);
  Serial.begin(9600);
  
  
  
}

void loop() {
  digitalWrite(trig,LOW);
  delayMicroseconds(1);
  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,HIGH);
  t=pulseIn(echo,HIGH);
  
  d=t*0.017;
  if(d>34){
    d=34;
  }
  if(d<6){
    d=6;
  }
  up=34*kp;
  down=6*kp;
  e=r-d;
  ei=ei+(e*dt);
  ed=(e-eo)/dt;
  u=kp*e+ki*ei+kd*ed;
  Serial.println(d);
  //Serial.println();

  if(d<=17 or d>=23){
    y=map(u,1014,-1074,25,85);
  }
  if(d>17 or d<23){
    y=map(u,1014*2.5,-1074*2.5,25,85);
  }
  
  if(y<20){
    y=20;
  }
  if(y>90){
    y=90;
  }
  //Serial.println(y);
  
  s.write(y);
  
  
  

}
```

