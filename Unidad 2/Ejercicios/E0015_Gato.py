
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QEvent
import recursos_rc

class Gato(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("E0015_Gato.ui", self)

        # Definir imágenes
        self.img_vacia = "Imagenes/skt.png"
        self.img_circulo = "Imagenes/gatoinplorandoayuda.jpg"
        self.img_tacha = "Imagenes/ardillas.jpg"

        self.turno = "O"  # Empieza el jugador con círculo

        # Lista de labels (las celdas del juego)
        self.celdas = [
            self.label_1, self.label_2, self.label_3,
            self.label_4, self.label_5, self.label_6,
            self.label_7, self.label_8, self.label_9
        ]

        # Tablero lógico para verificar victoria
        self.tablero = [["" for _ in range(3)] for _ in range(3)]

        # Inicializar las celdas
        for i, label in enumerate(self.celdas):
            label.setPixmap(QPixmap(self.img_vacia))
            label.setScaledContents(True)
            label.installEventFilter(self)  # Aplicar filtro de eventos para detectar clics
            label.setProperty("indice", i)  # Guardar índice de celda

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress and obj in self.celdas:
            self.cambiar_imagen(obj)
            return True
        return super().eventFilter(obj, event)

    def cambiar_imagen(self, label):
        indice = label.property("indice")
        fila, col = divmod(indice, 3)

        if label.pixmap() and label.pixmap().cacheKey() == QPixmap(self.img_vacia).cacheKey():
            if self.turno == "O":
                label.setPixmap(QPixmap(self.img_circulo))
                self.tablero[fila][col] = "O"
                self.turno = "X"
            else:
                label.setPixmap(QPixmap(self.img_tacha))
                self.tablero[fila][col] = "X"
                self.turno = "O"

        # Verificar victoria
        ganador = self.verificar_victoria()
        if ganador:
            QMessageBox.information(self, "Juego Terminado", f"¡{ganador} ha ganado!")
            self.reiniciar_juego()

    def verificar_victoria(self):
        # Revisar filas, columnas y diagonales
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] and self.tablero[i][0] != "":
                return self.tablero[i][0]  # Fila completa
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] and self.tablero[0][i] != "":
                return self.tablero[0][i]  # Columna completa

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] and self.tablero[0][0] != "":
            return self.tablero[0][0]  # Diagonal principal

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] and self.tablero[0][2] != "":
            return self.tablero[0][2]  # Diagonal secundaria

        return None

    def reiniciar_juego(self):
        self.turno = "O"
        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        for label in self.celdas:
            label.setPixmap(QPixmap(self.img_vacia))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Gato()
    ventana.show()
    sys.exit(app.exec_())

