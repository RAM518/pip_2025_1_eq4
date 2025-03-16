import sys
import math
import recursos_rc
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class TeoremaPitagorasApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar la interfaz gráfica desde el archivo .ui
        uic.loadUi("E007_TeoremadePitagoras.ui", self)

        # Conectar el botón a la función de calcular
        self.button_calcular.clicked.connect(self.calcular_hipotenusa)

    def calcular_hipotenusa(self):
        # Obtener los valores de los catetos
        try:
            cateto1 = float(self.input_cateto1.text())
            cateto2 = float(self.input_cateto2.text())

            # Calcular la hipotenusa
            hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

            # Mostrar el resultado
            self.label_resultado.setText(f"Resultado: {hipotenusa:.2f}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingresa valores válidos para los catetos.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = TeoremaPitagorasApp()
    ventana.show()
    sys.exit(app.exec_())