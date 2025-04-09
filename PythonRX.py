import serial
import time

# Abrimos la conexión con el puerto serial
# Windows
# arduino = serial.Serial('COM4', 9600)
# macOS
arduino = serial.Serial('/dev/tty.wchusbserial58741248741', 9600)
time.sleep(2)  # Esperamos a que se estabilice la conexión

print("Conexión establecida. Esperando datos...\n")

try:
    while True:
        if arduino.in_waiting > 0:
            linea = arduino.readline().decode('utf-8').strip()
            print(f"Recibido: {linea}")
except KeyboardInterrupt:
    print("\nFinalizando programa...")

finally:
    arduino.close()
    print("Puerto cerrado.")
