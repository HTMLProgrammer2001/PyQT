from PyQt5.QtWidgets import QDialog, QLineEdit, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import Qt, QObject


class changeEvent(QObject):
    event = pyqtSignal(int, str, str)

    def connect(self, callback):
        self.event.connect(callback)

    def emit(self, *args):
        self.event.emit(*args)


class EditPasswordDialog(QDialog, QWidget):
    def __init__(self, parent, row):
        super(EditPasswordDialog, self).__init__(parent)

        self.changeEvent = changeEvent()
        self.row = row

        self.initUi()

    def initUi(self):
        self.setWindowTitle('Edit post')
        self.show()

        self.setMinimumWidth(200)

        hLayout = QVBoxLayout()
        hLayout.setAlignment(Qt.AlignCenter)
        self.setLayout(hLayout)

        self.name = QLineEdit(self)
        self.name.setPlaceholderText('Name')
        self.name.setText(self.row['name'])

        self.login = QLineEdit(self)
        self.login.setPlaceholderText('Login')
        self.login.setText(self.row['login'])

        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText('Password')
        self.password.setText(self.row['password'])

        hLayout.addWidget(self.name)
        hLayout.addWidget(self.login)
        hLayout.addWidget(self.password)

        button = QPushButton('Edit')
        button.clicked.connect(self.enterData)

        hLayout.addWidget(button)

    def enterData(self):
        self.changeEvent.emit(self.row['id'], self.name.text(), self.login.text(), self.password.text())
        #self.close()

    def keyPressEvent(self, event):
        if event.key() + 1 == Qt.Key_Enter:
            self.enterData()

