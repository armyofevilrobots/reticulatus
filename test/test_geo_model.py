"""Tests the Model"""
from reticulatus.geo.model import Model
import unittest
import helpers

class TestModel(unittest.TestCase):
    """Test the Model"""

    def test_stl2model(self):
        """Test loading an stl and making a model"""
        stl = helpers.get_box()
        model = Model.from_stl(stl)
        print model

    def test_slicing(self):
        """Test initial slicer prototype"""
        stl = helpers.get_box()
        model = Model.from_stl(stl)
        layers = model.generate_planar_intersections(0.4, 1, 31)

        for (zlevel, intersections) in layers:
            if len(intersections):
                print "LAYER: ", zlevel
            for intersection in intersections:
                obj = intersection[0]
                if obj.is_Segment_3():
                    segment = obj.get_Segment_3()
                    start = segment.source()
                    end = segment.target()
                    assert start != end
        assert False




