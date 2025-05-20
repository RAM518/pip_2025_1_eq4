int led =  13;
int dEncendido = 1000;
int dApagado = 500;
void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  // INPUT = SENSORES
  // OUTPUT = ACTUADORES
}

void loop() {
  // put your main code here, to run repeatedly:
  //delay(ms)
  digitalWrite(led, -1);
  delay(dEncendido);
  digitalWrite(led,0);
  delay(dApagado);
   // 1 O TRUE ,HIGH
 
}
