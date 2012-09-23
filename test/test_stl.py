"""Test STL"""
from reticulatus.geo.stl import STL
import os
import unittest


class TestSTL(unittest.TestCase):
    """Test the STL"""

    def test_20mm_cube(self):
        """Load a small model?"""
        stl = STL(os.path.join(os.path.dirname(__file__),
            'data', '20mmbox.stl'))
        #stl.debug = True

        type = stl.type()
        print "Type is: ", type
        if type == "binary":
            print "Length is: ", stl.length()
            print "Header:"
            print stl.header()
        self.assertEquals(type, 'binary')
        stl.read()


    def test_my_head(self):
        """Does it load a huge model OK?"""
        stl = STL(os.path.join(os.path.dirname(__file__),
            'data', 'derekhead.stl'))
        type = stl.type()
        print "Type is: ", type
        if type == "binary":
            print stl.header()
            print "Length is: ", stl.length()
        stl.read()
        self.assertEquals(type, 'binary')
        self.assertEquals(stl.length(), 33326)

    def test_cgal_poly(self):
        """Does it generate a POLY ok?"""
        stl = STL(os.path.join(os.path.dirname(__file__),
            'data', '20mmbox.stl'))
        stl.read()
        stl.to_cgal_polys()

    def test_slicing(self):
        """Test initial slicer prototype"""
        stl = STL(os.path.join(os.path.dirname(__file__),
            'data', 'derekhead.stl'))
        stl.read()
        layers = stl.generate_planar_intersections(0.4, 1, 31)

        for (zlevel, intersections) in layers:
            if len(intersections):
                print "LAYER: ", zlevel
            for intersection in intersections:
                obj = intersection[0]
                if obj.is_Segment_3():
                    segment = obj.get_Segment_3()
                    #print "Line intersection", segment
                    print "Line from: ", segment.source(), "to", segment.target()




        assert False






