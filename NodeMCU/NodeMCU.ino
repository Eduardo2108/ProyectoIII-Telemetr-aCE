/*
Codigo Tercer proyecto Taller de Programacion
Eduardo Zumbado Granados
Jose Andres Rodriguez

**Carrito miedo**

 */
#include <ESP8266WiFi.h>

//Cantidad maxima de clientes es 1
#define MAX_SRV_CLIENTS 1
//Puerto por el que escucha el servidor
#define PORT 7070

/*
 * ssid: Nombre de la Red a la que se va a conectar el Arduino
 * password: Contraseña de la red
 * 
 * Este servidor no funciona correctamente en las redes del TEC,
 * se recomienda crear un hotspot con el celular
 */
const char* ssid = "WifiOfCar";
const char* password = "12345678";


// servidor con el puerto y variable con la maxima cantidad de 

WiFiServer server(PORT);
WiFiClient serverClients[MAX_SRV_CLIENTS];

/*
 * Intervalo de tiempo que se espera para comprobar que haya un nuevo mensaje
 */
unsigned long previousMillis = 0, temp = 0;
const long interval = 100;

/*
 * Pin donde está conectado el sensor de luz
 * Señal digital, lee 1 si hay luz y 0 si no hay.
 */
#define ldr D7

//pin del lector de bateria
#define battery A0

/**
 * Variables para manejar las luces con el registro de corrimiento.
 * Utilizan una función propia de Arduino llamada shiftOut.
 * shiftOut(ab,clk,LSBFIRST,data), la función recibe 2 pines, el orden de los bits 
 * y un dato de 8 bits.
 * El registro de corrimiento tiene 8 salidas, desde QA a QH. Nosotros usamos 6 de las 8 salidas
 * Ejemplos al enviar data: 
 * data = B00000000 -> todas encendidas
 * data = B11111111 -> todas apagadas
 * data = B00001111 -> depende de LSBFIRST o MSBFIRST la mitad encendida y la otra mitad apagada
 */
#define ab  D6 
#define clk D8
/*
 * Parte del codigo que controla los motores..
 * #FUE CAMBIADA: debido a problemas con el L298, se uso un modulo de dos L91100S
 * 
 * Motor A:
 * A_IA ^ A_IB ----> controlan el motor A (direccion)
 * 1^0 --> derecha
 * 0^1 --> izquierda
 * 0^0 --> avanzar directo.
 * 
 * Motor B:
 * B_IA ^ B_IB ----> controlan el motor B (Principal)
 * 1^0 --> Adelante
 * 0^1 --> Atras
 * 0^0 --> Free run.
 */
#define A_IA D1 // PIN A, MOTOR A
#define A_IB D2 // PIN B, MOTOR A
 
#define B_IA D3 // PIN A, MOTOR B
#define B_IB D4 // PIN B, MOTOR B
 



/**
 * Función de configuración.
 * Se ejecuta la primera vez que el módulo se enciende.
 * Si no puede conectarse a la red especificada entra en un ciclo infinito 
 * hasta ser reestablecido y volver a llamar a la función de setup.
 * La velocidad de comunicación serial es de 115200 baudios, tenga presente
 * el valor para el monitor serial.
 */
void setup() {
  Serial.begin(115200);
  pinMode(A_IA,OUTPUT);
  pinMode(A_IB,OUTPUT);
  pinMode(B_IA,OUTPUT);
  pinMode(B_IB ,OUTPUT);
  pinMode(clk,OUTPUT);
  pinMode(ab,OUTPUT);
 //Inputs  
  pinMode(ldr,INPUT);
  pinMode(battery, INPUT);

  // ip estática para el servidor
  IPAddress ip(192,168,43,200);
  IPAddress gateway(192,168,43,1);
  IPAddress subnet(255,255,255,0);

  WiFi.config(ip, gateway, subnet);

  // Modo para conectarse a la red
  WiFi.mode(WIFI_STA);
  // Intenta conectar a la red
  WiFi.begin(ssid, password);
  
  uint8_t i = 0;
  while (WiFi.status() != WL_CONNECTED && i++ < 20) delay(500);
  if (i == 21) {
    Serial.print("\nCould not connect to: "); Serial.println(ssid);
    while (1) delay(500);
  } else {
    Serial.println("\nIt´s connected");
  }
  server.begin();
  server.setNoDelay(true);


}

/*
 * Función principal que llama a las otras funciones y recibe los mensajes del cliente
 * Esta función comprueba que haya un nuevo mensaje y llama a la función de procesar
 * para interpretar el mensaje recibido.
 */
