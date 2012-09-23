"""Helper functions"""
import os
from reticulatus.geo.stl import STL

def get_box():
    """Gets the box (small model)"""
    stl = STL(os.path.join(os.path.dirname(__file__),
        'data', '20mmboxasc.stl'))
    stl.read()
    return stl

def get_head():
    """Gets the head (big model)"""
    stl = STL(os.path.join(os.path.dirname(__file__),
        'data', 'derekheadasc.stl'))
    stl.read()
    return stl
