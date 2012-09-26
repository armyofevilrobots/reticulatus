"""
Test a simple Layer object.
"""
import os
import unittest
import helpers
import cairo
import time
from multiprocessing import Pool, cpu_count

from reticulatus.worker import Worker
from reticulatus.geo.model import Model
from reticulatus.toolpath.layer import Layer



def generate_cairo_map(layer, prefix='layer', color=None):
    zlevel,intersections = layer
    ##print zlevel, intersections, prefix, color

    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1024, 1024)
    outpath = os.path.join(
        os.path.dirname(__file__),
        'out', '%s-%2.5f.png' % (prefix, zlevel))
    #outpath = os.path.join(
        #os.path.dirname(__file__),
        #'out', 'layer%2.5f.svg' % zlevel)
    #surf = cairo.SVGSurface(cairo.FORMAT_ARGB32, 256, 256)
    ctx = cairo.Context (surf)
    ctx.scale (512, 512)
    if color:
        ctx.set_source_rgb (*color)
    else:
        ctx.set_source_rgb (0.3, 0.3, 0.5)

    if len(intersections) == 0:
        return
    for intersection in intersections:
        #print intersection
        begin, last = intersection
        start = (
                0.5+round(begin[0]/20, 4),
                0.5+round(begin[1]/20, 4)
                )
        end = (
                0.5+round(last[0]/20, 4),
                0.5+round(last[1]/20, 4)
                )
        ctx.move_to(*start)
        ctx.line_to(*end)
        ctx.set_line_width (0.003)
        ctx.stroke ()
    surf.write_to_png(outpath)


def get_cairo_surf(filename):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1024, 1024)
    return surf


def draw_cairo_polys(polys, surf, color):
    ctx = cairo.Context (surf)
    ctx.scale (1024, 1024)
    ctx.set_source_rgba(*color)
    for poly in polys:
        if poly is None or not hasattr(poly, 'exterior') or poly.exterior is None:
            continue
        ctx.set_line_width (0.003)
        exterior = tuple(poly.exterior.coords)
        px, py = exterior[-1]
        px = round(0.5+(px/25),4)
        py = round(0.5+(py/25),4)
        ctx.move_to(px, py)
        for (px,py) in exterior:
            px = round(0.5+(px/25),4)
            py = round(0.5+(py/25),4)
            ctx.line_to(px, py)
            ctx.move_to(px, py)
    ctx.stroke()




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
            'out', 'stl-topview.png')
        surf.write_to_png(outpath)

        model = Model.from_stl(stl)
        #layers = model.generate_planar_intersections(-0, 1, 10)
        now=time.time()
        layers = model.generate_planar_intersections(0, 0.1, 30, processes=1)
        print "That took %5.5f seconds" % (time.time()-now)
        p = Pool(cpu_count()*4)

        now = time.time()
        p.map(generate_cairo_map, layers)
        print "That took %5.5f seconds" % (time.time()-now)


    def test_generate_insets(self):
        """Generate some layers and inset them"""
        stl = helpers.get_box()
        model = Model.from_stl(stl)
        now=time.time()
        layers = [
                Layer.from_CGAL_intersections(plane[1]) for
                    plane in
                    model.generate_planar_intersections(0, 0.1, 30)
                    if len(plane[1])]
        for layer in layers:
            eroded_layer = layer.eroded(0.2)
            for poly in eroded_layer.polys:
                exterior = tuple(poly.exterior.coords)
                self.assertEquals(exterior,
                    (
                        (9.8, -9.8), (-9.8, -9.8),
                        (-9.8, 9.8), (9.8, 9.8),
                        (9.8, -9.8)))

        print "Generating eroded layer planes took %5.5f seconds" % (time.time()-now)


    def test_complex_insets(self):
        """Test a complicated set of insets, on the head model."""
        stl = helpers.get_head()
        model = Model.from_stl(stl)
        now=time.time()
        layers = [
                (plane[0], Layer.from_CGAL_intersections(plane[1])) for
                    plane in
                    model.generate_planar_intersections(0, 0.1, 30)
                    if len(plane[1])]

        for layer in layers:
            outpath = os.path.join(
                os.path.dirname(__file__),
                'out',
                "layer-%3.3fz.png" % layer[0])
            surf = get_cairo_surf(outpath)
            polys = list(layer[1].polys)
            draw_cairo_polys(polys, surf, (0,0,0.5,1))

            for erosion in [0.15, 0.3, .45]:
                eroded = [poly.buffer(-erosion) for poly in polys]
                draw_cairo_polys(eroded, surf, (0.2, 2*erosion, 0.2, 1))

                for internal in poly.interiors:
                    draw_cairo_polys(internal, surf, (0.2, 0.2, 2*erosion, 1))
            surf.write_to_png(outpath)












