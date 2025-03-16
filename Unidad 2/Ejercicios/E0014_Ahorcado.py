import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QPixmap
import recursos_rc


class Ahorcado(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("E0014_Ahorcado.ui", self)

        # Lista de palabras posibles
        self.palabras = ["PYTHON", "ELEFANTE", "PROGRAMACION", "GUITARRA", "COMPUTADORA"]
        self.palabra_secreta = random.choice(self.palabras)
        self.palabra_actual = ["_" for _ in self.palabra_secreta]
        self.intentos = 0
        self.max_intentos = 6

        # Rutas de imágenes de cada parte del cuerpo
        self.partes_cuerpo = [
            "Imagenes/faker.png", "Imagenes/ardillas.jpg", "Imagenes/skt.png",
            "Imagenes/bici.jpg", "Imagenes/cerru.jpg", "Imagenes/leo.jpg",
            "Imagenes/gatoinplorandoayuda.jpg"
        ]

        # Lista de labels para cada parte del cuerpo
        self.labels_partes = [
            self.label_cabeza, self.label_torso, self.label_brazo_izq,
            self.label_brazo_der, self.label_pierna_izq, self.label_pierna_der
        ]

        # Inicializar las partes del cuerpo como invisibles
        for label in self.labels_partes:
            label.setVisible(False)

        # Conectar botones
        self.boton_verificar.clicked.connect(self.verificar_letra)

        # Inicializar UI
        self.actualizar_ui()

    def actualizar_ui(self):
        """Actualiza la interfaz gráfica con la palabra y muestra las partes del cuerpo según los intentos."""
        self.label_palabra.setText(" ".join(self.palabra_actual))

        # Mostrar partes del cuerpo según la cantidad de intentos fallidos
        for i in range(self.intentos):
            self.labels_partes[i].setPixmap(QPixmap(self.partes_cuerpo[i]))
            self.labels_partes[i].setScaledContents(True)
            self.labels_partes[i].setVisible(True)

    def verificar_letra(self):
        letra = self.input_letra.text().upper()
        if len(letra) != 1 or not letra.isalpha():
            QMessageBox.warning(self, "Error", "Ingrese una sola letra válida.")
            return

        if letra in self.palabra_secreta:
            for i, l in enumerate(self.palabra_secreta):
                if l == letra:
                    self.palabra_actual[i] = letra
        else:
            if self.intentos < self.max_intentos:
                self.intentos += 1

        self.input_letra.clear()
        self.actualizar_ui()

        # Verificar si el jugador gana o pierde
        if "_" not in self.palabra_actual:
            QMessageBox.information(self, "¡Ganaste!", f"Felicidades, la palabra era {self.palabra_secreta}.")
            self.reiniciar_juego()
        elif self.intentos >= self.max_intentos:
            QMessageBox.critical(self, "Perdiste", f"Game Over. La palabra era {self.palabra_secreta}.")
            self.reiniciar_juego()

    def reiniciar_juego(self):
        self.palabra_secreta = random.choice(self.palabras)
        self.palabra_actual = ["_" for _ in self.palabra_secreta]
        self.intentos = 0

        # Ocultar todas las partes del cuerpo nuevamente
        for label in self.labels_partes:
            label.setVisible(False)

        self.actualizar_ui()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ahorcado()
    ventana.show()
    sys.exit(app.exec_())
