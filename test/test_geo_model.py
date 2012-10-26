"""Tests the Model"""
from reticulatus.geo.model import Model
import unittest
import helpers

#This mesh is the simplest box, and is used for
#testing the mesh tools.

BOX_MODEL_OUT = [
        ((
            (9.999995, 9.999994, 0.0),
            (9.999995, -9.999995, 0.0),
            (-9.999996, -9.999993, 0.0)
            ), (0.0, -0.0, -1.0)),
        ((
            (9.999995, 9.999994, 0.0),
            (-9.999996, -9.999993, 0.0),
            (-9.999991, 9.999999, 0.0)
            ), (-0.0, 0.0, -1.0)),
        ((
            (10.0, 9.99999, 10.0),
            (-9.999994, 9.999995, 10.0),
            (-9.999999, -9.999991, 10.0)
            ), (0.0, 0.0, 1.0)),
        ((
            (10.0, 9.99999, 10.0),
            (-9.999999, -9.999991, 10.0),
            (9.999989, -10.0, 10.0)
            ), (0.0, 0.0, 1.0)),
        ((
            (9.999995, 9.999994, 0.0),
            (10.0, 9.99999, 10.0),
            (9.999989, -10.0, 10.0)
            ), (1.0, -5.722048e-07, -4.768374e-07)),
        ((
            (9.999995, 9.999994, 0.0),
            (9.999989, -10.0, 10.0),
            (9.999995, -9.999995, 0.0)
            ), (1.0, 0.0, 6.675721e-07)),
        ((
            (9.999995, -9.999995, 0.0),
            (9.999989, -10.0, 10.0),
            (-9.999999, -9.999991, 10.0)
            ), (-4.768374e-07, -1.0, -5.72205e-07)),
        ((
            (9.999995, -9.999995, 0.0),
            (-9.999999, -9.999991, 10.0),
            (-9.999996, -9.999993, 0.0)
            ), (-9.536747e-08, -1.0, 1.907349e-07)),
        ((
            (-9.999996, -9.999993, 0.0),
            (-9.999999, -9.999991, 10.0),
            (-9.999994, 9.999995, 10.0)
            ), (-1.0, 2.384187e-07, -2.861023e-07)),
        ((
            (-9.999996, -9.999993, 0.0),
            (-9.999994, 9.999995, 10.0),
            (-9.999991, 9.999999, 0.0)
            ), (-1.0, 2.384187e-07, -2.861022e-07)),
        ((
            (10.0, 9.99999, 10.0),
            (9.999995, 9.999994, 0.0),
            (-9.999991, 9.999999, 0.0)
            ), (2.384187e-07, 1.0, 4.76837e-07)),
        ((
            (10.0, 9.99999, 10.0),
            (-9.999991, 9.999999, 0.0),
            (-9.999994, 9.999995, 10.0)
            ), (2.861024e-07, 1.0, 3.814698e-07))]

class TestModel(unittest.TestCase):
    """Test the Model"""

    def test_stl2model(self):
        """Test loading an stl and making a model"""
        stl = helpers.get_box()
        model = Model.from_stl(stl)

    def test_model_numpy(self):
        """Test that the numpy model is structured right."""
        stl = helpers.get_box()
        model = Model.from_stl(stl)
        self.assertEquals(BOX_MODEL_OUT, model.mesh)



    def test_slicing(self):
        """Test initial slicer prototype"""
        stl = helpers.get_box()
        model = Model.from_stl(stl)
        layers = model.generate_planar_intersections(0.4, 1, 31)

        for (zlevel, intersections) in layers:
            for intersection in intersections:
                start, end = intersection
                assert start != end




