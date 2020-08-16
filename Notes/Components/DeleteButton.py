from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QDropEvent
from PyQt5.QtWidgets import QLabel

from Components.Note import Note


# delete signal for app
class DeleteSignal(QObject):
    event = pyqtSignal(int)

    def connect(self, callback):
        self.event.connect(callback)

    def emit(self, *args):
        self.event.emit(*args)


class DeleteButton(QLabel):
    def __init__(self, *args):
        super(DeleteButton, self).__init__(*args)

        self.setObjectName('delete')
        self.setCursor(QtCore.Qt.PointingHandCursor)
        self.setAcceptDrops(True)

        self.signal = DeleteSignal()

    def dragEnterEvent(self, e):
        # if user drag note to button then show hover style
        if isinstance(e.mimeData().parent(), Note):
            e.accept()

            self.setStyleSheet('''
                background: rgba(238, 36, 12, 1);
                color: rgb(255, 255, 255);
                border: 1px solid #fff;
            ''')

    def dragLeaveEvent(self, e):
        # on leave set default style
        self.setStyleSheet('''
            border: 1px solid rgb(0, 0, 0);
            background: rgba(255, 0, 0, 0);
            color: rgb(0, 0, 0);  
        ''')

    def dropEvent(self, e: QDropEvent):
        w: Note = e.mimeData().parent()
        w.hide()

        # set default style and emit delete event
        self.setStyleSheet('''
            border: 1px solid rgb(0, 0, 0);
            background: rgba(255, 0, 0, 0);
            color: rgb(0, 0, 0);  
        ''')

        self.signal.emit(w.item['id'])
