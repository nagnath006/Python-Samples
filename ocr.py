from os import listdir
from os.path import isfile, join
import sys
import os
import subprocess
import glob


dira = '/home/devuser/Documents/9780123814654.pdf'
root= '/home/devuser/Documents/OCR/'
command = "pdfimages"+ ' ' +"-j" + ' ' + dira + ' ' + root + '/' + "images"
os.system(command)
print "#############################PDF TO IMG Conversion Complete##########################################"
files = [f for f in listdir(root) if isfile(join(root, f))]

for x in files:
    imagefile = root + '/' + x
    y = str(x)
    command = "tesseract"+ ' ' + imagefile + ' ' + root + "output" +'/'+ "out" + y
    print command
    os.system(command)
print "############################Tessesract Work has done#################################################"
read_files = glob.glob("*.txt")
print read_files
with open(root + "output" +'/'+"result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())





