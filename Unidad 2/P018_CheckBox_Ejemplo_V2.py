import time as t
import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "P018_CheckBox_v2.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.cb_dormir.clicked.connect(self.control)
        self.cb_cine.toggled.connect(self.control) #Usar este we

    def control(self):
        obj = self.sender()
        valor= obj.isChecked()
        print("Objeto ", obj.text(), ": ", valor)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())