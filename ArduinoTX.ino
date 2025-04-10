//Libraries for OLED Display
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

void setup() {
  Serial.begin(9600);  // Inicializa la comunicación serial
  while (!Serial) {
    ; // Espera a que se abra el puerto serie (necesario para algunos Arduinos)
  }
  Serial.println("Arduino listo para recibir datos.");
}

void loop() {
  // Si hay datos disponibles desde el puerto serie (enviados por Python)
  if (Serial.available() > 0) {
    String recibido = Serial.readStringUntil('\n');  // Lee hasta nueva línea
    recibido.trim(); // Elimina espacios en blanco al inicio y final
    Serial.print("Mensaje recibido: ");
    Serial.println(recibido);  // Imprime el mensaje de vuelta
  }

  // Opcional: envía un mensaje cada cierto tiempo
  // delay(2000);
  // Serial.println("Hola desde Arduino");
}
