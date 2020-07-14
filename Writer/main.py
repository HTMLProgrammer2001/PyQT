from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QMessageBox
from PyQt5.QtCore import QBasicTimer, Qt
import sys
from time import time
from os import listdir
from random import choice

from design import Ui_MainWindow


class Main(Ui_MainWindow, QMainWindow):
    languages = ['ua', 'ru', 'en']
    isRun = False
    curText = ''
    curLanguage = 'ua'
    printedChars = 0
    mistakesCount = 0

    def __init__(self):
        super().__init__()

        self.timer = QBasicTimer()
        self.timer.start(50, self)
        self.startTime = time()

        self.setupUi(self)

        self.center()
        self.initUi()
        self.bindHandlers()

        self.stopButton.setEnabled(False)

    def initUi(self):
        self.setFixedSize(400, 316)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        sr = QDesktopWidget().availableGeometry().center()

        self.label.setWordWrap(True)

        qr.moveCenter(sr)
        self.move(qr.topLeft())

    def bindHandlers(self):
        self.startButton.clicked.connect(self.start)
        self.startAction.triggered.connect(self.start)

        self.stopButton.clicked.connect(self.stop)
        self.stopAction.triggered.connect(self.stop)

        self.exitAction.triggered.connect(app.quit)

        self.menu_2.triggered.connect(self.setLanguage)

        self.startButton.setFocusPolicy(Qt.NoFocus)
        self.stopButton.setFocusPolicy(Qt.NoFocus)

    def start(self):
        self.restart()
        self.isRun = True

        texts = listdir("./text/{}".format(self.curLanguage))
        randText = choice(texts)

        with open("./text/{}/{}".format(self.curLanguage, randText), encoding='UTF-8') as f:
            self.curText = f.read()
            self.showText()

        self.startButton.setEnabled(False)

        self.label.setFocus()

        self.startButton.setText('Заново')

        self.stopButton.setText('Остановить')
        self.stopButton.setEnabled(True)

    def stop(self):
        if not self.stopButton.isEnabled():
            return

        if self.isRun:
            self.startButton.setEnabled(True)
            self.stopButton.setText('Продолжить')
        else:
            self.startButton.setEnabled(False)
            self.stopButton.setText('Остановить')

        self.isRun = not self.isRun

    def showText(self):
        newText = '<font color="#0f0">{}</font>{}'.format(
            self.curText[:self.printedChars], self.curText[self.printedChars:])

        self.label.setText(newText)

    def setLanguage(self):
        for i, action in enumerate(self.menu_2.actions()):
            if action.isChecked():
                self.curLanguage = self.languages[i]
                return

    def restart(self):
        self.mistakesCount = 0
        self.printedChars = 0

        self.startTime = time()

    def win(self):
        charsPerSec = 60 / ((time() - self.startTime) / self.printedChars)
        mistakesPerc = self.mistakesCount / (self.printedChars + self.mistakesCount) * 100

        QMessageBox.information(self, 'Вы прошли тест', "Напечатано символов: {} \n".format(len(self.curText)) +
            "Средняя скорость: {:.2f} зн/мин \n".format(charsPerSec) +
            "Ошибки: {:.2f}%".format(mistakesPerc))

        self.restart()

    def keyPressEvent(self, e):
        if not self.isRun:
            return

        if e.text() == self.curText[self.printedChars]:
            self.printedChars += 1
            self.showText()

            if self.printedChars == len(self.curText):
                self.win()
        else:
            print("{} not same {}".format(e.text(), self.curText[self.printedChars]))
            self.mistakesCount += 1

    def timerEvent(self, e):
        if not self.isRun:
            return

        try:
            charsPerSec = 60/((time() - self.startTime)/self.printedChars)
        except ZeroDivisionError:
            charsPerSec = 0

        try:
            mistakesPerc = self.mistakesCount/(self.printedChars + self.mistakesCount) * 100
        except ZeroDivisionError:
            mistakesPerc = 0

        self.curSpeed.setText("{:.2f} зн/мин".format(charsPerSec))
        self.mistakes.setText("Ошибки: {:.2f}%".format(mistakesPerc))


app = QApplication(sys.argv)
main = Main()

sys.exit(app.exec_())
