import serial
import time

try:
    # Intenta conectarte al puerto COM3.
    # Asegúrate de que la velocidad (baudrate) coincida con la de tu sketch de Arduino (9600).
    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
    print("Conectado a Arduino en COM3.")
except serial.SerialException as e:
    print(f"Error al conectar con Arduino: {e}")
    print("Asegúrate de que el Arduino esté conectado y que el puerto COM3 sea el correcto.")
    exit()

def enviar_comando(comando):
    """Envía un comando al Arduino y lee la respuesta."""
    try:
        arduino.write(bytes(comando, 'utf-8'))
        time.sleep(0.05) # Pequeña pausa para que Arduino procese
        respuesta = arduino.readline().decode('utf-8').rstrip()
        if respuesta:
            print(f"Arduino: {respuesta}")
        else:
            # A veces la primera lectura puede estar vacía si Arduino no ha respondido aún
            time.sleep(0.1)
            respuesta = arduino.readline().decode('utf-8').rstrip()
            if respuesta:
                print(f"Arduino: {respuesta}")
            else:
                print("Arduino: (No se recibió respuesta)")
    except serial.SerialException as e:
        print(f"Error de comunicación: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    try:
        while True:
            print("\nEscribe '1' para encender el LED, '0' para apagarlo.")
            print("Escribe 'salir' para terminar.")
            comando_usuario = input("Comando: ")

            if comando_usuario.lower() == 'salir':
                print("Cerrando conexión.")
                break
            elif comando_usuario == '1' or comando_usuario == '0':
                enviar_comando(comando_usuario)
            else:
                print("Comando no válido. Por favor, introduce '1', '0' o 'salir'.")

    except KeyboardInterrupt:
        print("\nInterrupción por teclado. Cerrando...")
    finally:
        if arduino.is_open:
            arduino.close()
            print("Puerto serie cerrado.")
