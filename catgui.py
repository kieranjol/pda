# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kieranjol\pda\catgui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(678, 577)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 361, 351))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(450, 120, 131, 20))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 200, 131, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.commandLinkButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(170, 470, 188, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(450, 100, 131, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(450, 250, 131, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(450, 220, 131, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(450, 270, 131, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(450, 150, 131, 20))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(450, 170, 131, 20))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_9 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(450, 300, 131, 20))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_10 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(450, 320, 131, 20))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(30, 470, 111, 41))
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.commandLinkButton_3 = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(440, 470, 188, 41))
        self.commandLinkButton_3.setObjectName(_fromUtf8("commandLinkButton_3"))
        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(450, 370, 141, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(450, 410, 111, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.lineEdit_11 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(450, 70, 131, 20))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.lineEdit_12 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(10, 20, 113, 20))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 678, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "O\'Leary Family Photo Cataloging App", None))
        self.label.setText(_translate("MainWindow", "TextLabel", None))
        self.lineEdit_2.setText(_translate("MainWindow", "Location", None))
        self.commandLinkButton.setText(_translate("MainWindow", "Next", None))
        self.lineEdit_3.setText(_translate("MainWindow", "Date", None))
        self.lineEdit_4.setText(_translate("MainWindow", "People", None))
        self.lineEdit_7.setText(_translate("MainWindow", "Title", None))
        self.lineEdit_9.setText(_translate("MainWindow", "Creator - Photographer", None))
        self.commandLinkButton_2.setText(_translate("MainWindow", "Previous", None))
        self.commandLinkButton_3.setText(_translate("MainWindow", "Submit!", None))
        self.radioButton.setText(_translate("MainWindow", "Email pic to Kieran", None))
        self.radioButton_2.setText(_translate("MainWindow", "Email pic to David", None))
        self.lineEdit_11.setText(_translate("MainWindow", "Photo Details:", None))
        self.lineEdit_12.setText(_translate("MainWindow", "img_1001.jpg", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))

