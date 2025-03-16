import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E05_Peso_a_Dolar.ui"  # Nombre del archivo .ui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.dial.valueChanged.connect(self.cambiaValor)
        self.dial.setMinimum(0)
        self.dial.setMaximum(10000)
        self.dial.setSingleStep(10)
        self.dial.setValue(0)
        self.dial.setWrapping(True)
        self.tipo_cambio = 20.0

    def cambiaValor(self):
        pesos = self.dial.value()
        dolares = pesos / self.tipo_cambio
        self.txt_metros.setText(f"{pesos} MXN")
        self.txt_kms.setText(f"{round(dolares, 2)} USD")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())