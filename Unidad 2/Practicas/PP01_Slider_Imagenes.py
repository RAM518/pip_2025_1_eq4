import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

# Carga el archivo .ui
qtCreatorFile = "PP01_Slider_Imagenes.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class ImageSlider(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()  # Inicializa correctamente QMainWindow
        self.setupUi(self)  # Carga la UI del archivo .ui

        # Lista de imágenes a mostrar
        self.images = ["leoyzell.jpg", "leo.jpg","volvemosacasa.png", "ardillas.jpg", "gatoinplorandoayuda.jpg" ]
        self.current_index = 0

        # Configurar QLabel para mostrar las imágenes
        self.label.setPixmap(QPixmap(self.images[self.current_index]))
        self.label.setScaledContents(True)

        # Configurar el temporizador para cambiar la imagen cada 3 segundos
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.next_image)
        self.timer.start(1700)

    def next_image(self):
        """Cambia la imagen del QLabel."""
        self.current_index = (self.current_index + 1) % len(self.images)
        self.label.setPixmap(QPixmap(self.images[self.current_index]))

# Ejecutar la aplicación
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ImageSlider()
    window.show()
    sys.exit(app.exec())