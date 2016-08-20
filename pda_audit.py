import subprocess
import sys
import filecmp
from glob import glob
import os
import time
import csv

video_dir = sys.argv[1]
def create_csv(csv_file, *args):
    f = open(csv_file, 'wb')
    try:
        writer = csv.writer(f)
        writer.writerow(*args)
    finally:
        f.close()
        
def append_csv(csv_file, *args):
    f = open(csv_file, 'ab')
    try:
        writer = csv.writer(f)
        writer.writerow(*args)
    finally:
        f.close()
csv_filename = os.path.basename(video_dir) +  '_item_level' + time.strftime("_%Y_%m_%dT%H_%M_%S")
# CSV will be saved to your Desktop.
csvfile = os.path.expanduser("~/Desktop/%s.csv") % csv_filename       
create_csv(csvfile,('Filename', 'Codec', 'Megapixels', 'Filesize', 'Make', 'Camera Model Name', 'Image Width', 'Image Height', 'Exposure Time', 'F stop', 'ISO', 'Lens Model', 'File Modified Date', 'File Creation Date', 'Exif Modify Date'))      
# Directory with files that we want to transcode losslessly and generate metadata for
def get_exiftool(var_type, filename):
    var_type = subprocess.check_output(['exiftool', '-Megapixels','-FileSize', '-FileType', '-Make', '-Model','-ImageWidth','-ImageHeight','-ExposureTime','-FNumber', '-ISO', '-LensModel', '-FileModifyDate', '-FileCreateDate','-ModifyDate', '-s','-s','-s',filename])
    return var_type.splitlines()
#csv       = tkFileDialog.asksaveasfile(parent=root, defaultextension='.csv') 
all_files = 0
for root, dirs, files in os.walk(video_dir):
    for filename in files:
        all_files += 1
print all_files 
all_file_counter = 1
for root, dirs, files in os.walk(video_dir):
      
    total_files = len(files)
    counter = 1
    for filename in files:
        
        if filename.endswith(('.mov', '.mxf', '.avi', '.mp4', '.ogg', '.ogm', '.wmv','.mkv','.flv','.webm', 'jpg', 'jpeg', 'cr2', 'JPG', 'JPEG', 'CR2')):
             name = (os.path.join(root, filename))

             metadata =  get_exiftool('megapixels',  name )
             megapixels = metadata[0]
             filesize = metadata[1]
             codec = metadata[2]
             make = metadata[3]
             camera_model = metadata[4]
             image_width = metadata[5]
             image_height = metadata[6]
             exposure = metadata[7]
             fstop = metadata[8]
             iso = metadata[9]
             if subprocess.check_output(['exiftool', '-LensModel', name]) == '':
                 metadata.insert(10, 'No metadata')
             
             lensmodel = metadata[10]
           
              
             date_modified = metadata[11] 
             date_created = metadata[12] 
             exif_modify = metadata[13] 
             print metadata, name
             print ' File %d of %d in  current dir, %d of %d overall' % (counter, total_files, all_file_counter, all_files)
             counter +=1
             all_file_counter +=1
             append_csv(csvfile, (name,codec, megapixels, filesize, make, camera_model, image_width, image_height, exposure, fstop, iso, lensmodel, date_modified,date_created,exif_modify))
