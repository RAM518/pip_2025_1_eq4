int led =  13;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  // INPUT = SENSORES
  // OUTPUT = ACTUADORES
}

void loop() {
  // put your main code here, to run repeatedly:
  //delay(ms)
  delay(500);
  digitalWrite(led, -1);
  delay(500);
  digitalWrite(led,0);
   // 1 O TRUE ,HIGH
 
}
