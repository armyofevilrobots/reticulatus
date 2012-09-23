"""
CGAL polygon/model wrapper for slicing
"""
from CGAL.CGAL_Kernel import Plane_3, Triangle_3, Vector_3, Point_3
from CGAL.CGAL_Kernel import intersection
from CGAL.CGAL_Polyhedron_3 import Polyhedron_3
from CGAL.CGAL_AABB_tree import AABB_tree_Polyhedron_3_Facet_handle, AABB_tree_Triangle_3_soup

class Model:
    """
    Basically just a wrapper on a CGAL poly, but
    to add some extra functionality.
    """
    def __init__(self, facets):
        """Facets is an iterable containing a set of x,y,z tuples"""
        self.poly = Polyhedron_3()
        for facet in facets:
            #print "Facet: ", facet
            points = [Point_3(*point) for point in facet]
            if len(points) == 3:
                self.poly.make_triangle(*points)
            #elif len(points) == 4:
                #self.poly.make_tetrahedron(*points)
            else:
                raise RuntimeError, (
                        "Invalid point list for poly facet: %d sides" %
                        len(points))
        #self.soup = list()
        #for facet in facets:
            #tri = Triangle_3(*[Point_3(*point) for point in facet])
            #self.soup.append(tri)

    @classmethod
    def from_stl(cls, stl):
        return cls(facets = (facet['p'] for facet in stl._facets))


    def generate_planar_intersections(self,
            start_height, inc_height, max_height):
        """Generates a series of slices from height start_height and then
        every additional inc_height units."""
        #This is a CGAL tree that makes for fast slicening!
        print "Slicing starting at %f every %s units until %f" % (
                start_height, inc_height, max_height)
        tree = AABB_tree_Polyhedron_3_Facet_handle(self.poly.facets())
        #tree = AABB_tree_Triangle_3_soup(self.soup)
        zpos = start_height
        # This should _really_ be the max height from a bounding box eh?
        layers = list()
        while zpos < max_height:
            print "Slicing at %d" % zpos
            vec = Vector_3(0, 0, 1)
            plane_query = Plane_3(Point_3(0, 0, zpos), vec)
            #print plane_query
            intersections = list()
            tree.all_intersections(plane_query, intersections)
            #tree.all_intersected_primitives(plane_query, intersections)
            #for intersect in intersections:

                #newint = intersection(plane_query, intersect)
                #print newint
            #print intersections
            layers.append((zpos, intersections))
            zpos += inc_height
        return layers

    def dumb_generate_planar_intersections(self,
            start_height, inc_height, max_height):
        intersections = list()
        zpos = start_height
        while zpos < max_height:
            thislayer = list()
            vec = Vector_3(0, 0, 1)
            plane_query = Plane_3(Point_3(0, 0, zpos), vec)
            for tri in self.soup:
                #print "TRI", tri, "PLANE", plane_query
                try:
                    intersect = intersection(plane_query, tri)
                except Exception, exc:
                    print "Failed to intersect at", tri, "@", zpos
                if intersect:
                    thislayer.append((intersect, tri))
            intersections.append((zpos, thislayer))

            zpos += inc_height
        return intersections


