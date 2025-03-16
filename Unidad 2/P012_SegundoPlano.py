import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "P012_SegundoPlano.ui"  # Nombre del archivo .ui aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conexiones para los RadioButtons
        self.rb_perro.clicked.connect(self.perro)
        self.rb_gato.clicked.connect(self.gato)
        self.rb_pajaro.clicked.connect(self.pajaro)

        self.rb_amarillo.toggled.connect(self.amarillo)
        self.rb_rojo.toggled.connect(self.rojo)
        self.rb_azul.toggled.connect(self.azul)

    def perro(self):
        if self.rb_perro.isChecked():
            print("Perro seleccionado")

    def gato(self):
        if self.rb_gato.isChecked():
            print("Gato seleccionado")

    def pajaro(self):
        if self.rb_pajaro.isChecked():
            print("Pájaro seleccionado")

    def amarillo(self):
        if self.rb_amarillo.isChecked():
            print("Color amarillo seleccionado")

    def rojo(self):
        if self.rb_rojo.isChecked():
            print("Color rojo seleccionado")

    def azul(self):
        if self.rb_azul.isChecked():
            print("Color azul seleccionado")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
