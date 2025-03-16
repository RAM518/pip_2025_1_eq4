import sys
import random
from PyQt5 import uic
import recursos_rc
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class AdivinaNumeroApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar la interfaz gráfica desde el archivo .ui
        uic.loadUi("E009_AdivinaelNumero.ui", self)

        # Inicializar el número aleatorio
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

        # Conectar el botón a la función de adivinar
        self.boton_adivinar.clicked.connect(self.adivinar)

    def adivinar(self):
        # Obtener el número ingresado por el usuario
        try:
            numero_usuario = int(self.input_numero.text())
            self.intentos += 1

            # Comparar con el número secreto
            if numero_usuario < self.numero_secreto:
                self.label_resultado.setText("¡Más alto! Intenta de nuevo.")
            elif numero_usuario > self.numero_secreto:
                self.label_resultado.setText("¡Más bajo! Intenta de nuevo.")
            else:
                mensaje = f"¡Felicidades! Adivinaste el número en {self.intentos} intentos."
                QMessageBox.information(self, "¡Ganaste!", mensaje)
                self.reset_game()
        except ValueError:
            self.label_resultado.setText("Por favor, ingresa un número válido.")

    def reset_game(self):
        # Reiniciar el juego
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0
        self.label_resultado.setText("")
        self.input_numero.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = AdivinaNumeroApp()
    ventana.show()
    sys.exit(app.exec_())