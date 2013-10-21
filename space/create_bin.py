#!/usr/bin/env python

import shutil
import sys
import subprocess

print "Copying binaries"
try:
  shutil.copyfile("%s/space.py" % sys.argv[1], '/usr/bin/space')
  subprocess.call(['chmod', 'a+x', "/usr/bin/space"])
except IOError:
  print "You don' have permissions to perform this installation. Please, run this installation as root"
