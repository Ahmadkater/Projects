# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiviewer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(601, 401)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(601, 401))
        Form.setMaximumSize(QtCore.QSize(601, 401))
        self.Imagelbl = QtWidgets.QLabel(Form)
        self.Imagelbl.setGeometry(QtCore.QRect(70, 80, 128, 128))
        self.Imagelbl.setMaximumSize(QtCore.QSize(200, 200))
        self.Imagelbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Imagelbl.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Imagelbl.setText("")
        self.Imagelbl.setObjectName("Imagelbl")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(240, 230, 161, 20))
        self.label_2.setObjectName("label_2")
        self.Browse_button = QtWidgets.QPushButton(Form)
        self.Browse_button.setGeometry(QtCore.QRect(240, 290, 141, 28))
        self.Browse_button.setObjectName("Browse_button")
        self.Count_button = QtWidgets.QPushButton(Form)
        self.Count_button.setGeometry(QtCore.QRect(260, 110, 91, 28))
        self.Count_button.setObjectName("Count_button")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(241, 330, 141, 20))
        self.label.setObjectName("label")
        self.TransImagelbl = QtWidgets.QLabel(Form)
        self.TransImagelbl.setGeometry(QtCore.QRect(400, 80, 128, 128))
        self.TransImagelbl.setMaximumSize(QtCore.QSize(200, 200))
        self.TransImagelbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TransImagelbl.setText("")
        self.TransImagelbl.setObjectName("TransImagelbl")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(70, 230, 501, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(250, 30, 111, 28))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.Play_button = QtWidgets.QPushButton(self.splitter)
        self.Play_button.setEnabled(True)
        self.Play_button.setObjectName("Play_button")
        self.Pause_button = QtWidgets.QPushButton(self.splitter)
        self.Pause_button.setObjectName("Pause_button")
        self.Count_entry = QtWidgets.QLineEdit(Form)
        self.Count_entry.setGeometry(QtCore.QRect(280, 150, 41, 31))
        self.Count_entry.setText("")
        self.Count_entry.setObjectName("Count_entry")
        self.Imagelbl.raise_()
        self.Browse_button.raise_()
        self.Count_button.raise_()
        self.label.raise_()
        self.TransImagelbl.raise_()
        self.progressBar.raise_()
        self.splitter.raise_()
        self.Count_entry.raise_()
        self.label_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Performing Transformation"))
        self.Browse_button.setText(_translate("Form", "Browse"))
        self.Count_button.setText(_translate("Form", "Edit Count"))
        self.label.setText(_translate("Form", "Only Images will be choosen"))
        self.Play_button.setText(_translate("Form", "Play"))
        self.Pause_button.setText(_translate("Form", "Pause"))

