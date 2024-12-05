from PyQt5 import QtWidgets, QtCore
from moviecard import MovieCard
from addcard import AddCard
from regwindow import RegistrationWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Movie Storage Application")
        MainWindow.showMaximized()

        MainWindow.setStyleSheet("background-color: rgb(45, 45, 48);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.centralwidget.setLayout(self.mainLayout)

        self.searchWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.searchWidget)

        self.lineEdit = QtWidgets.QLineEdit(self.searchWidget)
        self.lineEdit.setFixedWidth(300)
        self.lineEdit.setStyleSheet("""
            background-color: rgb(60, 63, 65); 
            color: white;
            border: 1px solid rgb(80, 80, 80);
            border-radius: 5px;
            padding: 5px;
        """)

        self.searchButton = QtWidgets.QPushButton(self.searchWidget)
        self.searchButton.setText("Пошук")
        self.searchButton.setFixedWidth(100)
        self.searchButton.setFixedHeight(25)
        self.searchButton.setStyleSheet("""
        QPushButton {
            background-color: rgb(85, 170, 255); 
            color: white;
            border: none;
            border-radius: 5px;
            padding: 5px;
            transition: background-color 0.3s ease;
        }
        QPushButton:hover {
            background-color: rgb(0, 123, 255); 
        }
        QPushButton:pressed {
            background-color: rgb(0, 98, 204); 
            padding-top: 7px;  
            padding-bottom: 3px;
        }""")

        self.registerButton = QtWidgets.QPushButton("Реєстрація")
        self.registerButton.setFixedWidth(100)
        self.registerButton.setFixedHeight(25)
        self.registerButton.setStyleSheet("""
                QPushButton {
                    background-color: rgb(85, 170, 255); 
                    color: white;
                    border: none;
                    border-radius: 5px;
                    padding: 5px;
                    transition: background-color 0.3s ease;
                }
                QPushButton:hover {
                    background-color: rgb(0, 123, 255); 
                }
                QPushButton:pressed {
                    background-color: rgb(0, 98, 204); 
                    padding-top: 7px;  
                    padding-bottom: 3px;
                }""")
        self.registerButton.clicked.connect(self.registration_window)

        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout.addWidget(self.searchButton)
        self.horizontalLayout.addWidget(self.registerButton)
        self.horizontalLayout.setAlignment(QtCore.Qt.AlignCenter)

        self.mainLayout.addWidget(self.searchWidget, alignment=QtCore.Qt.AlignCenter)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.mainLayout.addWidget(self.scrollArea)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollAreaWidgetContents.setLayout(self.gridLayout)

        movies = [
            {"title": "Інтерстеллар", "rating": "⭐⭐⭐⭐⭐", "date": "2023-8-12", "path": "images/Interstellar_film_poster2.jpg"},
            {"title": "Паразити", "rating": "⭐⭐⭐⭐", "date": "2024-10-1", "path": "images/2007399.jpg"},
            {"title": "Початок", "rating": "⭐⭐⭐", "date": "2024-9-20", "path": "images/Початок_фільм,_2010.jpg"},
            {"title": "Бійцівський клуб", "rating": "⭐⭐⭐⭐⭐", "date": "2022-8-12", "path": "images/200px-Fight_Club_плакат.jpg"},
            {"title": "Драйв", "rating": "⭐⭐⭐⭐⭐", "date": "2023-12-12", "path": "images/225px-Український_постер_фільму__Драйв_.jpg"}
        ]

        for i, movie in enumerate(movies):
            movie_card = MovieCard(
                title=movie["title"],
                rating=movie["rating"],
                date=movie["date"],
                path_image=movie["path"]
            )
            self.gridLayout.addWidget(movie_card, i // 3, i % 3)

        add_movie_card = AddCard()
        self.gridLayout.addWidget(add_movie_card, len(movies) // 3, len(movies) % 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setStyleSheet("background-color: rgb(45, 45, 48); color: white;")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background-color: rgb(45, 45, 48); color: white;")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def registration_window(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.show()