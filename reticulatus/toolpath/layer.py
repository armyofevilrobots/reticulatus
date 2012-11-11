"""
Represents a single layer based on slices from the 3d model.
"""
import shapely.ops

class Layer:
    """
    Class that represents a single layer from a 3d model.
    Doesn't have _any_ pre-knowledge of zpos/thickness
    or tool, so that we can have multiple passes on the
    same layer with different tools/processes.
    """

    def __init__(self, polys):
        self.polys = tuple(polys)

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
        polys = shapely.ops.polygonize(lines)
        return cls(polys)

    @classmethod
    def from_CGAL_intersections(cls, intersections):
        """Returns a layer for a set of intersections"""
        assert len(intersections)
        lines = intersections or list()
        return cls.from_lines(lines)

