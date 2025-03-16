import sys
from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import recursos_rc

class ContadorClicks(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("E0013_Clicks.ui", self)

        self.contador = 0
        self.tiempo_restante = 10  # Duración del juego en segundos

        # Conectar botón de clic
        self.boton_click.clicked.connect(self.incrementar_contador)

        # Configurar el temporizador
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_tiempo)

        # Conectar botón de inicio
        self.boton_iniciar.clicked.connect(self.iniciar_juego)

    def iniciar_juego(self):
        self.contador = 0
        self.tiempo_restante = 10
        self.label_contador.setText("0")
        self.label_tiempo.setText(f"Tiempo: {self.tiempo_restante}s")
        self.timer.start(1000)  # Inicia el temporizador de 1 segundo
        self.boton_click.setEnabled(True)

    def incrementar_contador(self):
        self.contador += 1
        self.label_contador.setText(str(self.contador))

    def actualizar_tiempo(self):
        self.tiempo_restante -= 1
        self.label_tiempo.setText(f"Tiempo: {self.tiempo_restante}s")

        if self.tiempo_restante <= 0:
            self.timer.stop()
            self.boton_click.setEnabled(False)
            self.label_tiempo.setText("¡Tiempo terminado!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ContadorClicks()
    ventana.show()
    sys.exit(app.exec_())
