#!/usr/bin/env python

import os
import sys

from pybles import pybles

def xx(size, global_size):
	return size * 100 / global_size

total_size = 0
dires = []

for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
#for (dirpath, dirnames, filenames) in os.walk('/home/guido/Documents/GuidoAccardo/stuff/'):
	dires.append(dirpath)

global_size = 0

for (dirpath, dirnames, filenames) in os.walk(dires[0]):
	for f in filenames:
		fp = os.path.join(dirpath, f)
		global_size += os.path.getsize(fp)

paths = list()

for ddir in dires:
	total_size = 0
	for (dirpath, dirnames, filenames) in os.walk(ddir):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			total_size += os.path.getsize(fp)

	paths.append( (ddir, total_size) )
	
paths.remove( paths[0] )

pyb = pybles.Pyble()

pyb.add_column('path')
pyb.add_column('size prepresentation')
pyb.add_column('size in %')

for pp in paths:
	pyb.add_line([pp[0][20:], "X" * xx(pp[1], global_size), "%s%%" % xx(pp[1], global_size)])

pyb.show_table()
