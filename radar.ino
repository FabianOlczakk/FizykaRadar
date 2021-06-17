#include <Servo.h>

Servo myservo;

const int pingPin = 10;
const int echoPin = 11;

const int red_light_pin= 7;
const int green_light_pin = 5;
const int yellow_light_pin = 6;

const int button = 2;
int mode = 0;
int oldMode = 0;
boolean oldSwitchState = LOW;
boolean newSwitchState = LOW;

int pos = 1;
long duration;
int distance;

int degPerLoop = 1;
int modeDelay = LOW;
boolean loopBreak = LOW;
  
void setup() {
  pinMode(button, INPUT);
  pinMode(red_light_pin, OUTPUT);
  pinMode(green_light_pin, OUTPUT);
  pinMode(yellow_light_pin, OUTPUT);
  Serial.begin(9600);
  myservo.attach(3);
}

void loop() {
  spin();
  }
  
void spin() {
  for (pos = 1; pos <= 170; pos += degPerLoop) {
    modes();
    myservo.write(pos);
    dist(pos);         
    delay(modeDelay);       
  }
  for (pos = 170; pos >= 1; pos -= degPerLoop) {
    modes();
    myservo.write(pos);
    dist(pos);
    delay(modeDelay);
  }
}

void modes() {
  newSwitchState = digitalRead(button);
  if (newSwitchState != oldSwitchState )
  {
    if ( newSwitchState == HIGH )
    {
      mode++;
      if (mode > 4) {
        mode = 0;
      }
      
      switch(mode) {
        case 0:
          degPerLoop = 1;
          modeDelay = 5;
          break;
          
        case 1:
          degPerLoop = 0;
          modeDelay = 1;
          pos = 90;
          break;
          
        case 2:
          degPerLoop = 10;
          modeDelay = 120;
          break;

        case 3:
          degPerLoop = 30;
          modeDelay = 120;
          break
          ;        
      }
    }
    oldSwitchState = newSwitchState;
  }
}

void dist(int pos) {
   long duration, cm;
   pinMode(pingPin, OUTPUT);
   digitalWrite(pingPin, LOW);
   delayMicroseconds(2);
   digitalWrite(pingPin, HIGH);
   delayMicroseconds(10);
   digitalWrite(pingPin, LOW);
   pinMode(echoPin, INPUT);
   duration = pulseIn(echoPin, HIGH);
   cm = microsecondsToCentimeters(duration);
   target(pos, cm);
   delay(10);
}

void target(int pos, long distance) {
  
  if (distance > 200) {
    distance = 0;
  }
    rgb(distance);
    //Serial.print("{\"distance\": ");
    //Serial.print(distance);
    //Serial.print(",");
    //Serial.print("\"angle\": ");
    //Serial.print(pos);
    //Serial.print("}");
    //Serial.println();
    Serial.print(pos);
    Serial.print("*");
    Serial.print(distance);
    Serial.print("#");
  }
  
long microsecondsToCentimeters(long microseconds) {
   return microseconds / 29 / 2;
}

void rgb(int dis) {
  if (dis == 0) {
    dis = 999;
  }
  if (dis <= 40 && dis != 0) {
    digitalWrite(red_light_pin, HIGH);
    digitalWrite(green_light_pin, LOW);
    digitalWrite(yellow_light_pin, LOW);
  } else if (dis > 40 && dis <= 90) {
    digitalWrite(red_light_pin, LOW);
    digitalWrite(green_light_pin, LOW);
    digitalWrite(yellow_light_pin, HIGH);
  } else if (dis > 90) {
    digitalWrite(red_light_pin, LOW);
    digitalWrite(green_light_pin, HIGH);
    digitalWrite(yellow_light_pin, LOW);
  } 
}
