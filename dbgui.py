#!/usr/bin/env python
from PyQt4 import QtGui, QtCore, QtSql
import sys
import subprocess
import csv
import filedb
import os
import filecmp
import hashlib
from glob import glob

class ExampleApp(QtGui.QMainWindow, filedb.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.processbutton.clicked.connect(self.process)
        self.query1.returnPressed.connect(self.process)
        self.query2.returnPressed.connect(self.process)
        with open('dbconfig.txt', 'r') as fo:
            config_newlines = fo.readlines()
            config = []
            for i in config_newlines:
               config.append(i.rstrip())
                
        print config
        db 		= QtSql.QSqlDatabase.addDatabase(config[0])
    
        
        db.setHostName(config[1])
        db.setPort(int(config[2]))
        db.setDatabaseName(config[3])
        db.setUserName(config[4])
        db.setPassword(config[5])
        
        if (db.open()==False):     
          QtGui.QMessageBox.critical(None, "Database Error",
                    db.lastError().text()) 
        
    def process(self):
            
            
            query = QtSql.QSqlQuery()
            t = '%' + self.query1.text() +  '%'
            cmd = "SELECT * FROM filenames WHERE fullpath LIKE :fullpath"
            if not self.query2.text() == '':
            
                 
            
                 e = '%' + self.query2.text()
                 cmd += " AND filename LIKE :filename"
                 
            query.prepare(cmd)     
            query.bindValue(':fullpath', t)  
            if not self.query2.text() == '':
                query.bindValue(':filename', e)            
            
            query.exec_()
            self.tableWidget.setColumnCount(5) # hardcoded, but change to this for variable - self.tableWidget.setColumnCount(query.record().count())

            self.tableWidget.setRowCount(query.size())
            index=0
            while (query.next()):
                self.tableWidget.setItem(index,0,QtGui.QTableWidgetItem(query.value(0).toString()))
                self.tableWidget.setItem(index,1,QtGui.QTableWidgetItem(query.value(1).toString()))	
                self.tableWidget.setItem(index,2,QtGui.QTableWidgetItem(query.value(2).toString()))	
                self.tableWidget.setItem(index,3,QtGui.QTableWidgetItem(query.value(3).toString()))	
                # Changing order so that I can avoid a field in my view.
                self.tableWidget.setItem(index,4,QtGui.QTableWidgetItem(query.value(5).toString()))	
                index = index + 1  
            
def main():

    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app
    
    
if __name__ == '__main__':
    main()  # run the main function