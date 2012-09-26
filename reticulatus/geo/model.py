"""
CGAL polygon/model wrapper for slicing
"""
from CGAL.CGAL_Kernel import Plane_3, Vector_3, Point_3
from CGAL.CGAL_Polyhedron_3 import Polyhedron_3
from CGAL.CGAL_AABB_tree import AABB_tree_Polyhedron_3_Facet_handle
import logging
from futures import ThreadPoolExecutor, ProcessPoolExecutor
from reticulatus.worker import Worker

LOGGER = logging.getLogger(__file__)

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


    def _intersection_to_segments(self, intersections, accuracy=4):
        """Generate simple list/tuple/float objects for the intersections"""
        lines = list()
        for intersection in intersections:
            obj = intersection[0]
            if obj.is_Segment_3():
                #print "Segment3"
                segment = obj.get_Segment_3()
                start = (
                        round(segment.source().x(), accuracy),
                        round(segment.source().y(), accuracy)
                        )
                end = (
                        round(segment.target().x(), accuracy),
                        round(segment.target().y(), accuracy)
                        )
                if start != end:
                    lines.append((start, end))
        return lines


    def generate_planar_intersections(self,
            start_height, inc_height, max_height, accuracy=4, processes=None):
        """Generates a series of slices from height start_height and then
        every additional inc_height units."""
        #This is a CGAL tree that makes for fast slicening!
        LOGGER.info("Start of AABB tree generation.")
        tree = AABB_tree_Polyhedron_3_Facet_handle(self.poly.facets())
        LOGGER.info("Done AABB tree generation.")
        zpos = start_height
        # This should _really_ be the max height from a bounding box eh?
        vec = Vector_3(0, 0, 1)

        def zrange(start_height, inc_height, max_height):
            positions = list()
            zpos = start_height
            while True:
                positions.append(zpos)
                zpos += inc_height
                if zpos>max_height:
                    break
            return positions


        def _slice(zpos):
            plane_query = Plane_3(Point_3(0, 0, zpos), vec)
            intersections = list()
            tree.all_intersections(plane_query, intersections)
            return (zpos,
                self._intersection_to_segments(intersections, accuracy) )

        #Surprise surprise, this is faster single threaded :(
        #I'll have to modify things to be runnable in a sub func,
        #Or maybe write my own process wrapper
        layers = map(_slice, zrange(start_height, inc_height, max_height))

        return layers




