from asyncio import timeout

import serial as controlador

arduino = controlador.Serial("COM?", baudrate=9600, timeout=1)

while True:
    cadena = arduino.readline().decode().strip()
    if cadena != "":
        print(cadena)