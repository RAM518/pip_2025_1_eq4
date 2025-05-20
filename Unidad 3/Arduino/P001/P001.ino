int led =  13;
int contador ;
void setup() {
  Serial.begin(9600);
  contador=0;
  // put your setup code here, to run once:
  //pinMode(led, OUTPUT);
  // INPUT = SENSORES
  // OUTPUT = ACTUADORES
}

void loop() {
  Serial.println("Alumno:"+String(contador++));
  delay(1000);

}
