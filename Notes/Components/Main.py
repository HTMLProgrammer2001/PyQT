from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLabel
from math import ceil

from Components.MainWindowDesign import Ui_MainWindow as MainWindowDesign
from Components.Note import Note
from Components.wordprocessor import NoteWindow, QWidget
from Database import Database


class Notes(MainWindowDesign, QMainWindow):
    db: Database

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.openDB()
        self.addHandlers()
        self.showNotes()

        self.setAcceptDrops(True)
        self.setWindowIcon(QIcon('./images/Icon.ico'))

    def addHandlers(self):
        self.add.mousePressEvent = self.showAddEditor

        self.newestRadio.clicked.connect(self.showNotes)
        self.oldestRadio.clicked.connect(self.showNotes)
        self.deleteButton.signal.connect(self.db.deleteNote)

    def showAddEditor(self, *args):
        w = NoteWindow()
        w.show()

        # add note handler
        w.saveEmitter.connect(lambda text: (self.db.addNote(text), w.close()))

    def showEditEditor(self, item, *args):
        w = NoteWindow(item['text'])
        w.show()

        # edit note handler
        w.saveEmitter.connect(lambda text: (self.db.editNote(item['id'], text), w.close()))

    def openDB(self):
        self.db = Database()

        # connect to db change
        self.db.dbChanged.event.connect(self.showNotes)

        if not self.db.open():
            # show error
            QMessageBox(self, 'Error in db', 'Error in db connection')
        else:
            self.db.createTable()

    def emptyNotes(self):
        # set label in center
        self.gridLayoutWidget.setFixedHeight(40)
        label = QLabel()
        label.setText('No notes')
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("background: none; border: none")

        # add widget to layout
        self.gridLayout.addWidget(label, 1, 1, 1, 1)

    def noteClickListener(self, lbl):
        item = lbl.property('item')

        # inner function for closure
        def func(e):
            if e.button() == Qt.LeftButton:
                self.showEditEditor(item)

        return func

    def showNotes(self):
        notes = self.db.getNotes(self.newestRadio.isChecked())
        notesCount = len(notes)
        rows = ceil(notesCount/3)

        # delete all notes
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().setParent(None)

        # set new grid height
        self.gridLayoutWidget.setFixedHeight(rows * 130)

        # create notes
        for i, item in enumerate(notes):
            label = Note(item, self.gridLayoutWidget)
            label.mouseReleaseEvent = self.noteClickListener(label)

            self.gridLayout.addWidget(label, i//3, i % 3, 1, 1)

        # set empty label
        if not len(notes):
            self.emptyNotes()

    def dragEnterEvent(self, e):
        # accept all drags
        e.accept()

    def dragMoveEvent(self, e):
        w: QWidget = e.mimeData().parent()

        if not w:
            return

        # if user drag note than move it
        self.gridLayout.removeWidget(w)
        w.setParent(self)
        w.show()

        w.move(e.pos())

        e.setDropAction(Qt.MoveAction)
        e.accept()

    def dropEvent(self, e):
        # on drop re render
        e.mimeData().parent().hide()

        self.showNotes()
