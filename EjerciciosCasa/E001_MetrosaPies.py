import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E001_MetrosaPies.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_convertir.clicked.connect(self.convertir)
        self.btn_guardar.clicked.connect(self.guardar)

    # Área de los Slots
    def convertir(self):
        try:
            metros = float(self.txt_metros.text())
            pies = metros * 3.28084  # Factor de conversión de metros a pies
            self.txt_pies.setText(f"{pies:.2f}")  # Mostrar resultado con dos decimales
        except ValueError:
            self.msj("Por favor, ingrese un número válido.")

    def guardar(self):
        try:
            metros = self.txt_metros.text()
            pies = self.txt_pies.text()
            if metros and pies:
                with open("../Archivos/conversiones.csv", "a") as archivo:
                    archivo.write(f"{metros},{pies}\n")
                self.msj("Conversión guardada con éxito.")
            else:
                self.msj("Realice una conversión antes de guardar.")
        except Exception as e:
            self.msj(f"Error al guardar: {e}")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
