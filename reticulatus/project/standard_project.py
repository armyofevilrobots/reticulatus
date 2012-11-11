"""
This is a project abstraction
"""
from configobj import ConfigObj
from ..geo.stl import STL
from ..geo.model import Model
from ..toolpath.layer import Layer




class Project(object):
    """Abstraction for a project, containing model, slices, config, and
    perhaps a toolpath as well."""

    def __init__(self, model=None, layers=None, config=None):
        self.model = model or None
        self.layers = layers or None
        self.perimeters = None
        self.config = config or ConfigObj()


    @classmethod
    def from_stl(cls, stl=None, config=None):
        """Generates a fresh shiny new project from an stl file."""
        if stl is None:
            return cls(config=config)
        if isinstance(stl, (str, unicode)):
            stl = STL(stl)
        if isinstance(stl, STL):
            if not len(stl.facets):
                stl.read()
            model = Model.from_stl(stl)
            return cls(model, config=config)
        else:
            raise RuntimeError, "Unknown input data: %s" % stl

    def slice(self, initial_height, layer_height, tool_width, callback=None):
        """Slice me into layers!"""
        self.layers = list()
        for plane in self.model.generate_planar_intersections(
                initial_height, layer_height, 300):
            if len(plane[1]):
                layer= Layer.from_CGAL_intersections(plane[1])
                self.layers.append(layer)




        #self.layers = [
                #Layer.from_CGAL_intersections(plane[1]) for
                    #plane in
                    #self.model.generate_planar_intersections(initial_height, layer_height, 300)
                    #if len(plane[1])]
        self.perimeters = [
                layer.eroded(tool_width/2.0)
                for layer in self.layers]


