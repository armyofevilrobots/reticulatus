"""
CGAL polygon/model wrapper for slicing
"""
from CGAL.CGAL_Kernel import Plane_3, Vector_3, Point_3
from CGAL.CGAL_Polyhedron_3 import Polyhedron_3
from CGAL.CGAL_AABB_tree import AABB_tree_Polyhedron_3_Facet_handle
import logging

_logger = logging.getLogger(__file__)

class Model:
    """
    Basically just a wrapper on a CGAL poly, but
    to add some extra functionality.
    """
    def __init__(self, facets):
        """Facets is an iterable containing a set of x,y,z tuples"""
        self.poly = Polyhedron_3()
        for facet in facets:
            #Yes yes yes, I know, * magic, but it's _FASTER_
            points = [Point_3(*point) for point in facet]
            if len(points) == 3:
                self.poly.make_triangle(*points)
            else:
                raise RuntimeError, (
                        "Invalid point list for poly facet: %d sides" %
                        len(points))

    @classmethod
    def from_stl(cls, stl):
        """Generates a Model from an STL"""
        return cls(facets = (facet['p'] for facet in stl.facets))


    def generate_planar_intersections(self,
            start_height, inc_height, max_height):
        """Generates a series of slices from height start_height and then
        every additional inc_height units."""
        #This is a CGAL tree that makes for fast slicening!
        _logger.info("Start of AABB tree generation.")
        tree = AABB_tree_Polyhedron_3_Facet_handle(self.poly.facets())
        _logger.info("Done AABB tree generation.")
        zpos = start_height
        # This should _really_ be the max height from a bounding box eh?
        layers = list()
        while zpos < max_height:
            vec = Vector_3(0, 0, 1)
            plane_query = Plane_3(Point_3(0, 0, zpos), vec)
            intersections = list()
            tree.all_intersections(plane_query, intersections)
            layers.append((zpos, intersections))
            zpos += inc_height
        return layers

