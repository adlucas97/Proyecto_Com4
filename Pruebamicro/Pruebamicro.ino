const int pinout = 8; //Salida digital
const int muestra = 10; //Cuenta 20 milisegundos para registrar cuantos 1's fueron sensados
unsigned long milliscurrent; //Milisegundo presente
unsigned long millislast = 0; //Guardar el último tiempo
unsigned long milliselapsed = 0; //Guardar en el tiempo de muestra
int buffer_muestra = 0;// Valores de 1 registrados cada 20 ms

void setup() {
  Serial.begin(9600);
}

void loop() {
  milliscurrent = millis();
  milliselapsed = milliscurrent - millislast;

  if(digitalRead(pinout)== LOW){
    buffer_muestra++;
  }

  if(milliselapsed > muestra){
      Serial.println(buffer_muestra);
      buffer_muestra = 0;
      millislast = milliscurrent;
    }
}
