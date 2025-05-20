
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  // INPUT = SENSORES
  // OUTPUT = ACTUADORES
}

byte var = 0;

void loop() {
  // put your main code here, to run repeatedly:
 Serial.println(var);
  delay(1000);
}
