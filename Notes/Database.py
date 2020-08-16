from PyQt5.QtSql import QSqlQuery, QSqlDatabase
from PyQt5.QtCore import pyqtSignal, QObject


# database change event
class DbChange(QObject):
    event = pyqtSignal()


class Database:
    dbChanged = DbChange()

    def __init__(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.query = QSqlQuery()

    def open(self) -> bool:
        self.db.setDatabaseName('notes.db')

        # connect to db
        if self.db.open():
            return True

        return False

    def createTable(self):
        self.query.exec_('''CREATE TABLE IF NOT EXISTS `notes`(
            `text` TEXT NOT NULL
        );''')

    def addNote(self, text: str) -> bool:
        self.query.prepare("INSERT INTO `notes` VALUES(?);")
        self.query.bindValue(0, text)
        self.query.exec_()

        self.dbChanged.event.emit()

        if self.query.lastError():
            return False

        return True

    def getNotes(self, asc: bool = True):
        # get notes with sort
        if asc:
            self.query.exec_("SELECT rowid, * FROM `notes`;")
        else:
            self.query.exec_("SELECT rowid, * FROM `notes` ORDER BY `rowid` DESC;")

        notes = []

        # convert to list of dicts
        while self.query.next():
            notes.append({
                'id': self.query.value(0),
                'text': self.query.value(1)
            })

        return notes

    def getNote(self, id: int):
        # get note by id
        self.query.prepare("SELECT rowid, * FROM `notes` WHERE `rowid`=?")
        self.query.bindValue(0, id)
        self.query.exec_()

        self.query.first()

        return {
            'id': self.query.value(0),
            'text': self.query.value(1)
        }

    def editNote(self, id: int, text: str):
        self.query.prepare("UPDATE `notes` SET `text`=? WHERE `rowid`=?")
        self.query.bindValue(0, text)
        self.query.bindValue(1, id)
        self.query.exec_()

        self.dbChanged.event.emit()

        return {
            'id': id,
            'text': text
        }

    def deleteNote(self, id):
        self.query.prepare("DELETE FROM `notes` WHERE `rowid`=?")
        self.query.bindValue(0, id)
        self.query.exec_()

        self.dbChanged.event.emit()

        return bool(self.query.lastError())
