import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E01_Grados_a_Fahrenheit.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.dial.valueChanged.connect(self.cambiaValor)
        self.dial.setMinimum(0)
        self.dial.setMaximum(200)
        self.dial.setSingleStep(5)
        self.dial.setValue(0)
        self.dial.setWrapping(True)

    def cambiaValor(self):
        GCentigrados = self.dial.value()
        GFahrenheit = (GCentigrados * 9 / 5) + 32
        self.txt_grados.setText(str(GCentigrados))
        self.txt_fahrenheit.setText(str(round(GFahrenheit, 3)))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())