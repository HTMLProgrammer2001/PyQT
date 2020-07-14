from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal, QObject

from Designs.singleDesign import Ui_Form
from UI.EditPasswordDialog import EditPasswordDialog


class ChangeSignal(QObject):
    signal = pyqtSignal()


class SingleWidget(Ui_Form, QWidget):
    def __init__(self, row, db):
        super(SingleWidget, self).__init__()
        self.row = row
        self.db = db

        self.changed = ChangeSignal()

        self.setupUi(self)
        self.initUi()
        self.addHandlers()

    def initUi(self):
        self.nameLbl.setText(self.row['name'])

        self.setFixedHeight(51)

    def addHandlers(self):
        self.deleteLbl.mousePressEvent = self.deleteData
        self.editLbl.mousePressEvent = self.showEditDlg
        self.showLbl.mousePressEvent = self.showPassword

    def showPassword(self, *args):
        QMessageBox.information(self, 'Login data for {}'.format(self.row['name']),
                                f"Login: {self.row['login']}\nPassword: {self.row['password']}")

    def deleteData(self, *args):
        message = 'Are you really want delete data for {}?'.format(self.row['name'])

        if QMessageBox.question(self, 'Close', message) == QMessageBox.Yes:
            self.db.deleteRecord(self.row['id'])
            self.changed.signal.emit()

    def showEditDlg(self, *args):
        dlg = EditPasswordDialog(self, self.row)
        dlg.changeEvent.connect(self.editData)

    def editData(self, id, name, password):
        self.db.updateRecord(id, name, password)
        self.changed.signal.emit()
