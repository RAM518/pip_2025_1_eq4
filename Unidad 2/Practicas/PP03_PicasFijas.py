import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class PicasFijas(QMainWindow):
    def __init__(self):
        super().__init__()  # Corregido: __init__ en lugar de _init_
        uic.loadUi("PP03_PicasFijas.ui", self)  # Cargar la interfaz

        # Conectar botón de verificar
        self.boton_verificar.clicked.connect(self.verificar_intento)

        # Generar número secreto al iniciar
        self.generar_numero_secreto()

    def generar_numero_secreto(self):
        """Genera un número de 4 cifras únicas como el número secreto."""
        cifras = random.sample(range(0, 10), 4)  # Genera 4 cifras únicas
        self.numero_secreto = "".join(map(str, cifras))
        print("Número secreto generado:", self.numero_secreto)  # Para debug

    def verificar_intento(self):
        intento = self.input_numero.text()

        # Validar el intento
        if len(intento) != 4 or not intento.isdigit() or len(set(intento)) != 4:
            QMessageBox.warning(self, "Error", "Ingresa un número de 4 cifras únicas.")
            return

        # Calcular picas y fijas
        picas, fijas = self.calcular_picas_fijas(intento)
        self.label_resultado.setText(f"Picas: {picas}, Fijas: {fijas}")

        # Verificar si el usuario ganó
        if fijas == 4:
            QMessageBox.information(self, "¡Ganaste!", f"Felicidades, el número era {self.numero_secreto}.")
            self.generar_numero_secreto()  # Generar un nuevo número secreto

    def calcular_picas_fijas(self, intento):
        """Calcula la cantidad de Picas y Fijas en base al intento del usuario."""
        picas = sum(1 for i in range(4) if intento[i] in self.numero_secreto and intento[i] != self.numero_secreto[i])
        fijas = sum(1 for i in range(4) if intento[i] == self.numero_secreto[i])
        return picas, fijas


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = PicasFijas()
    ventana.show()
    sys.exit(app.exec_())