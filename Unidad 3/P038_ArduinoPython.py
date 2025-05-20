import sys
from PyQt5 import uic, QtWidgets, QtGui
import recursos_rc
import serial as tarjeta

qtCreatorFile = "P38.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.arduino=None
        self.btn_accion.clicked.connect(self.accion)

    # Área de los Slots
    def accion(self):
        texto=self.btn_accion.text()
        com=self.txt_com.text()
        if texto == "Conectar":
            self.arduino = tarjeta.Serial(com, baudrate=9600, timeout= 1)
            self.btn_accion.setText("Desconectar")
            self.btn_accion.setText("Conectado")
        elif texto== "Desconectar":
            self.arduino.close()
            self.btn_accion.setText("Reconectar")
            self.btn_accion.setText("Desconectado")
        elif texto=="Reconectar":
            self.arduino.open()
            self.btn_accion.setText("Desconectar")
            self.btn_accion.setText("Reconectado")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())