import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E03_Mililitros_a_Litros.ui" #Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.dial.valueChanged.connect(self.cambiaValor)
        self.dial.setMinimum(0)
        self.dial.setMaximum(6000)
        self.dial.setSingleStep(5)
        self.dial.setValue(0)
        self.dial.setWrapping(True)

    def cambiaValor(self):
        ml = self.dial.value()
        lit = ml / 1000
        self.txt_mililitros.setText(str(ml))
        self.txt_litros.setText(str(round(lit, 3)))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())