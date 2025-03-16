import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
import recursos_rc

class Semaforo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("E0017_SimularSemaforo.ui", self)

        self.estado = "verde"
        self.tiempo_verde = 3000
        self.tiempo_parpadeo = 3000
        self.tiempo_amarillo = 2000
        self.tiempo_rojo = 5000
        self.parpadeo_verde = 4  # Parpadeo 4 veces en 3 segundos

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.iniciar_parpadeo)

        self.timer_parpadeo = QTimer(self)
        self.timer_parpadeo.timeout.connect(self.parpadear_verde)

        self.iniciar_semaforo()

    def iniciar_semaforo(self):
        self.label_verde.setVisible(True)
        self.label_amarillo.setVisible(False)
        self.label_rojo.setVisible(False)

        self.timer.start(self.tiempo_verde)

    def iniciar_parpadeo(self):
        self.timer.stop()
        self.parpadeo_verde = 4
        self.timer_parpadeo.start(750)

    def parpadear_verde(self):
        if self.parpadeo_verde > 0:
            self.label_verde.setVisible(not self.label_verde.isVisible())
            self.parpadeo_verde -= 1
        else:
            self.timer_parpadeo.stop()
            self.cambiar_estado()

    def cambiar_estado(self):
        if self.estado == "verde":
            self.estado = "amarillo"
            self.label_verde.setVisible(False)
            self.label_amarillo.setVisible(True)
            self.timer.start(self.tiempo_amarillo)
        elif self.estado == "amarillo":
            self.estado = "rojo"
            self.label_amarillo.setVisible(False)
            self.label_rojo.setVisible(True)
            self.timer.start(self.tiempo_rojo)
        elif self.estado == "rojo":
            self.estado = "verde"
            self.label_rojo.setVisible(False)
            self.label_verde.setVisible(True)
            self.timer.start(self.tiempo_verde)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Semaforo()
    ventana.show()
    sys.exit(app.exec_())
