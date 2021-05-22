#include <Servo.h>

Servo myservo;

const int pingPin = 2;
const int echoPin = 3;

const int red_light_pin= 11;
const int green_light_pin = 10;
const int yellow_light_pin = 9;

const int button = 8;
int mode = 0;
int oldMode = 0;
boolean oldSwitchState = LOW;
boolean newSwitchState = LOW;

int pos = 0;
long duration;
int distance;

int degPerLoop = 1;
boolean modeDelay = LOW;
boolean loopBreak = LOW;

void setup() {
  pinMode(button, INPUT);
  pinMode(red_light_pin, OUTPUT);
  pinMode(green_light_pin, OUTPUT);
  pinMode(yellow_light_pin, OUTPUT);
  Serial.begin(9600);
  myservo.attach(13);
}

void loop() {
  spin();
  }
  
void spin() {
  for (pos = 0; pos <= 172; pos += degPerLoop) {
    modes();
    myservo.write(pos);
    dist(pos);         
    if (modeDelay == HIGH) {
    delay(180);
  } else {
    delay(1);
  }             
  }
  for (pos = 172; pos >= 0; pos -= degPerLoop) {
    modes();
    myservo.write(pos);
    dist(pos);
    if (modeDelay == HIGH) {
    delay(180);
  } else {
    delay(1);
  }
  }
}

void modes() {
  newSwitchState = digitalRead(button);
  if (newSwitchState != oldSwitchState )
  {
    // has the button switch been closed?
    if ( newSwitchState == HIGH )
    {
      if (mode == 1) {
        degPerLoop = 5;
        modeDelay = LOW;
        mode = 2;
      }
      else if (mode == 2) {
        degPerLoop = 10;
        modeDelay = HIGH;
        mode = 3;
      }
      else if (mode == 3) {
        degPerLoop = 20;
        modeDelay = HIGH;
        mode = 4;
      }
      else if (mode == 4) {
        degPerLoop = 20;
        modeDelay = LOW;
        mode = 5;
      }
      else if (mode == 5) {
        degPerLoop = 0;
        modeDelay = LOW;
        pos = 90;
        mode = 6;
      }
      else if (mode == 6) {
        degPerLoop = 1;
        modeDelay = LOW;
        mode = 0;
      }
      else {
        degPerLoop = 3;
        modeDelay = LOW;
        mode = 1;
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
   delay(20);
}

void target(int pos, long distance) {
  //if (distance > 2 && distance < 99) {
    rgb(distance);
    Serial.print("{\"distance\": ");
    Serial.print(distance);
    Serial.print(",");
    Serial.print("\"angle\": ");
    Serial.print(pos);
    Serial.print("}");
    Serial.println();
  //}
  }
  
long microsecondsToCentimeters(long microseconds) {
   return microseconds / 29 / 2;
}

void rgb(int dis) {
  if (dis <= 33) {
    digitalWrite(red_light_pin, HIGH);
    digitalWrite(green_light_pin, LOW);
    digitalWrite(yellow_light_pin, LOW);
  } else if (dis > 33 && dis <= 50) {
    digitalWrite(red_light_pin, LOW);
    digitalWrite(green_light_pin, LOW);
    digitalWrite(yellow_light_pin, HIGH);
  } else if (dis > 50) {
    digitalWrite(red_light_pin, LOW);
    digitalWrite(green_light_pin, HIGH);
    digitalWrite(yellow_light_pin, LOW);
  } 
}
