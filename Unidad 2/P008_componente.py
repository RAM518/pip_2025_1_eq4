import sys
from PyQt5 import uic, QtWidgets, QtGui
import recursos_rc

qtCreatorFile = "P008_componente.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.selectorImagen.setMinimum(1)  # Valor mínimo del slider
        self.selectorImagen.setMaximum(3)  # Valor máximo del slider (3 veces)
        self.selectorImagen.setSingleStep(1)  # Incremento de 1 en 1
        self.selectorImagen.setValue(1)  # Valor inicial
        self.selectorImagen.valueChanged.connect(self.cambiaValor)

        self.diccionarioDatos = {
            1: (":/Archivo/gatoinplorandoayuda.jpg", ["Gato", "4 meses", "Raton"]),
            2: (":/Archivo/logouat2.jpg", ["Castor", "65 años", "Estudiar"]),
            3: (":/Archivo/logouat.jpg", ["Correcaminos", "75 años", "Superacion"])
        }
        self.indice = 1  # Inicia en 1 para coincidir con el valor del slider
        self.obtenerDatos()

    # Área de los Slots
    def obtenerDatos(self):
        # Obtiene los datos del diccionario según el índice actual
        nombre = self.diccionarioDatos[self.indice][1][0]
        edad = self.diccionarioDatos[self.indice][1][1]
        juguete = self.diccionarioDatos[self.indice][1][2]
        self.txt_nombre.setText(nombre)
        self.txt_edad.setText(edad)
        self.txt_juguete.setText(juguete)

    def cambiaValor(self):
        # Obtiene el valor actual del slider
        value = self.selectorImagen.value()
        self.indice = value  # Actualiza el índice según el valor del slider
        self.obtenerDatos()  # Actualiza los datos mostrados

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())