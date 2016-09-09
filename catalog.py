#!/usr/bin/env python
from PyQt4 import QtGui, QtCore
import sys
import subprocess
import csv
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
        
        self.display_filename()
        
        self.grab_exisiting_metadata()
        
        self.commandLinkButton.clicked.connect(self.create_csv)
        self.submitButton.clicked.connect(self.archive)
        self.commandLinkButton.clicked.connect(self.display_filename)
        self.commandLinkButton_2.clicked.connect(self.previous)
        
        
        self.commandLinkButton.clicked.connect(self.next)
        self.commandLinkButton.clicked.connect(self.clear)
        self.commandLinkButton.clicked.connect(self.grab_exisiting_metadata)

    
    def archive(self):
       for i in images:
           csv_check = i + '.csv'
           if os.path.isfile(csv_check):
               master_dir = os.path.splitext(i)[0] 
               metadata = master_dir + '/metadata'
               proxies = master_dir + '/proxy'
               log = master_dir + '/logs'
               exif = metadata + '/exif.xml'  
               md5_file = master_dir + '/' + master_dir + '_md5.txt'
               sha512_file = master_dir + '/' + master_dir + '_sha512.txt'
               
               os.makedirs(master_dir)
               os.makedirs(metadata)
               os.makedirs(proxies)
               os.makedirs(log)
               
               '''
               robocopy D:\2013\2013-01-21\ D:\ IMG_2246.CR2
               '''
               with open(exif, "w+") as fo:
                   exiftool_output = subprocess.check_output(['exiftool', '-X', i ])
                   fo.write(exiftool_output)
                
               with open(md5_file, "w+") as fo:
                   md5 = subprocess.check_output(['md5deep', '-ler', i])
                   fo.write(md5)
                
               with open(sha512_file, "w+") as fo:
                   sha512 = subprocess.check_output(['openssl', 'sha512', '-r', i])
                   fo.write(sha512)

    def grab_exisiting_metadata(self):
        
        csv_file = images[counter] + '.csv'
        print os.path.abspath(csv_file), 'xx'
        if os.path.isfile(csv_file):
                    read_object = open(csv_file)
                    reader = csv.reader(read_object)
                    csv_list = list(reader)
                    print csv_list[1]
                    filename_from_csv, date, title, creator, people, location, description, subject = csv_list[1]
                    self.dateField.setText(date)
                    self.titleField.setText(title)
                    self.creatorField.setText(creator)
                    self.peopleField.setText(people)
                    self.locationField.setText(location) 
                    self.descriptionField.setText(description) 
                    self.subjectField.setText(subject)    
    def create_csv(self):
        
        csv_file = images[counter] + '.csv'
        date = self.dateField.text()
        title = self.titleField.text()
        creator = self.creatorField.text()
        people = self.peopleField.text()
        location = self.locationField.text()
        description = self.descriptionField.text()
        subject = self.subjectField.text()
        data_check = [str(date), str(title), str(creator), str(people), str(location), str(description), str(subject)]
        print data_check
        field_count = 0
        for fields in data_check:
            if fields == '':
                print fields
            else:
                field_count += 1
        print field_count
        if not field_count == 0:        
            if not os.path.isfile(csv_file):
                f = open(csv_file, 'wb')
                try:
                    writer = csv.writer(f)
                    header = ['Filename','Date', 'Title', 'Creator', 'People', 'Location', 'Description', 'Subject']
                    writer.writerow(header)
                    writer.writerow([images[counter],date, title, creator, people, location, description, subject])

                finally:
                    f.close()
                    
                    
    def clear(self):
        self.dateField.setText('')
        self.titleField.setText('')
        self.creatorField.setText('')
        self.peopleField.setText('')
        self.locationField.setText('') 
        self.descriptionField.setText('') 
        self.subjectField.setText('') 
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
    def display_filename(self):
        self.current_filename.setText(images[counter])    
def main():

    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app
    
    
if __name__ == '__main__':
    main()  # run the main function