# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filedb.ui'
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
        MainWindow.resize(1280, 800)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 800, 600))
        self.tableWidget.setMinimumSize(QtCore.QSize(800, 600))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.query1 = QtGui.QLineEdit(self.centralwidget)
        self.query1.setGeometry(QtCore.QRect(910, 30, 171, 20))
        self.query1.setObjectName(_fromUtf8("query1"))
        self.processbutton = QtGui.QPushButton(self.centralwidget)
        self.processbutton.setGeometry(QtCore.QRect(840, 180, 75, 23))
        self.processbutton.setObjectName(_fromUtf8("processbutton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(830, 30, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.query2 = QtGui.QLineEdit(self.centralwidget)
        self.query2.setGeometry(QtCore.QRect(910, 70, 171, 20))
        self.query2.setObjectName(_fromUtf8("query2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(830, 70, 51, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.processbutton.setText(_translate("MainWindow", "Search!", None))
        self.label.setText(_translate("MainWindow", "Full Path", None))
        self.label_2.setText(_translate("MainWindow", "Extension", None))

