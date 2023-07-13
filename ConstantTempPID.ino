// This program was written by Francisco Sebstiano -- https://ciscosebas9.wixsite.com/francisco-sebastiano
// MIT License

#include <Servo.h>

Servo myservo;

int wirePin = A1; //parallel -- pin for checking the temp of the wire
int waterPin = A4; //series -- pin for checking the temp of the water

unsigned long startMillis; //an updatable value for milliseconds since the last cycle of some timed process
unsigned long currentMillis; //an updatable value for the number of milliseconds since the program started running
const unsigned long period = 5000; //the number of milliseconds that the timed process will take

//int pwmPin = 10; // The pin which sends control signals to the heated wire which modulate the amount of current flowing through the wire. 
//int motorDirec1 = 6; //A pin which is brought low to send current through the heated wire
//int motorDirec2 = 7; //A pin which is brought high to send current through the heated wire. pin 6 must be low and pin 7 must be high simultaneously for current to go through the wire.


int setPoint = 500; // resitance value asssociated with 50 degrees celsius, the set point of the wire
int wireTemp; //variable for temperature of the wire
int raw; // variable for the raw outputs of the wire temp voltage divider
float output; // variable for the pwm value that drives the heated wire

//Below are the PID coefficients, kp, ki. kd. They are used to tune the controller.
float kP = 4; 
float kI = 0;
float kD = 0;

//a bunch of variables which store the values of different functions
float errorFunction = 0;
float lastErrorFunction = 0;
float integral = 0;
float derivative = 0;
float proportionate = 0;


float dt = 5; // the update rate for the PID system, dt, difference in time

void setup() {
  // put your setup code here, to run once:

  myservo.attach(5);

  // assign pin functions
  pinMode(wirePin, INPUT);
  pinMode(waterPin, INPUT);
  //pinMode(motorDirec2, OUTPUT);
  //pinMode(motorDirec1, OUTPUT);
  //pinMode(pwmPin, OUTPUT);
  Serial.begin(9600);
  startMillis = millis(); //initiate millisecond count

}

void loop() {
  // put your main code here, to run repeatedly:

  // turn on the wire heating system
  //digitalWrite(motorDirec2, LOW);
  //digitalWrite(motorDirec1, HIGH); 

  // calculate temperature of wire
  wireTemp = analogRead(wirePin);
  //wireTemp = (raw*45000)/(1024-raw);
  //Serial.println(wireTemp);
  //Serial.print(" ");
  //Serial.println(analogRead(waterPin));

  // Calculate the error function, Derivative, and Integral 
  errorFunction = wireTemp - setPoint;
  integral = (integral + errorFunction)*kI;
  //Serial.print("hi");
  derivative = lastErrorFunction - errorFunction;
  derivative = derivative/dt;
  derivative = derivative*kD;
  proportionate = errorFunction*kP;
  lastErrorFunction = errorFunction;
  delay(dt*1000);
 
  output = proportionate + integral + derivative; //calculates the output and sends output pwm value to the heated wire driver. 
  //Serial.println(output);
  if (output > 180){
    output = 180;
  }
  if (output < 0){
    output = 0;
  }
  //analogWrite(pwmPin, output);
  myservo.write(output);

  // This function prints the raw temperature reading values of the wire and water every 1 second. 
  currentMillis = millis();
  if (currentMillis - startMillis >= period)
  {
    Serial.print(analogRead(wirePin));
    Serial.print(" ");
    Serial.println(analogRead(waterPin));
    //Serial.println(output);
    startMillis = currentMillis;
  }

}
