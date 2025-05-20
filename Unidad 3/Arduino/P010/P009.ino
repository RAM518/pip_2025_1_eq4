int respuesta;
int led = 13;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
  pinMode (led, OUTPUT);
  // INPUT = SENSORES
  // OUTPUT = ACTUADORES
}


void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0) {
  respuesta = Serial.readString().toInt();

  digitalWrite(led, respuesta);

  }
  delay(100);
}
