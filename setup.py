#from distutils.core import setup
from setuptools import setup
from setuptools import setup
from distutils.command.install import install as _install

import os
import sys

def _post_install(dir):
    from subprocess import call
    print os.path.join(dir, 'space')
    call([sys.executable, 'create_bin.py', os.path.join(dir, 'space')],
         cwd=os.path.join(dir, 'space'))


class install(_install):
    def run(self):
        _install.run(self)
        self.execute(_post_install, (self.install_lib,),
                     msg="Running post install task")



setup(
    name='Space',
    version='1.0.2',
    author='Guido Accardo',
    author_email='gaccardo@gmail.com',
    mantainer='Guido Accardo',
    mantainer_email='gaccardo@gmail.com',
    home_page='http://pypi.python.org/pypi/Space/',
    symmary='',
    platform='Multiarch',
    packages=['space'],
    url='http://pypi.python.org/pypi/Pybles/',
    license='LICENSE.txt',
    cmdclass={'install': install},
    description='',
    long_description=open('README.txt').read(),
    )
