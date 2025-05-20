String respuesta;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);

  
  // INPUT = SENSORES
  // OUTPUT = ACTUADORES
}


void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0) {
  respuesta = Serial.readString();
  Serial.println(respuesta);
  }
}
