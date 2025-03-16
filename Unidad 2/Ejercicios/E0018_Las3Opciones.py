import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap
import recursos_rc

class QuizApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("E0018_Las3Opciones.ui", self)

        # Preguntas y respuestas
        self.preguntas = [
            {"imagen": "Imagenes/leoyzell.jpg", "respuesta": "leoyzell", "opciones": ["Celine", "leoyzell", "Rene"]},
            {"imagen": "Imagenes/uatlogo.png", "respuesta": "Harvard", "opciones": ["Harvard", "Tec", "CBTis"]},
            {"imagen": "Imagenes/leo.jpg", "respuesta": "Leo", "opciones": ["Leo", "EstaNo", "EstaTampoco"]},
            {"imagen": "Imagenes/ardillas.jpg", "respuesta": "Ijoesuputamadre", "opciones": ["Ijoesuputamadre", "llamen", "aDios"]},
        ]

        self.pregunta_actual = ["imagen"]

        # Conectar botones
        self.boton1.clicked.connect(lambda: self.verificar_respuesta(self.boton1.text()))
        self.boton2.clicked.connect(lambda: self.verificar_respuesta(self.boton2.text()))
        self.boton3.clicked.connect(lambda: self.verificar_respuesta(self.boton3.text()))

        self.mostrar_nueva_pregunta()

    def mostrar_nueva_pregunta(self):
        self.pregunta_actual = random.choice(self.preguntas)

        # Mostrar imagen
        self.label_imagen.setPixmap(QPixmap(self.pregunta_actual["imagen"]))

        # Asignar opciones

        self.boton1.setText(self.pregunta_actual["opciones"][0])
        self.boton2.setText(self.pregunta_actual["opciones"][1])
        self.boton3.setText(self.pregunta_actual["opciones"][2])

    def verificar_respuesta(self, seleccion):
        if seleccion == self.pregunta_actual["respuesta"]:
            QMessageBox.information(self, "Bien Hecho", "Le atinasteeee!!")
        else:
            QMessageBox.warning(self, "Pus Mal Hecho", "Cuanta mediocridad...")

        self.mostrar_nueva_pregunta()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = QuizApp()
    ventana.show()
    sys.exit(app.exec_())
