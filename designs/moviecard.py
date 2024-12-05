from PyQt5 import QtWidgets, QtCore, QtGui


class MovieCard(QtWidgets.QWidget):
    def __init__(self, title, rating, date, path_image, parent=None):
        super(MovieCard, self).__init__(parent)

        self.setStyleSheet("background-color: rgb(111, 106, 255); border-radius: 10px; padding: 10px;")
        self.setFixedSize(281, 411)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)

        self.name = QtWidgets.QLabel(title, self)
        self.name.setFont(QtGui.QFont("Arial Black", 10, QtGui.QFont.Bold))
        self.name.setStyleSheet("color: black;")
        self.name.setWordWrap(True)
        self.name.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        main_layout.addWidget(self.name)

        info_layout = QtWidgets.QHBoxLayout()

        self.rating = QtWidgets.QLabel(rating, self)
        self.rating.setStyleSheet("color: black;")
        self.rating.setAlignment(QtCore.Qt.AlignLeft)
        info_layout.addWidget(self.rating)

        self.date = QtWidgets.QLabel(date, self)
        self.date.setStyleSheet("color: black;")
        self.date.setAlignment(QtCore.Qt.AlignRight)
        info_layout.addWidget(self.date)

        main_layout.addLayout(info_layout)

        self.image = QtWidgets.QLabel(self)
        self.image.setPixmap(QtGui.QPixmap(path_image))
        self.image.setScaledContents(True)
        self.image.setFixedSize(261, 321)
        main_layout.addWidget(self.image)
        main_layout.setAlignment(self.image, QtCore.Qt.AlignCenter)
