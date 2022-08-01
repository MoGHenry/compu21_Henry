from windowClass import Window
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
window = Window('compu21')
window.show()

sys.exit(app.exec())
