void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
}
void loop() {
  if (Serial.available()) {
    int numero = Serial.parseInt();  
    if (numero >= 0 && numero <= 255) {  
      actualizarLEDs(numero);
    } else {
      Serial.println("Número fuera de rango (0-255)");
    }
  }
}
void actualizarLEDs(int numero) {
  Serial.println(numero);
  digitalWrite(2, (numero >> 0) & 1);
  digitalWrite(3, (numero >> 1) & 1);
  digitalWrite(4, (numero >> 2) & 1);
  digitalWrite(5, (numero >> 3) & 1);
  digitalWrite(6, (numero >> 4) & 1);
  digitalWrite(7, (numero >> 5) & 1);
  digitalWrite(8, (numero >> 6) & 1);
  digitalWrite(9, (numero >> 7) & 1);  
  delay(5000);  
}