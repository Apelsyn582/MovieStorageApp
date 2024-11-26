from PyQt5 import QtWidgets, QtCore, QtGui

from windowaddmovie import AddMovieWindow


class AddCard(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AddCard, self).__init__(parent)

        self.setStyleSheet("""
            background-color: #292C42; 
            border-radius: 10px;
            border: 2px solid rgb(255, 255, 255); 
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.4); 
            padding: 10px;
        """)

        self.setFixedSize(281, 411)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)

        self.label = QtWidgets.QLabel("Додайте новий фільм", self)
        self.label.setFont(QtGui.QFont("Arial Black", 12, QtGui.QFont.Bold))
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        main_layout.addWidget(self.label)

        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.mousePressEvent = self.add_movie_event

    def add_movie_event(self, event):
        self.open_add_movie_window()

    def open_add_movie_window(self):
        self.add_movie_window = AddMovieWindow()
        self.add_movie_window.show()