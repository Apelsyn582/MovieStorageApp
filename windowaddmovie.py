from PyQt5 import QtWidgets, QtCore, QtGui


class AddMovieWindow(QtWidgets.QWidget):
    def __init__(self):
        super(AddMovieWindow, self).__init__()

        self.setWindowTitle("Додати фільм")
        self.setFixedSize(500, 360)

        self.setStyleSheet("""
            background-color: rgb(45, 45, 48);
            border-radius: 10px;
            padding: 10px;
        """)

        main_layout = QtWidgets.QVBoxLayout(self)

        self.name_label = QtWidgets.QLabel("Назва фільму:", self)
        self.name_label.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))  # Зробимо текст жирним
        self.name_label.setStyleSheet("color: white;")
        self.name_input = QtWidgets.QLineEdit(self)
        self.name_input.setStyleSheet("""
            background-color: rgb(60, 63, 65); 
            color: white;
            border: 1px solid rgb(80, 80, 80);
            border-radius: 5px;
            padding: 5px;
        """)
        main_layout.addWidget(self.name_label)
        main_layout.addWidget(self.name_input)

        self.rating_label = QtWidgets.QLabel("Рейтинг:", self)
        self.rating_label.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))  # Зробимо текст жирним
        self.rating_label.setStyleSheet("color: white;")
        self.rating_input = QtWidgets.QLineEdit(self)
        self.rating_input.setStyleSheet("""
            background-color: rgb(60, 63, 65); 
            color: white;
            border: 1px solid rgb(80, 80, 80);
            border-radius: 5px;
            padding: 5px;
        """)
        main_layout.addWidget(self.rating_label)
        main_layout.addWidget(self.rating_input)

        self.date_label = QtWidgets.QLabel("Дата виходу:", self)
        self.date_label.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))  # Зробимо текст жирним
        self.date_label.setStyleSheet("color: white;")
        self.date_input = QtWidgets.QLineEdit(self)
        self.date_input.setStyleSheet("""
            background-color: rgb(60, 63, 65); 
            color: white;
            border: 1px solid rgb(80, 80, 80);
            border-radius: 5px;
            padding: 5px;
        """)
        main_layout.addWidget(self.date_label)
        main_layout.addWidget(self.date_input)

        self.image_label = QtWidgets.QLabel("Зображення:", self)
        self.image_label.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))  # Зробимо текст жирним
        self.image_label.setStyleSheet("color: white;")
        self.image_input = QtWidgets.QLineEdit(self)
        self.image_button = QtWidgets.QPushButton("Вибрати файл", self)
        self.image_button.setStyleSheet("""
            background-color: rgb(85, 170, 255);
            color: white;
            border: none;
            border-radius: 5px;
            padding: 5px;
        """)
        self.image_button.clicked.connect(self.select_image)

        image_layout = QtWidgets.QHBoxLayout()
        image_layout.addWidget(self.image_input)
        image_layout.addWidget(self.image_button)
        main_layout.addWidget(self.image_label)
        main_layout.addLayout(image_layout)

        button_layout = QtWidgets.QHBoxLayout()

        self.add_button = QtWidgets.QPushButton("Додати", self)
        self.add_button.setStyleSheet("""
            background-color: rgb(85, 170, 255); 
            color: white;
            border: none;
            border-radius: 5px;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: rgb(70, 150, 240);  
        }
        QPushButton:pressed {
            background-color: rgb(50, 120, 200); 
            padding-top: 7px;  
            padding-bottom: 3px; 
        }
        """)
        self.add_button.clicked.connect(self.add_movie)

        self.cancel_button = QtWidgets.QPushButton("Скасувати", self)
        self.cancel_button.setStyleSheet("""
            background-color: rgb(255, 0, 0); 
            color: white;
            border: none;
            border-radius: 5px;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: rgb(200, 0, 0);  
        }
        QPushButton:pressed {
            background-color: rgb(150, 0, 0); 
            padding-top: 7px;  
            padding-bottom: 3px;
        }
        """)
        self.cancel_button.clicked.connect(self.close)

        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.cancel_button)

        main_layout.addLayout(button_layout)

    def select_image(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setNameFilter("Images (*.png *.jpg *.bmp)")
        file_dialog.setViewMode(QtWidgets.QFileDialog.List)
        if file_dialog.exec_():
            selected_file = file_dialog.selectedFiles()[0]
            self.image_input.setText(selected_file)

    def add_movie(self):
        title = self.name_input.text()
        rating = self.rating_input.text()
        date = self.date_input.text()
        image_path = self.image_input.text()

        self.close()
