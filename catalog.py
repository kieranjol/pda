#!/usr/bin/env python
from PyQt4 import QtGui, QtCore
import sys
import subprocess
import catgui
import os
import filecmp
import hashlib
from glob import glob



counter = 0
class ExampleApp(QtGui.QMainWindow, catgui.Ui_MainWindow):
    def __init__(self):
        global image
        global images
        
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        dir = sys.argv[1]
        os.chdir(dir)
        images = glob('*.jpeg') + glob('*.tif')+ glob('*.jpg')
        image = QtGui.QImage(images[counter])
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))
        self.commandLinkButton.clicked.connect(self.next)
        self.commandLinkButton_2.clicked.connect(self.previous)
        
    def next(self):
        global counter
        counter+=1
        image = QtGui.QImage(images[counter])
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))
    def previous(self):
        global counter
        counter-=1
        image = QtGui.QImage(images[counter])
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))
    





        '''
        self.processButton.setEnabled(True)
        self.processButton.clicked.connect(self.encode)
        #self.oeTextBox.textChanged.connect(self.countup)
        #print text
        #items = []
        self.filmPreparationListBox.itemSelectionChanged.connect(self.getPrepList)
        self.filmCaptureInterventionsListBox.itemSelectionChanged.connect(self.getInterventionList)
        self.rawAudioInterventions.itemSelectionChanged.connect(self.getRawAudioInterventionsList)
        self.userComboBox.activated[str].connect(self.getUser)
        self.tapeWorkstationComboBox.activated[str].connect(self.getWorkstation)
        
        '''
        
        
    
def main():

    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app
    
    
if __name__ == '__main__':
    main()  # run the main function