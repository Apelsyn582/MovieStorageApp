from PyQt5 import QtWidgets, QtCore, QtGui

class AddCard(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AddCard, self).__init__(parent)

        self.setStyleSheet("background-color: rgb(111, 106, 255); border-radius: 10px; padding: 10px;")
        self.setFixedSize(281, 411)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)

        self.label = QtWidgets.QLabel("Додайте новий фільм", self)
        self.label.setFont(QtGui.QFont("Arial Black", 10, QtGui.QFont.Bold))
        self.label.setStyleSheet("color: black;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        main_layout.addWidget(self.label)

        self.add_button = QtWidgets.QPushButton("Додати", self)
        self.add_button.setStyleSheet("background-color: rgb(255, 100, 100); color: white;")
        self.add_button.setFixedHeight(40)
        main_layout.addWidget(self.add_button)
