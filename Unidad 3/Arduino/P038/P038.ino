int leds [] =  {10, 11, 12};
String valor ;

void setup() {
  for (int i = 0; i<3; i++){
  pinMode(led, OUTPUT);
  }
  Serial.begin(9600);
  Serial.setTime(100);

}

void loop() {
  if (Serial.available()>0){
    valor = Serial.readString();
    for (int i = 0; i<3; i++){
    digitalWrite(leds [i], valor.charAt(i));
    }
  }
  delay(100);
}
