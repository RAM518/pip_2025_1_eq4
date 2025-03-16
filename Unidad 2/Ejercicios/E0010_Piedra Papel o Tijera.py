import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import recursos_rc

class PiedraPapelTijerasApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar la interfaz gráfica desde el archivo .ui
        uic.loadUi("E0010_Piedra Papel o Tijera.ui", self)

        # Conectar los botones a sus funciones correspondientes
        self.boton_piedra.clicked.connect(lambda: self.jugar("piedra"))
        self.boton_papel.clicked.connect(lambda: self.jugar("papel"))
        self.boton_tijeras.clicked.connect(lambda: self.jugar("tijeras"))

    def jugar(self, eleccion_usuario):
        # Opciones posibles
        opciones = ["piedra", "papel", "tijeras"]

        # Elección de la computadora
        eleccion_computadora = random.choice(opciones)

        # Determinar el resultado
        if eleccion_usuario == eleccion_computadora:
            resultado = "¡Empate!"
        elif (
            (eleccion_usuario == "piedra" and eleccion_computadora == "tijeras")
            or (eleccion_usuario == "papel" and eleccion_computadora == "piedra")
            or (eleccion_usuario == "tijeras" and eleccion_computadora == "papel")
        ):
            resultado = "¡Ganaste!"
        else:
            resultado = "¡Perdiste!"

        # Mostrar el resultado
        mensaje = f"Tú elegiste: {eleccion_usuario}\nComputadora eligió: {eleccion_computadora}\n{resultado}"
        self.label_resultado.setText(mensaje)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = PiedraPapelTijerasApp()
    ventana.show()
    sys.exit(app.exec_())