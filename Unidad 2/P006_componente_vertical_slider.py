import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P006_VerticalSlider.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp (QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__ (self):
        QtWidgets.QMainWindow.__init__ (self)
        Ui_MainWindow.__init__ (self)
        self.setupUi(self)
        self.dial.valueChanged.connect(self.cambiaValor)
        self.dial.setSingleStep(5)
        self.dial.setMinimum(-50)
        self.dial.setMaximum(50)
        self.dial.setValue(50)
        self.txt_valor.setText("-50")

    def cambiaValor (self):
        value=self.dial.value()
        self.txt_valor.setText(str(value))
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    def saludar(self ):
        print("Saludos a los de ingenieria")