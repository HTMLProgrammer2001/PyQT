from PyQt5 import QtCore, QtGui, QtWidgets

from Components.DeleteButton import DeleteButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QtWidgets.QMainWindow):
        MainWindow.setFixedSize(600, 470)

        self.centralwidget = QtWidgets.QWidget()
        MainWindow.setStyleSheet('''
        QLabel{
            background: #FFE633;
            border: 1px solid black;
            border-radius: 5px;
            font: 75 10pt \"Arial\";
            color: black;
        }
        QLabel:hover{
            background:#F9DF52;
        }
        
        QLabel#add{
            border: 1px solid #fff;
            border-radius: 25px;
            background: #21C7F7;
            color: #fff;font: 75 26pt \"Arial Narrow\"
        }
        QLabel#add:hover {
            background: #19A0C8;
        }
        
        QLabel#delete{
            border: 1px solid rgb(0, 0, 0);
            background: rgba(255, 0, 0, 0);
            padding: 10px;
            
            color: rgb(0, 0, 0);  
            font-weight: bold;
            font-size: 18px;  
        }
        
        QLabel#delete:hover{
            background: rgba(238, 36, 12, 1);
            color: rgb(255, 255, 255);
            border: 1px solid #fff;
        }
        ''')

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget.setLayout(self.verticalLayout)

        self.radioWidget = QtWidgets.QWidget(self.centralwidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.radioWidget.sizePolicy().hasHeightForWidth())

        self.radioWidget.setSizePolicy(sizePolicy)
        self.radioWidget.setMinimumSize(QtCore.QSize(0, 40))

        self.radioLayout = QtWidgets.QHBoxLayout()

        self.newestRadio = QtWidgets.QRadioButton(self.radioWidget)
        self.newestRadio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.newestRadio.setChecked(True)
        self.radioLayout.addWidget(self.newestRadio)

        self.oldestRadio = QtWidgets.QRadioButton(self.radioWidget)
        self.oldestRadio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioLayout.addWidget(self.oldestRadio)

        self.radioLayout.addStretch(1)

        self.deleteButton = DeleteButton('Drop to delete')
        self.radioLayout.addWidget(self.deleteButton)

        self.radioWidget.setLayout(self.radioLayout)

        self.verticalLayout.addWidget(self.radioWidget)


        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setFixedHeight(400)

        self.gridLayoutWidget = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.gridLayoutWidget)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayoutWidget.setFixedSize(585, 0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget.setLayout(self.gridLayout)

        self.verticalLayout.addWidget(self.scrollArea)

        self.add = QtWidgets.QLabel(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(280, 410, 50, 50))
        self.add.setFixedSize(QtCore.QSize(50, 50))
        self.add.setAlignment(QtCore.Qt.AlignCenter)
        self.add.setCursor(QtCore.Qt.PointingHandCursor)
        self.add.setObjectName("add")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Notes"))
        self.newestRadio.setText(_translate("MainWindow", "Newest"))
        self.oldestRadio.setText(_translate("MainWindow", "Oldest"))
        self.add.setText(_translate("MainWindow", "+"))
