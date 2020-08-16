from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QCursor, QMouseEvent, QDrag
from PyQt5.QtCore import Qt, QMimeData


class Note(QLabel):
    def __init__(self, item, *args):
        super().__init__(*args)

        self.setMouseTracking(True)
        self.item = item
        self.initUi()

    def initUi(self):
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setAlignment(Qt.AlignTop)
        self.setFixedSize(190, 125)
        self.setWordWrap(True)
        self.setText(self.item['text'])
        self.setProperty('item', self.item)

    def mousePressEvent(self, e: QMouseEvent):
        super().mousePressEvent(e)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, e: QMouseEvent):
        if e.buttons() != Qt.RightButton:
            return

        # start drag note
        mimeData = QMimeData()
        mimeData.setParent(self)

        drag = QDrag(self)
        drag.setMimeData(mimeData)

        drag.exec_(Qt.MoveAction)

    def dragEnterEvent(self, e):
        e.accept()
