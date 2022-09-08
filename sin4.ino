// analog-plot
// 
// Read analog values from A0 and A1 and print them to serial port.
//
// electronut.in
 
#include "Arduino.h"
 
void setup()
{
  // initialize serial comms
  Serial.begin(9600); 
}
int i=0;
float x;
float pi=3.1415927;
void loop()
{
  if (i==99) i=0;
  x=pi*float(i)/50.0;
  float val1 = sin(x);
  float val2 = sin(pi/4.0+x);
  float val3 = sin(pi/2.0+x);
  float val4 = sin(3.0*pi/4.0+x);
  i=i+1;
// print to serial
  Serial.print(val1);
  Serial.print(", ");
  Serial.print(val2);
  Serial.print(", ");
  Serial.print(val3);
  Serial.print(", ");
  Serial.print(val4);
  Serial.print("\n");
  // wait 
  delay(100);
}
