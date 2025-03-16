import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E06_Area_Pentagono.ui"  # Nombre del archivo .ui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.txt_metros.textChanged.connect(self.calcular_area)
        self.txt_apotema.textChanged.connect(self.calcular_area)

    def calcular_area(self):
        try:
            lado = float(self.txt_metros.text())
            apotema = float(self.txt_apotema.text())
            area = (5 * lado * apotema) / 2
            self.txt_resultado.setText(f"{area:.2f}")
        except ValueError:
            self.txt_resultado.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())