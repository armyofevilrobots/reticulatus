from reticulatus.geo.stl import STL
from reticulatus.geo.model import Model
import os
import unittest

class TestModel(unittest.TestCase):
    """Test the Model"""

    def _get_box(self):
        stl = STL(os.path.join(os.path.dirname(__file__),
            'data', '20mmbox.stl'))
        stl.read()
        return stl

    def _get_head(self):
        stl = STL(os.path.join(os.path.dirname(__file__),
            'data', 'derekhead.stl'))
        stl.read()
        return stl

    def test_stl2model(self):
        stl = self._get_box()
        model = Model.from_stl(stl)
        print model

    def test_slicing(self):
        """Test initial slicer prototype"""
        stl = self._get_head()
        model = Model.from_stl(stl)
        layers = model.generate_planar_intersections(0.4, 1, 31)

        for (zlevel, intersections) in layers:
            if len(intersections):
                print "LAYER: ", zlevel
            for intersection in intersections:
                obj = intersection[0]
                if obj.is_Segment_3():
                    segment = obj.get_Segment_3()
                    #print "Line intersection", segment
                    #print "Line from: ", segment.source(), "to", segment.target()
                    start = segment.source()
                    end = segment.target()
                    #print "HXYZ: ",start.x(), start.y(), start.z()
        #assert False



