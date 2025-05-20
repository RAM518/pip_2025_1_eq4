from asyncio import timeout

import serial as controlador

arduino = controlador.Serial("COM?", baudrate=9600, timeout=1)
