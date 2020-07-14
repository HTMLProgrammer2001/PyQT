from PyQt5.QtWidgets import QDialog, QLineEdit, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import Qt, QObject


class changeEvent(QObject):
    event = pyqtSignal(str, str, str)

    def connect(self, callback):
        self.event.connect(callback)

    def emit(self, *args):
        self.event.emit(*args)


class AddPasswordDialog(QDialog, QWidget):
    def __init__(self, parent):
        super(AddPasswordDialog, self).__init__(parent)

        self.changeEvent = changeEvent()

        self.initUi()

    def initUi(self):
        self.setWindowTitle('Add post')
        self.show()

        self.setMinimumWidth(200)

        hLayout = QVBoxLayout()
        hLayout.setAlignment(Qt.AlignCenter)
        self.setLayout(hLayout)

        self.name = QLineEdit(self)
        self.name.setPlaceholderText('Name')

        self.login = QLineEdit(self)
        self.login.setPlaceholderText('Login')

        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText('Password')

        hLayout.addWidget(self.name)
        hLayout.addWidget(self.login)
        hLayout.addWidget(self.password)

        button = QPushButton('Add')
        button.clicked.connect(self.enterData)

        hLayout.addWidget(button)

    def enterData(self):
        self.changeEvent.emit(self.name.text(), self.login.text(), self.password.text())
        self.close()

    def keyPressEvent(self, event):
        if event.key() + 1 == Qt.Key_Enter:
            self.enterData()