void loop() {
  
  unsigned long currentMillis = millis();
  uint8_t i;
  //check if there are any new clients
  if (server.hasClient()) {
    for (i = 0; i < MAX_SRV_CLIENTS; i++) {
      //find free/disconnected spot
      if (!serverClients[i] || !serverClients[i].connected()) {
        if (serverClients[i]) serverClients[i].stop();
        serverClients[i] = server.available();
        continue;
      }
    }
    //no free/disconnected spot so reject
    WiFiClient serverClient = server.available();
    serverClient.stop();
  }

  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    for (i = 0; i < MAX_SRV_CLIENTS; i++) {
      // El cliente existe y está conectado
      if (serverClients[i] && serverClients[i].connected()) {
        // El cliente tiene un nuevo mensaje
        if(serverClients[i].available()){
          // Leemos el cliente hasta el caracter '\r'
          String mensaje = serverClients[i].readStringUntil('\r');
          // Eliminamos el mensaje leído.
          serverClients[i].flush();
          
          // Preparamos la respuesta para el cliente
          String respuesta; 
          procesar(mensaje, &respuesta);
          Serial.println(mensaje);
          // Escribimos la respuesta al cliente.
          serverClients[i].println(respuesta);
        }  
        serverClients[i].stop();
      }
    }
  }
}

/*
 * Función para dividir los comandos en pares llave, valor
 * para ser interpretados y ejecutados por el Carro
 * Un mensaje puede tener una lista de comandos separados por ;
 * Se analiza cada comando por separado.
 * Esta función es semejante a string.split(char) de python
 * 
 */
void procesar(String input, String * output){
  //Buscamos el delimitador ;
  Serial.println("Checking input....... ");
  int comienzo = 0, delComa, del2puntos;
  bool result = false;

  delComa = input.indexOf(';',comienzo);
  
  while(delComa>0){
    String comando = input.substring(comienzo, delComa);
    Serial.print("Processing comando: ");
    Serial.println(comando);
    del2puntos = comando.indexOf(':');
    /*
    * Si el comando tiene ':', es decir tiene un valor
    * se llama a la función exe 
    */
    if(del2puntos>0){
        String llave = comando.substring(0,del2puntos);
        String valor = comando.substring(del2puntos+1);

        Serial.print("(llave, valor) = ");
        Serial.print(llave);
        Serial.println(valor);
        //Una vez separado en llave valor 
        *output = implementar(llave,valor); 
    }
    else if(comando == "sense"){
      *output = getbattery();  
    }  
     
    /**
     * ## AGREGAR COMPARACIONES PARA COMANDOS SIN VALOR
     * EJEM: comando == CIRCLE; 
     */
    comienzo = delComa+1;
    delComa = input.indexOf(';',comienzo);
  }
}

