import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer, QTime
import recursos_rc
class RelojAlarmaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar la interfaz gráfica desde el archivo .ui
        uic.loadUi("E0011_Reloj con Alarma.ui", self)

        # Inicializar variables
        self.alarma = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_reloj)
        self.timer.start(1000)  # Actualizar cada segundo

        # Conectar el botón para establecer la alarma
        self.boton_set_alarma.clicked.connect(self.establecer_alarma)

    def actualizar_reloj(self):
        # Obtener la hora actual
        hora_actual = QTime.currentTime()
        hora_str = hora_actual.toString("hh:mm:ss")
        self.label_reloj.setText(hora_str)

        # Verificar si la alarma está activa
        if self.alarma and hora_actual == self.alarma:
            QMessageBox.information(self, "Alarma", "¡Es hora!")
            self.alarma = None
            self.label_alarma.setText("Alarma no establecida")

    def establecer_alarma(self):
        # Obtener los valores de los spinboxes
        horas = self.spin_horas.value()
        minutos = self.spin_minutos.value()
        segundos = self.spin_segundos.value()

        # Crear un objeto QTime para la alarma
        self.alarma = QTime(horas, minutos, segundos)

        # Mostrar la alarma establecida
        self.label_alarma.setText(f"Alarma establecida: {self.alarma.toString('hh:mm:ss')}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = RelojAlarmaApp()
    ventana.show()
    sys.exit(app.exec_())