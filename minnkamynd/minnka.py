#! /usr/bin/python

import os

filenamefile = open("tobig.txt", "r")
filenames = [word for line in filenamefile for word in line.split()];
filenamefile.close()

for filename in filenames:
   command = "convert "+filename+" -resize 720 "+filename
   response = os.system(command)
   print response

