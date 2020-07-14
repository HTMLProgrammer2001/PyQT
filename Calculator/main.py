import sys
from design import Ui_MainWindow
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow
from PyQt5.Qt import Qt


class Main(QMainWindow, Ui_MainWindow):
    isCalculated = False

    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.center()

        self.addPushHandlers()

        self.textEdit.setAlignment(Qt.AlignLeft)

    def center(self):
        fr = self.frameGeometry()
        qr = QDesktopWidget().availableGeometry().center()

        fr.moveCenter(qr)
        self.move(fr.topLeft())

    def addDigit(self):
        if self.isCalculated:
            self.textEdit.setText('')
            self.isCalculated = False

        text = self.sender().text()
        self.textEdit.setText(self.textEdit.toPlainText() + text)

    def clearText(self):
        self.textEdit.setText('')

    def calculate(self):
        evaluatedVal = eval(self.textEdit.toPlainText())
        self.textEdit.setText(self.textEdit.toPlainText() + "\n" + str(evaluatedVal))

        self.isCalculated = True

    def addPushHandlers(self):
        self.pushButton_1.clicked.connect(self.addDigit)
        self.pushButton_2.clicked.connect(self.addDigit)
        self.pushButton_3.clicked.connect(self.addDigit)
        self.pushButton_5.clicked.connect(self.addDigit)
        self.pushButton_6.clicked.connect(self.addDigit)
        self.pushButton_7.clicked.connect(self.addDigit)
        self.pushButton_8.clicked.connect(self.addDigit)
        self.pushButton_9.clicked.connect(self.addDigit)
        self.pushButton_10.clicked.connect(self.addDigit)
        self.pushButton_11.clicked.connect(self.addDigit)
        self.pushButton_13.clicked.connect(self.addDigit)
        self.pushButton_14.clicked.connect(self.addDigit)
        self.pushButton_15.clicked.connect(self.addDigit)
        self.pushButton_16.clicked.connect(self.addDigit)

        self.pushButton_12.clicked.connect(self.clearText)
        self.pushButton_4.clicked.connect(self.calculate)


app = QApplication(sys.argv)
main = Main()
main.show()

sys.exit(app.exec_())
