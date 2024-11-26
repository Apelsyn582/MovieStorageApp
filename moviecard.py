from PyQt5 import QtWidgets, QtCore, QtGui
from windowaddmovie import AddMovieWindow

class MovieCard(QtWidgets.QWidget):
    def __init__(self, title, rating, date, path_image, parent=None):
        super(MovieCard, self).__init__(parent)

        self.setStyleSheet("""
            background-color: rgb(60, 60, 63); 
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.4); 
            padding: 10px;
        """)
        self.setFixedSize(281, 450)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)

        self.name = QtWidgets.QLabel(title, self)
        self.name.setFont(QtGui.QFont("Arial Black", 9, QtGui.QFont.Bold))
        self.name.setStyleSheet("color: white;")
        self.name.setWordWrap(True)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        main_layout.addWidget(self.name)

        info_layout = QtWidgets.QHBoxLayout()
        info_layout.setSpacing(5)

        self.rating = QtWidgets.QLabel(rating, self)
        self.rating.setFont(QtGui.QFont("Arial", 9))
        self.rating.setStyleSheet("color: gold;")
        self.rating.setAlignment(QtCore.Qt.AlignCenter)  
        info_layout.addWidget(self.rating)

        self.date = QtWidgets.QLabel(date, self)
        self.date.setFont(QtGui.QFont("Arial", 9))
        self.date.setStyleSheet("color: white;")
        self.date.setAlignment(QtCore.Qt.AlignCenter)  
        info_layout.addWidget(self.date)

        main_layout.addLayout(info_layout)

        self.image = QtWidgets.QLabel(self)
        self.image.setPixmap(QtGui.QPixmap(path_image))
        self.image.setScaledContents(True)
        self.image.setFixedSize(261, 330)
        main_layout.addWidget(self.image)
        main_layout.setAlignment(self.image, QtCore.Qt.AlignCenter)
