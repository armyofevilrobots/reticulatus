"""Test STL"""
from reticulatus.geo.stl import STL
import os
import unittest


class TestSTL(unittest.TestCase):
    """Test the STL"""

    def test_20mm_cube_asc(self):
        """Load a small model?"""
        stl = STL(os.path.join(os.path.dirname(__file__),
            'data', '20mmboxasc.stl'))
        stl.debug = True
        type = stl.type()
        self.assertEquals(type, 'ascii')
        stl.read()
        stl.dump()

    def test_20mm_cube_bin(self):
        """Load a small model?"""
        stl = STL(os.path.join(os.path.dirname(__file__),
            'data', '20mmbox.stl'))
        stl.debug = True
        type = stl.type()
        self.assertEquals(type, 'binary')
        stl.read()
        stl.dump()

    def test_my_head(self):
        """Does it load a huge model OK?"""
        stl = STL(os.path.join(os.path.dirname(__file__),
            'data', 'derekhead.stl'))
        type = stl.type()
        if type == "binary":
            print stl.header()
            print "Length is: ", stl.length()
        stl.read()
        self.assertEquals(type, 'binary')
        self.assertEquals(stl.length(), 33326)

