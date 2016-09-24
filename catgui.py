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
        MainWindow.resize(988, 605)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 541, 381))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.dateField = QtGui.QLineEdit(self.centralwidget)
        self.dateField.setGeometry(QtCore.QRect(680, 90, 251, 20))
        self.dateField.setText(_fromUtf8(""))
        self.dateField.setObjectName(_fromUtf8("dateField"))
        self.commandLinkButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(170, 480, 188, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.locationField = QtGui.QLineEdit(self.centralwidget)
        self.locationField.setGeometry(QtCore.QRect(680, 190, 251, 20))
        self.locationField.setObjectName(_fromUtf8("locationField"))
        self.peopleField = QtGui.QLineEdit(self.centralwidget)
        self.peopleField.setGeometry(QtCore.QRect(680, 240, 251, 20))
        self.peopleField.setObjectName(_fromUtf8("peopleField"))
        self.titleField = QtGui.QLineEdit(self.centralwidget)
        self.titleField.setGeometry(QtCore.QRect(680, 140, 251, 20))
        self.titleField.setObjectName(_fromUtf8("titleField"))
        self.creatorField = QtGui.QLineEdit(self.centralwidget)
        self.creatorField.setGeometry(QtCore.QRect(680, 290, 251, 20))
        self.creatorField.setObjectName(_fromUtf8("creatorField"))
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(30, 480, 111, 41))
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.current_filename = QtGui.QLineEdit(self.centralwidget)
        self.current_filename.setGeometry(QtCore.QRect(10, 20, 171, 20))
        self.current_filename.setText(_fromUtf8(""))
        self.current_filename.setObjectName(_fromUtf8("current_filename"))
        self.descriptionField = QtGui.QLineEdit(self.centralwidget)
        self.descriptionField.setGeometry(QtCore.QRect(680, 340, 251, 20))
        self.descriptionField.setObjectName(_fromUtf8("descriptionField"))
        self.subjectField = QtGui.QLineEdit(self.centralwidget)
        self.subjectField.setGeometry(QtCore.QRect(680, 390, 251, 20))
        self.subjectField.setObjectName(_fromUtf8("subjectField"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 90, 59, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(590, 140, 59, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(590, 190, 59, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(590, 240, 59, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(590, 290, 59, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(590, 340, 81, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(590, 390, 59, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.checkBoxFilter = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxFilter.setGeometry(QtCore.QRect(590, 470, 261, 20))
        self.checkBoxFilter.setObjectName(_fromUtf8("checkBoxFilter"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Folder = QtGui.QAction(MainWindow)
        self.actionOpen_Folder.setObjectName(_fromUtf8("actionOpen_Folder"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "O\'Leary Family Photo Cataloging App", None))
        self.label.setText(_translate("MainWindow", "TextLabel", None))
        self.commandLinkButton.setText(_translate("MainWindow", "Next", None))
        self.commandLinkButton_2.setText(_translate("MainWindow", "Previous", None))
        self.label_2.setText(_translate("MainWindow", "Date", None))
        self.label_3.setText(_translate("MainWindow", "Title", None))
        self.label_4.setText(_translate("MainWindow", "Location", None))
        self.label_5.setText(_translate("MainWindow", "People", None))
        self.label_6.setText(_translate("MainWindow", "Creator", None))
        self.label_7.setText(_translate("MainWindow", "Description", None))
        self.label_8.setText(_translate("MainWindow", "Subject", None))
        self.checkBoxFilter.setText(_translate("MainWindow", "Only show cataloged images", None))
        self.actionOpen_Folder.setText(_translate("MainWindow", "Open Folder", None))

