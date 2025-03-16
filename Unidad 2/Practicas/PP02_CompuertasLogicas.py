import sys
from PyQt5 import uic, QtWidgets

# Cargar el archivo .ui
qtCreatorFile = "PP02_CompuertasLogicas.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class CompuertasLogicasApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar señales y slots
        self.btn_calcular.clicked.connect(self.calcular_resultado)

    def calcular_resultado(self):
        # Obtener valores de las entradas
        entrada_a = self.radio_a.isChecked()  # True si está seleccionado
        entrada_b = self.radio_b.isChecked()  # True si está seleccionado

        # Obtener la compuerta seleccionada
        compuerta = self.combo_compuertas.currentText()

        # Calcular el resultado según la compuerta
        if compuerta == "AND":
            resultado = entrada_a and entrada_b
        elif compuerta == "OR":
            resultado = entrada_a or entrada_b
        elif compuerta == "NOT":
            resultado = not entrada_a  # Solo usa la entrada A
        elif compuerta == "XOR":
            resultado = entrada_a != entrada_b
        else:
            resultado = False

        # Mostrar el resultado en el QLabel
        self.label_resultado.setText(str(resultado))

# Ejecutar la aplicación
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CompuertasLogicasApp()
    window.show()
    sys.exit(app.exec_())