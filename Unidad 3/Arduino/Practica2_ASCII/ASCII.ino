
String palabra = "";

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
    palabra = Serial.readString();
    Pbina(palabra);  // Mostrar cada letra en binario
  }
}

void Pbina(String palabra) {
  palabra.trim();
  
  for (int i = 0; i < palabra.length(); i++) {  // Recorre cada carácter de la palabra
    char caracter = palabra.charAt(i);  // Obtiene un carácter de la palabra
    int numero = int(caracter);  // Convierte el carácter a su código ASCII (decimal)
    
    Serial.print("Mostrando letra: ");
    Serial.println(caracter);
    Serial.print("Código ASCII (decimal): ");
    Serial.println(numero);

    actualizarLEDs(numero);
    delay(5000); 
    apagarLEDs();
    delay(2000); 
  }
}

void actualizarLEDs(int numero) {
  digitalWrite(2, (numero >> 0) & 1);
  digitalWrite(3, (numero >> 1) & 1);
  digitalWrite(4, (numero >> 2) & 1);
  digitalWrite(5, (numero >> 3) & 1);
  digitalWrite(6, (numero >> 4) & 1);
  digitalWrite(7, (numero >> 5) & 1);
  digitalWrite(8, (numero >> 6) & 1);
  digitalWrite(9, (numero >> 7) & 1);


}

void apagarLEDs() {
  for (int pin = 2; pin <= 9; pin++) {
    digitalWrite(pin, LOW);
  }
}