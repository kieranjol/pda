# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'catgui.ui'
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
        MainWindow.resize(868, 605)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 541, 381))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.dateField = QtGui.QLineEdit(self.centralwidget)
        self.dateField.setGeometry(QtCore.QRect(580, 120, 131, 20))
        self.dateField.setText(_fromUtf8(""))
        self.dateField.setObjectName(_fromUtf8("dateField"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(580, 200, 131, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.commandLinkButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(170, 480, 188, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(580, 100, 131, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(580, 250, 131, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.locationField = QtGui.QLineEdit(self.centralwidget)
        self.locationField.setGeometry(QtCore.QRect(580, 220, 131, 20))
        self.locationField.setObjectName(_fromUtf8("locationField"))
        self.peopleField = QtGui.QLineEdit(self.centralwidget)
        self.peopleField.setGeometry(QtCore.QRect(580, 270, 131, 20))
        self.peopleField.setObjectName(_fromUtf8("peopleField"))
        self.lineEdit_7 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(580, 150, 131, 20))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.titleField = QtGui.QLineEdit(self.centralwidget)
        self.titleField.setGeometry(QtCore.QRect(580, 170, 131, 20))
        self.titleField.setObjectName(_fromUtf8("titleField"))
        self.lineEdit_9 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(580, 300, 131, 20))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.creatorField = QtGui.QLineEdit(self.centralwidget)
        self.creatorField.setGeometry(QtCore.QRect(580, 320, 131, 20))
        self.creatorField.setObjectName(_fromUtf8("creatorField"))
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(30, 480, 111, 41))
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.submitButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(570, 480, 188, 41))
        self.submitButton.setObjectName(_fromUtf8("submitButton"))
        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(580, 370, 141, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(580, 410, 111, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.lineEdit_11 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(580, 70, 131, 20))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.current_filename = QtGui.QLineEdit(self.centralwidget)
        self.current_filename.setGeometry(QtCore.QRect(10, 20, 113, 20))
        self.current_filename.setText(_fromUtf8(""))
        self.current_filename.setObjectName(_fromUtf8("current_filename"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(730, 250, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.descriptionField = QtGui.QLineEdit(self.centralwidget)
        self.descriptionField.setGeometry(QtCore.QRect(730, 270, 113, 20))
        self.descriptionField.setObjectName(_fromUtf8("descriptionField"))
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(730, 300, 113, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.subjectField = QtGui.QLineEdit(self.centralwidget)
        self.subjectField.setGeometry(QtCore.QRect(730, 320, 113, 20))
        self.subjectField.setObjectName(_fromUtf8("subjectField"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 868, 22))
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
        self.submitButton.setText(_translate("MainWindow", "Submit!", None))
        self.radioButton.setText(_translate("MainWindow", "Email pic to Kieran", None))
        self.radioButton_2.setText(_translate("MainWindow", "Email pic to David", None))
        self.lineEdit_11.setText(_translate("MainWindow", "Photo Details:", None))
        self.lineEdit.setText(_translate("MainWindow", "Description", None))
        self.lineEdit_6.setText(_translate("MainWindow", "Subject", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))

