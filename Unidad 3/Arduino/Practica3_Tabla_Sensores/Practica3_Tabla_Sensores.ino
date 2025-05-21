#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();

  Serial.println("=======================");
  Serial.println("---- SENSOR DHT11 ----");
  Serial.println("=======================");
  Serial.println("Humedad (%)\tTemperatura (°C)");
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  Serial.print(h);
  Serial.print("\t");
  Serial.println(t);

  delay(2000);
}

