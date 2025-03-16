import sys
import random
import recursos_rc
from functools import partial
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer


class SimonDiceApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("E0012_Memorizar Patrones.ui", self)

        self.secuencia = []
        self.indice_usuario = 0
        self.puntaje = 0
        self.labels = {
            "imagen 1": self.label_imagen1,
            "imagen 2": self.label_imagen2,
            "imagen 3": self.label_imagen3,
            "imagen 4": self.label_amarillo,
        }

        # Asignar eventos de clic a cada label correctamente
        for color, label in self.labels.items():
            label.mousePressEvent = partial(self.verificar_secuencia, color)

        self.label_iniciar.mousePressEvent = lambda event: self.iniciar_juego()

        self.timer_secuencia = QTimer(self)
        self.timer_secuencia.timeout.connect(self.mostrar_siguiente_color)

    def iniciar_juego(self):
        self.secuencia.clear()
        self.indice_usuario = 0
        self.puntaje = 0
        self.label_puntaje.setText("Puntaje: 0")
        self.label_instrucciones.setText("Memoriza la secuencia y repítela")
        self.agregar_color_a_secuencia()
        self.mostrar_secuencia()

    def agregar_color_a_secuencia(self):
        color = random.choice(list(self.labels.keys()))
        self.secuencia.append(color)

    def mostrar_secuencia(self):
        self.indice_secuencia = -1
        self.timer_secuencia.start(1000)

    def mostrar_siguiente_color(self):
        self.indice_secuencia += 1
        if self.indice_secuencia < len(self.secuencia):
            color = self.secuencia[self.indice_secuencia]
            self.resaltar_label(color)
        else:
            self.timer_secuencia.stop()

    def resaltar_label(self, color):
        label = self.labels[color]
        label.setStyleSheet("border: 3px solid white;")
        QTimer.singleShot(500, lambda: label.setStyleSheet("border: none;"))

    def verificar_secuencia(self, color, event):
        if color == self.secuencia[self.indice_usuario]:
            self.indice_usuario += 1
            if self.indice_usuario == len(self.secuencia):
                self.puntaje += 1
                self.label_puntaje.setText(f"Puntaje: {self.puntaje}")
                self.indice_usuario = 0
                self.agregar_color_a_secuencia()
                self.mostrar_secuencia()
        else:
            QMessageBox.information(self, "Fin del juego", f"¡Perdiste! Puntaje final: {self.puntaje}")
            self.iniciar_juego()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = SimonDiceApp()
    ventana.show()
    sys.exit(app.exec_())
