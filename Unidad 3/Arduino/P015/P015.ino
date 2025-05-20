int potenciometro=A0; //A0 - A5
int led=6;
void setup() {
 //No comunicacion serial, no Serial.Begin
  //Hz: Cantidad de veces que hace un ciclo en un segundo
}


void loop() {

  for(int i = 0; i<60 ; i++){
    analogWrite(led,i);
    delay(10);
  }
  for(int i = 60; i>0 ; i--){
    analogWrite(led,i);
    delay(10);
  }

  //int v=analogRead(pot);
  //analogWrite(led,)


}
