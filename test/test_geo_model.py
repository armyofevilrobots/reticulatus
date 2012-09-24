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

    def test_slicing(self):
        """Test initial slicer prototype"""
        stl = helpers.get_box()
        model = Model.from_stl(stl)
        layers = model.generate_planar_intersections(0.4, 1, 31)

        for (zlevel, intersections) in layers:
            for intersection in intersections:
                start, end = intersection
                assert start != end




