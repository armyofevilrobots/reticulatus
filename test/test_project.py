"""Tests the Project"""
from reticulatus.geo.model import Model
from reticulatus.project import Project
import unittest
import helpers

class TestProject(unittest.TestCase):
    """Test the Project"""

    def test_stl2project_(self):
        """Test loading an stl and making a project"""
        stl = helpers.get_box()
        prj = Project.from_stl(stl)
        print prj, prj.model







