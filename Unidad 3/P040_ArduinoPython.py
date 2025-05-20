import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
import recursos_rc
import serial as tarjeta

qtCreatorFile = "P40_ArduinoPython.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.txt_com.setText("COM3")

        self.arduino=None

        self.btn_accion.clicked.connect(self.accion)
        self.segundoPlano = QtCore.QTimer
        ##self.segundoPlano.timeout.connect(self.lecturas)

        self.bandera=0
    # Área de los Slots

    def lecturas (self):
        if self.arduino.isOpen():
            if self.arduino.inWaiting(): #Serial.available()>0
                cadena = self.arduino.readLine().decode().strip()
                if cadena != "":
                    self.datos.append==0;
                    if self.bandera==0:
                        print(cadena)
                        self.lista_datos.addItem(cadena)
                        self.lista_datos.setCurrentRow(self.lista_datos.count()-1)

    try
        def accion(self):
            texto=self.btn_accion.text()
            com=self.txt_com.text()
            if texto == "Conectar":
                self.arduino = tarjeta.Serial(com, baudrate=9600, timeout= 1)
                self.segundoPlano.start(100)
                self.btn_accion.setText("Desconectar")
                self.txt_estado.setText("Conectado")
            elif texto== "Desconectar":
                self.segundoPlano.stop()
                self.arduino.close()
                self.btn_accion.setText("Reconectar")
                self.txt_estado.setText("Desconectado")
            elif texto=="Reconectar":
                self.arduino.open()
                self.segundoPlano.start(100)
                self.btn_accion.setText("Desconectar")
                self.txt_estado.setText("Reconectado")
    except Exception as error:
        print(error)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())