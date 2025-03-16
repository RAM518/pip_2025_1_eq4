import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E02_Horas_a_Segundos.ui"  # Nombre del archivo .ui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Configuración del QDial
        self.dial.valueChanged.connect(self.cambiaValor)
        self.dial.setMinimum(0)
        self.dial.setMaximum(24)
        self.dial.setSingleStep(1)
        self.dial.setValue(0)
        self.dial.setWrapping(True)
        self.dial.setNotchesVisible(True)
        self.dial.setInvertedAppearance(True)

    def cambiaValor(self):
        posicion = self.dial.value()
        horas = posicion if posicion != 0 else 12
        segundos = horas * 3600

        self.txt_metros.setText(f"{horas} HORAS")
        self.txt_kms.setText(f"{segundos} SEGUNDOS")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())