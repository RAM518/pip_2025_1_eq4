from asyncio import timeout

import serial as controlador

arduino = controlador.Serial("COM?", baudrate=9600, timeout=1)

datos = []
lectura = 0
tot_lecturas = 25

while lectura < tot_lecturas:
    cadena = arduino.readline().decode().strip()
    if cadena != "":
        print(cadena)
        datos.append(cadena)
        lectura=1

datos = [int (i) for i in datos]
print (datos)
