import sys
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel, QPushButton, QGraphicsOpacityEffect
from PyQt5.QtCore import QPropertyAnimation, QByteArray
import recursos_rc

qtCreatorFile = "P_Memorama.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.aplicar_opacidad_imagenes()
        self.conectar_botones()

    def aplicar_opacidad_imagenes(self):
        self.efectos_opacidad = {}
        self.animaciones = {}
        self.estado_imagenes = {}  # Estado actual de cada imagen (True = Visible, False = Oculta)
        opacidad_inicial = 0.0

        for widget in self.findChildren(QLabel):
            efecto_opacidad = QGraphicsOpacityEffect(self)
            efecto_opacidad.setOpacity(opacidad_inicial)
            widget.setGraphicsEffect(efecto_opacidad)
            self.efectos_opacidad[widget.objectName()] = efecto_opacidad
            self.estado_imagenes[widget.objectName()] = False  # Todas las imágenes empiezan ocultas

    def conectar_botones(self):
        for boton in self.findChildren(QPushButton):
            boton.clicked.connect(self.alternar_imagen)

    def alternar_imagen(self):
        boton = self.sender()
        indice = boton.objectName().split('_')[-1]
        label_name = f'label_{indice}'

        if label_name in self.efectos_opacidad:
            label = self.findChild(QLabel, label_name)
            efecto_opacidad = self.efectos_opacidad[label_name]
            estado_actual = self.estado_imagenes[label_name]

            animacion = QPropertyAnimation(efecto_opacidad, b'opacity')
            animacion.setDuration(500)

            if estado_actual:  # Imagen visible, ocultarla
                animacion.setStartValue(1.0)
                animacion.setEndValue(0.0)
            else:  # Imagen oculta, mostrarla
                animacion.setStartValue(0.0)
                animacion.setEndValue(1.0)

            animacion.start()
            self.animaciones[label_name] = animacion

            # Cambiar el estado de la imagen
            self.estado_imagenes[label_name] = not estado_actual

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())