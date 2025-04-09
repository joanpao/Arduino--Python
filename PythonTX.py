import serial
import time

# Abrimos la conexión con el puerto serial
# Windows
# arduino = serial.Serial('COM4', 9600)
# macOS
# arduino = serial.Serial('/dev/tty.wchusbserialxxxxxxxx', 9600)
arduino = serial.Serial('/dev/tty.wchusbserial58741248741', 9600)
# Esperamos a que se estabilice la conexión
time.sleep(2)

print("Conexión establecida. Enviando datos...\n")

#Envia mensajes numerados indefinidamente

try:
    contador = 0
    while True:
        mensaje = f"Mensaje numero {contador}\n"
        # Enviamos el mensaje
        arduino.write(mensaje.encode('utf-8'))  
        print(f"Enviado: {mensaje.strip()}")
        # Incrementa el contador de mensajes
        contador += 1
        # Esperamos un segundo entre mensajes
        time.sleep(1)  
except KeyboardInterrupt:
    print("\nFinalizando programa...")

finally:
    arduino.close()
    print("Puerto cerrado.")

