import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
import recursos_rc

class OperacionesAritmeticas(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("E0016_OperacionesX.ui", self)

        # Lista de operaciones (No se repiten hasta que terminen todas)
        self.preguntas = [
            {"operacion": "5 + 3", "respuesta": "8", "fondo": "Imagenes/gatoinplorandoayuda.jpg"},
            {"operacion": "7 - 2", "respuesta": "5", "fondo": "Imagenes/cerru.jpg"},
            {"operacion": "4 * 3", "respuesta": "12", "fondo": "Imagenes/faker.png"},
            {"operacion": "16 / 4", "respuesta": "4", "fondo": "Imagenes/bici.jpg"}
        ]

        self.preguntas_pendientes = self.preguntas.copy()
        self.pregunta_actual = None

        # Conectar botón de enviar
        self.boton_enviar.clicked.connect(self.verificar_respuesta)

        # Configurar el temporizador
        self.tiempo_limite = 10  # Segundos para responder
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tiempo_agotado)

        self.mostrar_nueva_pregunta()

    def mostrar_nueva_pregunta(self):
        if not self.preguntas_pendientes:
            QMessageBox.information(self, "Fin del juego", "Has completado todas las operaciones!")
            self.close()
            return
        self.pregunta_actual = self.preguntas_pendientes.pop(0)
        self.label_pregunta.setText(self.pregunta_actual["operacion"])

        pixmap = QPixmap(self.pregunta_actual["fondo"])
        self.label_fondo.setPixmap(pixmap)
        self.label_fondo.setScaledContents(True)

        self.input_respuesta.clear()

        # Iniciar temporizador
        self.timer.start(self.tiempo_limite * 1000)

    def verificar_respuesta(self):
        self.timer.stop()
        respuesta_usuario = self.input_respuesta.text()

        if respuesta_usuario == self.pregunta_actual["respuesta"]:
            QMessageBox.information(self, "Correcto!", "Respuesta correcta!")
        else:
            QMessageBox.warning(self, "Incorrecto", "Respuesta incorrecta!")

        self.mostrar_nueva_pregunta()

    def tiempo_agotado(self):
        self.timer.stop()
        QMessageBox.warning(self, "Tiempo agotado", "Se acabó el tiempo para responder!")
        self.mostrar_nueva_pregunta()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = OperacionesAritmeticas()
    ventana.show()
    sys.exit(app.exec_())
