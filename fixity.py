import os
import subprocess
import hashlib

path = sys.argv[1]
def hashlib_md5(filename, manifest):
   
   m = hashlib.md5()
   with open(str(filename), 'rb') as f:
       while True:
           buf = f.read(2**20)
           if not buf:
               break
           m.update(buf)
   md5_output = m.hexdigest()
   print os.path.basename(filename)
   
   with open(manifest, "wb") as fo:
       fo.write(md5_output + '  '  + os.path.basename(filename) +  '\n')

for root, dirnames, filenames in os.walk(path):
    for files in filenames:
        files = os.path.join(root, files)
        if not files.endswith('.md5'):
            manifest = files + '_md5.md5'
            if not os.path.isfile(manifest):
 
                hashlib_md5(files, manifest)