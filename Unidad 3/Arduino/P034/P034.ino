int pot =  A0;
int valor ;
void setup() {
  Serial.begin(9600);

  // put your setup code here, to run once:
  //pinMode(led, OUTPUT);
  // INPUT = SENSORES
  // OUTPUT = ACTUADORES
}

void loop() {
  Valor = analogRead(pot);
  Serial.println(valor)
  delay(250);

}
