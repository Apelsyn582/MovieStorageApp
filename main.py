import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from moviedes import Ui_MainWindow
class MovieStorageApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Movie Storage Application")
        self.setGeometry(300, 200, 400, 300)

        main_widget = QWidget()
        main_layout = QVBoxLayout()

        self.label = QLabel("ШО ви голови??", self)
        main_layout.addWidget(self.label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MovieStorageApp()
    window.show()
    sys.exit(app.exec_())