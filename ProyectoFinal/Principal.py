import sys
from PyQt5 import QtWidgets, uic, QtCore
import serial

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Vista_Principal.ui", self)
        self.arduino = None
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.leer_datos)
        self.btn_iniciar.clicked.connect(self.conectar_arduino)
        self.txt_estado.setText("Desconectado")
        # Conectar los botones mostrar
        self.btn_mostrar_1.clicked.connect(lambda: self.mostrar_datos('dht'))
        self.btn_mostrar_2.clicked.connect(lambda: self.mostrar_datos('ldr'))
        self.btn_mostrar_3.clicked.connect(lambda: self.mostrar_datos('ultrasonico'))
        # Buffers para los datos
        self.buffer_dht = []
        self.buffer_ldr = []
        self.buffer_ultrasonico = []

    def conectar_arduino(self):
        try:
            self.arduino = serial.Serial('COM3', 9600, timeout=1)
            self.txt_estado.setText("Conectado a Arduino")
            self.timer.start(200)  
        except Exception as e:
            self.txt_estado.setText(f"Error: {e}")

    def leer_datos(self):
        if self.arduino and self.arduino.isOpen():
            try:
                while self.arduino.in_waiting:
                    linea = self.arduino.readline().decode(errors='ignore').strip()
                    if linea:
                        # Guardar en buffer según palabra clave
                        if ("Temperatura" in linea or "Motor" in linea or "DHT" in linea or "Transistor" in linea):
                            self.buffer_dht.append(linea)
                        elif ("LDR" in linea or "LEDs" in linea or "Fotoreceptor" in linea):
                            self.buffer_ldr.append(linea)
                        elif ("Distancia" in linea or "Alerta" in linea or "Ultrasonico" in linea):
                            self.buffer_ultrasonico.append(linea)
            except Exception as e:
                self.txt_estado.setText(f"Lectura error: {e}")

    def mostrar_datos(self, tipo):
        if tipo == 'dht':
            self.lista_datos.clear()
            for linea in self.buffer_dht[-100:]:  # Solo muestra los últimos 100 datos
                self.lista_datos.addItem(linea)
            if self.buffer_dht:
                self.lista_datos.setCurrentRow(self.lista_datos.count()-1)
        elif tipo == 'ldr':
            self.lista_datos_2.clear()
            for linea in self.buffer_ldr[-100:]:
                self.lista_datos_2.addItem(linea)
            if self.buffer_ldr:
                self.lista_datos_2.setCurrentRow(self.lista_datos_2.count()-1)
        elif tipo == 'ultrasonico':
            self.lista_datos_3.clear()
            for linea in self.buffer_ultrasonico[-100:]:
                self.lista_datos_3.addItem(linea)
            if self.buffer_ultrasonico:
                self.lista_datos_3.setCurrentRow(self.lista_datos_3.count()-1)
        # Vuelve a llamar a mostrar_datos después de 1 segundo para refrescar
        QtCore.QTimer.singleShot(1000, lambda: self.mostrar_datos(tipo))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
