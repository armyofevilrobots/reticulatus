"""
Represents a single layer based on slices from the 3d model.
"""
import shapely.ops
from shapely.geometry import MultiPolygon

class Layer:
    """
    Class that represents a single layer from a 3d model.
    Doesn't have _any_ pre-knowledge of zpos/thickness
    or tool, so that we can have multiple passes on the
    same layer with different tools/processes.
    """

    def __init__(self, polys):
        self.polys = polys
        #if isinstance(polys, MultiPolygon):
            #self.polys = polys #Now expect multipolygon
        #else:
            #self.polys = polys



    def __repr__(self):
        """Something pretty to show."""
        #return "|".join([str(
            #tuple(poly.exterior.coords)) for
            #poly in self.polys])
        return str([
            tuple(poly.exterior.coords) for poly in
            self.polys])


    def eroded(self, distance):
        """Generates eroded polys"""
        newpolys = list()
        for poly in self.polys:
            newpoly = poly.buffer(-distance)
            if newpoly:
                newpolys.append(newpoly)
        return Layer(newpolys)


    @classmethod
    def from_lines(cls, lines):
        """Generates a layer from a set of lines"""
        polys = tuple(shapely.ops.polygonize(lines))
        #boundary = polys[0]
        #for poly in polys[1:]:
            #boundary = boundary.symmetric_difference(poly)
        #polys = boundary
        return cls(polys)

    @classmethod
    def from_CGAL_intersections(cls, intersections):
        """Returns a layer for a set of intersections"""
        assert len(intersections)
        lines = intersections or list()
        return cls.from_lines(lines)

