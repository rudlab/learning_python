#!/usr/bin/python
# This Python file uses the following encoding: utf-8

import time
import datetime
ts = time.time()
my_time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

import subprocess

#útihiti
celsius1 = subprocess.check_output("ssh pi@russell -p 22202 'python /home/pi/pyprog/get_one_temp.py 1'", shell=True)

#innihiti
celsius2 = subprocess.check_output("ssh pi@russell -p 22202 'python /home/pi/pyprog/get_one_temp.py 0'", shell=True)

#frystiskápur
celsius3 = subprocess.check_output("ssh pi@russell -p 22202 'python /home/pi/pyprog/get_one_temp.py 2'", shell=True)


def nrmlz(realval):
	realval = float(realval)
        min = -20
        max = 30
        range = max - min
        ajusted = realval-min
        normalized = float(ajusted) / range;
        return normalized;

import matplotlib.pyplot as plt
import matplotlib as mpl
cmap = mpl.cm.coolwarm



"""
Fyrirmynd : http://matplotlib.org/examples/pylab_examples/custom_ticker1.html
"""


x_punktar = range(1,4)

my_label1 = 'Úti' +     ' ('+str(celsius1).strip()+' °C)'
my_label2 = 'Inni' +    ' ('+str(celsius2).strip()+' °C)'
my_label3 = 'Frystir' + ' ('+str(celsius3).strip()+' °C)'

my_title = 'Hitastig í og við bílskúr'
my_ylabel ='°C'
my_xlabel ='Mæling ' + my_time;
my_data = (float(celsius1),float(celsius2),float(celsius3))
my_labels = (my_label1.decode('utf-8'),my_label2.decode('utf-8'),my_label3.decode('utf-8')) 
#my_colors = ('green','red','blue')
my_colors = (cmap(nrmlz(celsius1)),cmap(nrmlz(celsius2)),cmap(nrmlz(celsius3)))

plt.bar(x_punktar,my_data,align='center',label=my_labels,color=my_colors)
plt.grid(axis='y')
plt.axhline(0, color='black')
plt.xticks(x_punktar ,my_labels)
plt.title(my_title.decode('utf-8'))
plt.ylabel(my_ylabel.decode('utf-8'))
plt.xlabel(my_xlabel.decode('utf-8'))

plt.savefig("/Users/baldure/learning_python/garagetemp.png")
