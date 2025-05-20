int index;
int led1 = 6;
int led2 = 7;
int led3 = 8;
int led4 = 9;
int led5 = 10;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
  pinMode (led1, OUTPUT);
  pinMode (led2, OUTPUT);
  pinMode (led3, OUTPUT);
  pinMode (led4, OUTPUT);
  pinMode (led5, OUTPUT);
  // INPUT = SENSORES
  // OUTPUT = ACTUADORES
}


void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0) {
  index = Serial.readString().toInt();

  pinMode (led1, 0);
  pinMode (led2, 0);
  pinMode (led3, 0);
  pinMode (led4, 0);
  pinMode (led5, 0);

  switch (index){
    case 1:
      digitalWrite(led1, 1);
    case 2:
      digitalWrite(led2, 1);
    case 3:
      digitalWrite(led2, 1);
    case 4:
      digitalWrite(led2, 1);
    case 5:
      digitalWrite(led2, 1);
  }

  }
  delay(100);
}
