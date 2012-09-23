"""Setup stub for reticulatus"""

from setuptools import setup, find_packages
import sys, os

VERSION = '0.0'

setup(name='reticulatus',
      VERSION=VERSION,
      description="Post-processor for 3d printing G-code.",
      long_description="""\
Performs various cleanups including:
 - Fixing gaps in shallow domes or low angle top surfaces
 - Intelligent support structure for internal/external overhangs
 - Ramping and arced entries to extrusions
 - Predictive Hooke's law extrusion starts
 - Other things I haven't thought of yet.
""",
      classifiers=[],
      keywords='reprap cnc gcode slic3r skeinforge',
      author='Derek Anderson',
      author_email='derek@armyofevilrobots.com',
      url='http://www.armyofevilrobots.com/',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'numpy',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
