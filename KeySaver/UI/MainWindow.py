from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QMessageBox, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon

from Designs.design import Ui_MainWindow
from UI.AddPasswordDialog import AddPasswordDialog
from UI.singleWidget import SingleWidget
from DB import DB


class Main(Ui_MainWindow, QMainWindow):
    db = None

    def __init__(self):
        super().__init__()

        self.execSql()
        self.setupUi(self)
        self.initUi()
        self.setHandlers()

    def execSql(self):
        self.db = DB()

        if not self.db.init():
            QMessageBox.critical(self, 'Error', 'Can not open db')
            self.close()

    def initUi(self):
        self.show()
        self.changeCount()
        self.showList()

        self.setWindowTitle('Key Saver')
        self.setWindowIcon(QIcon('./images/icon.ico'))

    def setHandlers(self):
        self.pushButton.clicked.connect(self.showAddDialog)
        self.lineEdit.textChanged[str].connect(self.showList)
        self.clearButton.clicked.connect(lambda x: (self.db.clear(), self.updateWindow()))

    def changeCount(self):
        self.label.setText('There are {} passwords'.format(self.db.getCount()))

    def showList(self):
        layout = QVBoxLayout()
        wrapper = QWidget(self)

        for row in self.db.filter(self.lineEdit.text()):
            single = SingleWidget(row, self.db)
            single.setParent(self)
            single.changed.signal.connect(self.updateWindow)

            layout.addWidget(single)

        layout.addStretch(1)
        wrapper.setLayout(layout)
        self.scrollArea.setWidget(wrapper)

    def showAddDialog(self):
        dlg = AddPasswordDialog(self)
        dlg.changeEvent.connect(lambda *args: (self.db.addRecord(*args), self.updateWindow()))

    def updateWindow(self):
        self.showList()
        self.changeCount()

    def center(self):
        fr = self.frameGeometry()
        qr = QDesktopWidget().availableGeometry().center()

        fr.moveCenter(qr)
        self.move(fr.topLeft())

    def closeEvent(self, event):
        if QMessageBox.question(self, 'Close', 'Are you sure?') == QMessageBox.Yes:
            self.db.close()
            event.accept()
        else:
            event.ignore()
