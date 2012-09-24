"""Setup stub for reticulatus"""

from setuptools import setup, find_packages
import sys

VERSION = '0.0'
REQUIRES = [ 'configobj', 'futures']

if float(sys.version[:3]) < 2.7:
    REQUIRES.append('argparse')

setup(name='reticulatus',
      VERSION=VERSION,
      description="Another slicer, in python, and fast!",
      long_description="""High speed python based slicer,
      with NO skeinforge dependencies.""",
      classifiers=[],
      keywords='reprap cnc gcode slic3r skeinforge',
      author='Derek Anderson',
      author_email='derek@armyofevilrobots.com',
      url='http://www.armyofevilrobots.com/',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe = True,
      install_requires = REQUIRES,
      entry_points={
          'console_scripts': [
              'reticulate = reticulatus.scripts.reticulate:main',
              ]
          }
      )
