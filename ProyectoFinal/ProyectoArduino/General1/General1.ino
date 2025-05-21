#include <DHT.h>

// Definición de pines y constantes
// Sensor DHT11
#define DHTPIN 2
#define DHTTYPE DHT11
#define TRANSISTOR_PIN 8  //controla la base del transistor

// Sensor LDR
const int ldrPin = A0;
const int ldrLed1 = 11;
const int ldrLed2 = 6;
int ldrValue = 0;
int thresholdOn = 850;
int thresholdOff = 850;
bool ledsState = false;

// Sensor ultrasónico
const int trigPin = 9;
const int echoPin = 10;
const int alarmLed1 = 13;
const int alarmLed2 = 12;
const int buzzerPin = 7;

// Variables globales
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // Inicialización serial
  Serial.begin(9600);
  
  // Inicialización DHT11
  dht.begin();
  
  // Configuración de pines
  // Para LDR
  pinMode(ldrLed1, OUTPUT);
  pinMode(ldrLed2, OUTPUT);
  
  // Para transistor que controla el motor
  pinMode(TRANSISTOR_PIN, OUTPUT);
  digitalWrite(TRANSISTOR_PIN, LOW); // Aseguramos que inicia apagado
  
  // Para ultrasónico
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(alarmLed1, OUTPUT);
  pinMode(alarmLed2, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  
  Serial.println("Sistema integrado iniciado - Motor en circuito externo 9V");
}

void loop() {

  processTemperature();
  
  processLDR();
  
  processUltrasonic();
  
  delay(100); 
}

void processTemperature() {
  static unsigned long lastCheck = 0;
  const unsigned long interval = 2000; 
  
  if (millis() - lastCheck >= interval) {
    lastCheck = millis();
    
    float humedad = dht.readHumidity();
    float temperatura = dht.readTemperature();

    if (isnan(humedad) || isnan(temperatura)) {
      Serial.println("¡Error al leer el sensor DHT11!");
      return;
    }
    Serial.print("Humedad: ");
    Serial.print(humedad);
    Serial.print("%\t");
    Serial.print("Temperatura: ");
    Serial.print(temperatura);
    Serial.println("°C");

    // Controlamos el transistor, no el motor directamente
    if (temperatura > 27.0) {
      digitalWrite(TRANSISTOR_PIN, HIGH);
      Serial.println("Motor ACTIVADO (Transistor ON)");
    } else {
      digitalWrite(TRANSISTOR_PIN, LOW);
      Serial.println("Motor DESACTIVADO (Transistor OFF)");
    }
  }
}

void processLDR() {
  static unsigned long lastCheck = 0;
  const unsigned long interval = 100; 
  
  if (millis() - lastCheck >= interval) {
    lastCheck = millis();
    
    ldrValue = analogRead(ldrPin);
    Serial.print("LDR: ");
    Serial.println(ldrValue);

    if (ldrValue < thresholdOn && !ledsState) {
      digitalWrite(ldrLed1, HIGH);
      digitalWrite(ldrLed2, HIGH);
      ledsState = true;
      Serial.println("Encendiendo LEDs por LDR");
    } 
    else if (ldrValue > thresholdOff && ledsState) {
      digitalWrite(ldrLed1, LOW);
      digitalWrite(ldrLed2, LOW);
      ledsState = false;
      Serial.println("Apagando LEDs por LDR");
    }
  }
}

void processUltrasonic() {
  static unsigned long lastCheck = 0;
  const unsigned long interval = 200; // Cada 200ms
  
  if (millis() - lastCheck >= interval) {
    lastCheck = millis();
    
    // Medición de distancia
    long duration, distance;
    
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    
    duration = pulseIn(echoPin, HIGH);
    distance = duration * 0.0343 / 2;
    

    if (distance <= 5 && distance > 0) {
      // Secuencia intermitente (LEDs + Buzzer ON/OFF cada 200ms)
      static bool alarmState = false;
      alarmState = !alarmState;
      
      digitalWrite(alarmLed1, alarmState);  
      digitalWrite(alarmLed2, alarmState);  
      digitalWrite(buzzerPin, alarmState);  
      
      Serial.println("¡Alerta! Objeto detectado");
    } else {
      digitalWrite(alarmLed1, LOW);     
      digitalWrite(alarmLed2, LOW);     
      digitalWrite(buzzerPin, LOW);    
    }
    
    Serial.print("Distancia: ");
    Serial.print(distance);
    Serial.println(" cm");
  }
}