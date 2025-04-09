import serial
import time

# Conectamos al puerto serial
arduino = serial.Serial('/dev/tty.wchusbserial58741248741', 9600)
time.sleep(2)  # Esperamos que se estabilice la conexión

print("Conexión establecida. Escribe un mensaje para enviar al Arduino.")
print("Escribe 'salir' para terminar.\n")

try:
    while True:
        mensaje = input(">> ")
        if mensaje.lower() == 'salir':
            break
        arduino.write((mensaje + '\n').encode('utf-8'))  # Añade \n para que Arduino detecte el final
        print(f"Enviado: {mensaje}")
except KeyboardInterrupt:
    print("\nInterrupción del usuario.")

finally:
    arduino.close()
    print("Puerto cerrado.")
