from PyQt5.QtWidgets import QApplication
import sys

from UI.MainWindow import Main


app = None


def showUI():
    global app

    app = QApplication(sys.argv)
    main = Main()

    main.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    showUI()
