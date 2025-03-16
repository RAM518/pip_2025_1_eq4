import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import recursos_rc


class TablaMultiplicar(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("E008_TabladeMultiplicar.ui", self)
        self.button_calcular.clicked.connect(self.calcular_tabla)

    def calcular_tabla(self):
        try:
            numero = int(self.input_numero.text())
            resultado = "\n".join([f"{numero} x {i} = {numero * i}" for i in range(1, 11)])
            self.text_resultado.setPlainText(resultado)
        except ValueError:
            self.text_resultado.setPlainText("Por favor, ingrese un número válido.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = TablaMultiplicar()
    ventana.show()
    sys.exit(app.exec_())
