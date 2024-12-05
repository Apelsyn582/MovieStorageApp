from PyQt5 import QtWidgets, QtCore


class RegistrationWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Реєстрація")
        self.setStyleSheet("background-color: rgb(45, 45, 48); color: white;")
        self.resize(400, 300)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(10)

        self.username_label = QtWidgets.QLabel("Ім'я користувача:")
        self.username_input = QtWidgets.QLineEdit()
        self.setup_line_edit(self.username_input)

        self.email_label = QtWidgets.QLabel("Електронна пошта:")
        self.email_input = QtWidgets.QLineEdit()
        self.setup_line_edit(self.email_input)

        self.password_label = QtWidgets.QLabel("Пароль:")
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.setup_line_edit(self.password_input)

        self.confirm_password_label = QtWidgets.QLabel("Підтвердити пароль:")
        self.confirm_password_input = QtWidgets.QLineEdit()
        self.confirm_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.setup_line_edit(self.confirm_password_input)

        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.register_button = QtWidgets.QPushButton("Зареєструватися")
        self.register_button.setStyleSheet("""
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
        self.cancel_button = QtWidgets.QPushButton("Скасувати")
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
        self.buttons_layout.addWidget(self.register_button)
        self.buttons_layout.addWidget(self.cancel_button)

        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.email_label)
        self.layout.addWidget(self.email_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.confirm_password_label)
        self.layout.addWidget(self.confirm_password_input)
        self.layout.addLayout(self.buttons_layout)

    def setup_line_edit(self, line_edit):
        line_edit.setStyleSheet("""
            background-color: rgb(60, 63, 65); 
            color: white; 
            border: 1px solid rgb(80, 80, 80); 
            border-radius: 5px; 
            padding: 3px; /* Зменшено padding */
        """)
        line_edit.setFixedHeight(25)
