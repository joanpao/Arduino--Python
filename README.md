# Arduino ->Python
Demo de una conexión serie desde Arduino (TX) a Python (RX)
Los programas funcionan por parejas:
- PythonTX.py y PythonTX_KEYBOARD.py envian por el puerto serie  un texto incluido en el programa o tecleado desde el terminal
que es recibido por ArduinoRX que debe de estar ejecutándose en la placa de desarrollo para que lo muestra en el display
(Se evita que escriba en puerto serie para envitar interrupciones) pero
podría reenviarse via LoRa / WiFi / Bluetooth a otro dispositivo
-  ArduinoTX envian por el puerto serie  un texto incluido en el programa pero que podía haber recibido via LoRa / WiFi / Bluetooth
al programa PythonRX.py que debe estar ejecutandose en el ordenador

Observe que:
- La arquitectura es de cliente-servidor, debiendo de estar el programa RX ejecutándose en su entorno correspondiente.
- La placa de desarrollo de arduino (ESP32) ebe estar conectada con el ordenador por un cable USB de datos
(no todos los cables USB lo permiten, pues muchos solamente soportan alimentación)
- En el programa Python dependeiendo de su sistema operativo tendrá que definir el puerto de una forma u otra
  - En windows  arduino = serial.Serial('COM4', 9600)
  - En macOS  arduino = serial.Serial('/dev/tty.wchusbserialxxxxxxxxxx', 9600)
