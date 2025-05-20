int valores[3]=(0,0,0);
int led=13;
int sensores[3]=(A1,A2,A3);
void setup() {


  piMode(led,OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(100);
}

void loop() {
  val = analogRead(sensor);
  for (int i=0, i<3, i++){
    valores[i]=analogRead(sensores[i]);
    cadena += String(valores[i]) + "-";
  }   

  Serial.println(cadena);

  if (Serial.available()>0){
    int v  Serial.readString().toInt();
    digitalWrite(led,v);

  }

}

