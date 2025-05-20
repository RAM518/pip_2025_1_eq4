int led =  0;
int valor ;
void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.setTime(100);
  // put your setup code here, to run once:
  //pinMode(led, OUTPUT);
  // INPUT = SENSORES
  // OUTPUT = ACTUADORES
}

void loop() {
  if (Serial.available()>0){
    valor = Serial.readString().toInt
    digitalWrite(led, valor)
  }
  delay(100);

}
