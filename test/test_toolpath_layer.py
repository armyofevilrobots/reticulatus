"""
Test a simple Layer object.
"""
import os
import unittest
import helpers
import cairo

from reticulatus.geo.model import Model
from reticulatus.toolpath.layer import Layer

class TestLayer(unittest.TestCase):
    """Test the Layer"""

    def test_generate_layers(self):
        """Generate some layers and validate them"""
        stl = helpers.get_head()
        surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1024, 1024)
        ctx = cairo.Context (surf)
        ctx.scale (1024, 1024)
        ctx.set_source_rgb (0.8, 0.2, 0.5)
        for facet in stl._facets:
            x,y,z = facet['p'][0]
            ctx.move_to(0.5+x/30, 0.5+y/30)

            x,y,z = facet['p'][1]
            ctx.line_to(0.5+x/30,0.5+y/30)
            x,y,z = facet['p'][2]
            ctx.line_to(0.5+x/30,0.5+y/30)
        ctx.set_line_width (0.001)
        ctx.stroke()

        outpath = os.path.join(
            os.path.dirname(__file__),
            'out', 'stl-cube.png')
        surf.write_to_png(outpath)

        model = Model.from_stl(stl)
        #layers = model.generate_planar_intersections(-0, 1, 10)
        layers = model.generate_planar_intersections(0, 0.5, 30)

        for (zlevel, intersections) in layers:
            surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1024, 1024)
            ctx = cairo.Context (surf)
            ctx.scale (1024, 1024)
            ctx.set_source_rgb (0.3, 0.3, 0.5)
            if len(intersections) == 0:
                continue
            for intersection in intersections:
                obj = intersection[0]
                if obj.is_Segment_3():
                    segment = obj.get_Segment_3()
                    start = (
                            0.5+round(segment.source().x()/20, 4),
                            0.5+round(segment.source().y()/20, 4)
                            )
                    end = (
                            0.5+round(segment.target().x()/20, 4),
                            0.5+round(segment.target().y()/20, 4)
                            )
                    ctx.move_to(*start)
                    ctx.line_to(*end)
                    ctx.set_line_width (0.003)
                    ctx.stroke ()

            outpath = os.path.join(
                os.path.dirname(__file__),
                'out', 'layer%2.5f.png' % zlevel)
            surf.write_to_png(outpath)

            layer = Layer.from_CGAL_intersections(intersections)
            #eroded = [poly.eroded(0.2) for poly in layer.polys]







