
int v;

void setup() {
  // put your setup code here, to run once:
  v=0;
  Serial.begin(9600);

  // INPUT = SENSORES
  // OUTPUT = ACTUADORES
}

byte var = 0;

void loop() {
  // put your main code here, to run repeatedly:

  Serial.println("valor:" + String (v));
  v += 1;
  delay(1000);
}