String implementar(String llave, String valor){
  /**
   * La variable result puede cambiar para beneficio del desarrollador
   * Si desea obtener más información al ejecutar un comando.
   */
  String result="ok;";
  Serial.print("Comparing llave: ");
  
  Serial.print(llave);
  
  if(llave == "pwm"){
  
    if(valor.toInt() > 0){
      analogWrite(B_IA, valor.toInt());
      digitalWrite(B_IB, LOW);
    }
      if(valor.toInt() < 0){
        int pwm = -1*(valor.toInt());
        analogWrite(B_IB, pwm);
        digitalWrite(B_IA, LOW);
      }
      if (valor.toInt() == 0){
        digitalWrite(B_IB, LOW);
        digitalWrite(B_IA, LOW);
      }
    }    
  else if(llave == "especial"){
    Serial.print("SPECIAL MOVE");
    //Go back
    Serial.println("go back");
    analogWrite(B_IB, 1023);
    digitalWrite(B_IA, LOW);
    //Turn left
    Serial.println("turn left");
    digitalWrite(A_IA, LOW);
    digitalWrite(A_IB, HIGH);
    delay(1000);//hold on a second
    //Turn Right
    Serial.println("turn right");
    digitalWrite(A_IA, HIGH);
    digitalWrite(A_IB, LOW);
    delay(1000);
    //Turn left
    Serial.println("turn left");
    digitalWrite(A_IA, LOW);
    digitalWrite(A_IB, HIGH);
    delay(1000);//hold on a second
    //Turn Right
    Serial.println("turn right");
    digitalWrite(A_IA, HIGH);
    digitalWrite(A_IB, LOW);
    delay(1000);

    // ENDS UP
    Serial.println("done");
    digitalWrite(A_IA, LOW);
    digitalWrite(A_IB, LOW);
    digitalWrite(B_IB, LOW);
    digitalWrite(B_IA, LOW);
    

  }
  else if(llave == "celebra"){
    Serial.println("CELEBRATE MOVE");
    //GO FORWARD AND LEFT
    digitalWrite(A_IA, LOW);
      digitalWrite(A_IB, HIGH);
        analogWrite(B_IA, 1023);
          digitalWrite(B_IB, LOW);
            delay(1000);
    
    //GO BACK AND RIGHT
    digitalWrite(A_IA, HIGH);
      digitalWrite(A_IB, LOW);
        analogWrite(B_IB, 1023);
           digitalWrite(B_IA, LOW);
              delay(1000);
    
    //GO FORWARD AND LEFT
    digitalWrite(A_IA, LOW);
      digitalWrite(A_IB, HIGH);
        analogWrite(B_IA, 1023);
          digitalWrite(B_IB, LOW);
              delay(1000);
    
    //GO BACK AND RIGHT
    digitalWrite(A_IA, HIGH);
      digitalWrite(A_IB, LOW);
        analogWrite(B_IB, 1023);
          digitalWrite(B_IA, LOW);
            delay(1000);

     //END
         Serial.println("done");
    digitalWrite(A_IA, LOW);
    digitalWrite(A_IB, LOW);
    digitalWrite(B_IB, LOW);
    digitalWrite(B_IA, LOW);
  }
  else if(llave == "dir"){
   Serial.println(" Girando");
   if (valor.toInt() == 1){
    digitalWrite(A_IA, HIGH);
    digitalWrite(A_IB, LOW);
   }
   if (valor.toInt() == -1){
    digitalWrite(A_IA, LOW);
    digitalWrite(A_IB, HIGH);
   }
    if (valor.toInt() == 0){
    digitalWrite(A_IA, LOW);
    digitalWrite(A_IB, LOW);
   }
  }
  else if(llave[0] == 'l'){
    Serial.println("Cambiando Luces");
    Serial.print("valor luz: ");
    Serial.println(valor);
    
    byte data = B11111111;
    byte dataux = B11111111;
    //Recomendación utilizar operadores lógico de bit a bit (bitwise operators)
    switch (llave[1]){
      case 'f':
        if (valor.toInt() == 1){
         Serial.println("Luces frontales");
          dataux = B00111111;
        }
        else{
          dataux = B11111111;
        }
        case 'e':
        if (valor.toInt() == 1){
           Serial.println("Luces emergencia");
          dataux = B11001111;
        }
        else{
          dataux = B11111111;
        }
        //Serial.println("Luces Emergencia");
        break;
      case 'b':
      
        if (valor.toInt() == 1){
          Serial.println("Luces traseras");
          dataux = B11110011;
        }
        else{
          dataux = B11111111;
        }
        
        break;
      case 'l':
        if (valor.toInt() == 1){
          Serial.println("Luces izquierda");
          dataux = B11011111;
        }
        else{
          dataux = B11111111;
        }
        
        break;
      case 'r':
        if (valor.toInt() == 1){
          Serial.println("Luces derechas");
          dataux = B11101111;
        }
        else{
          dataux = B11111111;
        }
        //
        break;
        /*6
       * # AGREGAR CASOS CON EL FORMATO l[caracter]:valor;
       * SI SE DESEAN manejar otras salidas del registro de corrimiento
       */
      default:
        Serial.println("Ninguna de las anteriores");  
        break;
    }
    //data VARIABLE QUE DEFINE CUALES LUCES SE ENCIENDEN Y CUALES SE APAGAN
    //Serial.println(dataux);
    
    shiftOut(ab, clk, LSBFIRST,dataux);
    //shiftOut(ab, clk, LSBFIRST, dataux);
  }
   
  /**
   * El comando tiene el formato correcto pero no tiene sentido para el servidor
   */
  else{
    result = "Undefined key value: " + llave+";";
    Serial.println(result);
  }
  return result;
}

/**
 * Función para obtener los valores de telemetría del auto
 */
int getbattery(){
  
  // Lectura del nivel de bateria
  int battery_read = analogRead(battery); // Se lee el pin de la bateria
  //float battery_per = ((battery_read)/1023)*100; // formula que pasa de 0-1023 a 0-100%
  //char batteryLvl = String(battery_per) + "%"; // concatenacion del "%" para estetica :)

  //Lectura del nivel de luz (digital)
  //int light = digitalRead(ldr); // lee si hay luz o no, es binario (0 o 1)

  // EQUIVALENTE A UTILIZAR STR.FORMAT EN PYTHON, %d -> valor decimal
  int sense = battery_read;
  Serial.print("Sensing: ");
  Serial.println(sense);
  return sense;
}
 
