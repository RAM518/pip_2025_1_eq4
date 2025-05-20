#include <Servo.h>
Servo serv;
int pot=A0;
void setup() {
 //No comunicacion serial, no Serial.Begin
  //Hz: Cantidad de veces que hace un ciclo en un segundo
  serv.attach(10);
}


void loop() {
  int v= analogRead(pot);
  v=map(v, 0, 1023, 0, 180);
  serv.write(v);
  delay(30);

}
