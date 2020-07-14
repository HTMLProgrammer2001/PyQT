# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'single.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        showIcon = QtGui.QPixmap('./images/eye.png')
        editIcon = QtGui.QPixmap('./images/pen.png')
        deleteIcon = QtGui.QPixmap('./images/close.png')

        Form.setObjectName("Form")
        Form.resize(402, 56)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 401, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nameLbl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.nameLbl.sizePolicy().hasHeightForWidth())
        self.nameLbl.setSizePolicy(sizePolicy)
        self.nameLbl.setScaledContents(False)
        self.nameLbl.setObjectName("name")
        self.horizontalLayout.addWidget(self.nameLbl)
        self.showLbl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.showLbl.sizePolicy().hasHeightForWidth())
        self.showLbl.setSizePolicy(sizePolicy)
        self.showLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.showLbl.setObjectName("show")
        self.showLbl.setPixmap(showIcon)
        self.horizontalLayout.addWidget(self.showLbl)
        self.editLbl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.editLbl.setObjectName("edit")
        self.editLbl.setPixmap(editIcon)
        self.horizontalLayout.addWidget(self.editLbl)
        self.deleteLbl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.deleteLbl.setObjectName("delete_2")
        self.deleteLbl.setPixmap(deleteIcon)
        self.horizontalLayout.addWidget(self.deleteLbl)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nameLbl.setText(_translate("Form", "TextLabel"))
