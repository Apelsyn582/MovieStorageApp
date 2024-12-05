import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from designs.moviedes import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())