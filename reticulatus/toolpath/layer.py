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
        self.polys = polys

    def eroded(self, distance):
        return Layer(self.polys.buffer(-distance))

    @classmethod
    def from_lines(cls, lines):
        """Generates a layer from a set of lines"""
        polys = shapely.ops.polygonize(lines)
        return cls(polys)

    @classmethod
    def from_CGAL_intersections(cls, intersections, accuracy=4):
        """Returns a layer for a set of intersections"""
        assert len(intersections)
        lines = list()
        for intersection in intersections:
            obj = intersection[0]
            int_obj = intersection[1]

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
            elif obj.is_Line_3():
                print "LINE3"
            elif obj.is_Ray_3():
                print "Ray3"
            elif obj.is_Triangle_3():
                print "Triangle3"
            elif obj.is_Point_3():
                print "Poiunt3"
            else:
                print "Unknown intersection type:", intersection
        return cls.from_lines(lines)

