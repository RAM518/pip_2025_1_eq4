from asyncio import timeout

import serial as controlador

arduino = controlador.Serial("COM3", baudrate=9600, timeout=1)

while True:
    accion = input("Ingresa el valor de accion para el led: ")
    arduino.write(accion.encode())