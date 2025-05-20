/* int valores[3]={0,0,0}; 
int sensores[3]={A1,A2,A3}; */
int led=13;
void setup() {
  pinMode(led,OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(100);
}

String cadena;
char *c;
char *token;

void loop() {
  if (Serial.available()>0){
    //100R567R041
    cadena= Serial.readString();
    c = cadena.c_str();

    Serial.println("Cadena Completa: ");
    Serial.println(c);

    token = strtok(c,"R"); //Tokeniza la cadena
    //digitalWrite(led,cadena);
    while(token != NULL){
      Serial.println(token);
      token= strtok(NULL,"R");
    }


    Serial.println("Acceso a la ubicacion de los tokens");
    Serial.println(&c[0]);
    Serial.println(&c[4]);
    Serial.println(&c[8]);

    Serial.print("cadena despues de tokenizar: "); 
    Serial.println(c);



  }   
 
}

