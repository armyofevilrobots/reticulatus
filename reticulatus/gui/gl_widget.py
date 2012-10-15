"""Main UI stuffs"""
from PySide import QtOpenGL, QtCore, QtGui
#import math
import logging
from OpenGL import GL
from reticulatus.gui import icon
import math
from .shaders import get_shader
from OpenGL.GL import shaders
#from OpenGL import GLUT
#from OpenGL import GLU
#from OpenGL.GL import shaders



#QT warnings due to pep8 != QT
# pylint: disable=C0103

class GLWidget(QtOpenGL.QGLWidget):
    """GL Wrapper widget"""
    def __init__(self, parent=None):
        self.log = logging.getLogger(__name__)
        self.log.info("Generating glwidget")
        QtOpenGL.QGLWidget.__init__(self, parent)

        self.poly_line_color = QtGui.QColor.fromRgbF(0.2, 0.2, 0.1, 1)
        self.poly_fill_color =  QtGui.QColor.fromRgbF(0.4, 0.4, 0.4, 1)
        self.gl_bg_color = QtGui.QColor.fromCmykF(0.19, 0.19, 0.0, 0.0)
        self.gl_platform_color = QtGui.QColor.fromRgbF(0.5, 0.5, 0.5, 0.5)
        #self.vertex = None
        #self.fragment = None
        self.shader = None

        self.x_rot = 90.0
        self.y_rot = 0.0
        self.z_rot = 0.0

        self.x_pan = 0.0
        self.y_pan = 0.0
        self.zoom = 100.0

        self.slice_slider = None

        self.o_width = 0.0
        self.o_height = 0.0
        self.layers = [
                'wireframe',
                'polygons',
                'platform'] #Slices off by default
        self.objects = dict(
                wireframe=None, polygons=None, platform=None, slices=None)
        self.colors = dict(
                wireframe=self.poly_line_color,
                polygons=self.poly_fill_color,
                platform=self.gl_platform_color,
                _background=self.gl_bg_color)
        self._iconcache = None
        self.bottom = None
        self.top = None

        self.last_pos = QtCore.QPoint()


    def set_slice_slider(self, slider):
        """We set the slider used for slice heights"""
        self.slice_slider = slider
        self.slice_slider.valueChanged.connect(self.slider_moved)


    def slider_moved(self, _):
        """We got a change to the slider value."""
        if 'slices' in self.layers:
            self.updateGL()


    def _cleanup(self):
        """Cleans up the genlists to prevent memleaks."""
        #This part fixes a memory leak
        for _, genlist in self.objects.iteritems():
            if genlist is not None:
                GL.glDeleteLists(genlist, 1)

    def x_rotation(self):
        """Getter"""
        return self.x_rot

    def y_rotation(self):
        """Getter"""
        return self.y_rot

    def z_rotation(self):
        """Getter"""
        return self.z_rot

    def minimumSizeHint(self):
        """Getter"""
        return QtCore.QSize(50, 50)

    def sizeHint(self):
        """Getter"""
        return QtCore.QSize(400, 400)




    def set_x_rotation(self, angle):
        """Change our rotation"""
        angle = self.normalizeAngle(angle)
        if angle != self.x_rot:
            self.x_rot = angle
            #self.emit(QtCore.SIGNAL("xRotationChanged(int)"), angle)
            self.updateGL()

    def set_y_rotation(self, angle):
        """Change our rotation"""
        angle = self.normalizeAngle(angle)
        if angle != self.y_rot:
            self.y_rot = angle
            #self.emit(QtCore.SIGNAL("yRotationChanged(int)"), angle)
            self.updateGL()

    def set_z_rotation(self, angle):
        """Change our rotation"""
        angle = self.normalizeAngle(angle)
        if angle != self.z_rot:
            self.z_rot = angle
            #self.emit(QtCore.SIGNAL("zRotationChanged(int)"), angle)
            self.updateGL()

    def initializeGL(self):
        """Init"""
        self.qglClearColor(self.gl_bg_color.darker())

        #GL.glShadeModel(GL.GL_FLAT)
        GL.glEnable(GL.GL_DEPTH_TEST)

        GL.glClearDepth(1.0)

        #Fix up the lines to be cleaner...
        GL.glEnable(GL.GL_LINE_SMOOTH)
        GL.glHint(GL.GL_LINE_SMOOTH_HINT, GL.GL_NICEST)
        GL.glLineWidth(0.1)
        GL.glEnable(GL.GL_BLEND)
        GL.glEnable(GL.GL_MULTISAMPLE)
        GL.glEnable(GL.GL_LIGHTING)
        GL.glEnable(GL.GL_LIGHT0)
        GL.glEnable(GL.GL_NORMALIZE)
        GL.glEnable(GL.GL_LIGHT1)

        GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)

        #self.vertex, self.fragment = get_shader()
        #self.shader = get_shader()

        #THis is all SHAMELESSLY copied from the tutes at
        #http://pyopengl.sourceforge.net/context/tutorials/shader_5.xhtml
        #I will be gutting and replacing with something more appropriate
        #later on, but for now, let's get it running
        #for uniform in (
            #'Global_ambient',
            #'Light_ambient','Light_diffuse','Light_location',
            #'Material_ambient','Material_diffuse',
        #):
            #location = GL.glGetUniformLocation( self.shader, uniform )
            #if location in (None,-1):
                #print 'Warning, no uniform: %s'%( uniform )
            #setattr( self, uniform+ '_loc', location )
        #for attribute in (
            #'Vertex_position','Vertex_normal',
        #):
            #location = GL.glGetAttribLocation( self.shader, attribute )
            #if location in (None,-1):
                #print 'Warning, no attribute: %s'%( uniform )
            #setattr( self, attribute+ '_loc', location )
        #GL.glUseProgram(self.shader)
        #GL.glUniform4f( self.Global_ambient_loc, .3,.05,.05,.1 )

        GL.glEnable(GL.GL_COLOR_MATERIAL)

        GL.glMaterialfv(GL.GL_FRONT_AND_BACK, GL.GL_DIFFUSE, [0.6, 0.6, 0.6, 1.0])
        GL.glMaterialfv(GL.GL_FRONT_AND_BACK, GL.GL_AMBIENT, [0.3, 0.3, 0.3, 1.0])
        GL.glMaterialfv(GL.GL_FRONT_AND_BACK, GL.GL_SPECULAR, [0.5, 0.5, 0.5, 1.0])
        GL.glMaterialfv(GL.GL_FRONT_AND_BACK, GL.GL_SHININESS, 10.0)
        GL.glColorMaterial(GL.GL_FRONT_AND_BACK, GL.GL_AMBIENT_AND_DIFFUSE)
        GL.glLightModeli(
                GL.GL_LIGHT_MODEL_COLOR_CONTROL,
                GL.GL_SINGLE_COLOR
                )
        GL.glLightModeli(GL.GL_LIGHT_MODEL_TWO_SIDE, 1)


    def set_light_positions(self):
        """Set the light positions."""
        GL.glLightfv(GL.GL_LIGHT0, GL.GL_POSITION, [100, 0, -1000, 0])
        GL.glLightfv(GL.GL_LIGHT0, GL.GL_QUADRATIC_ATTENUATION, 100.0)
        GL.glLightfv(GL.GL_LIGHT0, GL.GL_AMBIENT, [0.3, 0.3, 0.3, 0])
        GL.glLightfv(GL.GL_LIGHT0, GL.GL_DIFFUSE, [0.7, 0.7, 0.7, 0])
        GL.glLightfv(GL.GL_LIGHT0, GL.GL_SPECULAR, [0.5, 0.5, 0.5, 0])

        GL.glLightfv(GL.GL_LIGHT1, GL.GL_POSITION, [-100, 0, -1000, 0])
        GL.glLightfv(GL.GL_LIGHT1, GL.GL_AMBIENT, [0.3, 0.3, 0.3, 0])
        GL.glLightfv(GL.GL_LIGHT1, GL.GL_DIFFUSE, [0.4, 0.4, 0.4, 0])
        GL.glLightfv(GL.GL_LIGHT1, GL.GL_SPECULAR, [0.4, 0.4, 0.4, 0])

    def _get_slice_height(self):
        """Helper to get the slice limits."""
        if not self.slice_slider:
            return 9999999
        else:
            return 0.005+1.0*self.slice_slider.value()


    def paintGL(self):
        """Redraw"""
        GL.glDepthFunc(GL.GL_LEQUAL)
        GL.glDepthMask(GL.GL_TRUE)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glClipPlane(GL.GL_CLIP_PLANE0,
                (0, 0, -1, self._get_slice_height()))
        GL.glLoadIdentity()
        GL.glScaled(self.zoom/100, self.zoom/100, self.zoom/100)
        self.set_light_positions()
        GL.glTranslated(self.x_pan, self.y_pan, 0.1)
        GL.glRotated(self.x_rot , 1.0, 0.0, 0.0)
        GL.glRotated(self.y_rot , 0.0, 1.0, 0.0)
        GL.glRotated(self.z_rot , 0.0, 0.0, 1.0)
        #GL.glUseProgram(0)
        if 'slices' in self.layers:
            GL.glEnable(GL.GL_CLIP_PLANE0)
        else:
            GL.glDisable(GL.GL_CLIP_PLANE0)
        for layer in sorted(self.layers):
            if layer == 'wireframe':
                GL.glPolygonMode( GL.GL_FRONT_AND_BACK, GL.GL_LINE )
            elif layer == 'clip':
                pass
            else:
                GL.glPolygonMode( GL.GL_FRONT_AND_BACK, GL.GL_FILL )
                if layer != 'platform':
                    GL.glPolygonOffset(1, 1)
            self.log.info("Painting: %s" % layer)
            if self.objects[layer] is not None:
                GL.glCallList(self.objects[layer])


    def resizeGL(self, width, height):
        """New window size."""
        self.o_width = width
        self.o_height = height
        self.log.debug("Resized gl win to %d, %d", width, height)
        side = min(width, height)
        GL.glViewport(0, 0, width, height)
        self.log.debug("Setting glviewport: %f, %f, %f, %f",
                (width - side) / 2, (height - side) / 2, side, side)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GL.glOrtho((-100.0*width)/height, (+100.0*width)/height,
                100, -100, 1500.0, -1500.0)
        GL.glMatrixMode(GL.GL_MODELVIEW)

    def mousePressEvent(self, event):
        """Push"""
        self.last_pos = QtCore.QPoint(event.pos())

    def wheelEvent(self, event):
        """We got a scroll. Change the zoom."""
        GL.glClipPlane(GL.GL_CLIP_PLANE0,
                (0, 0, -1, self._get_slice_height()))
        num_degrees = event.delta() / 8.0
        num_steps = num_degrees
        self.zoom += num_steps
        if self.zoom < 30.0:
            self.zoom = 30.0
        parent = self.window()
        parent.statusBar().showMessage("Zoom: %3.3f" % (self.zoom/100.0))


        self.updateGL()


    def mouseMoveEvent(self, event):
        """Drag, rotate."""
        dx = event.x() - self.last_pos.x()
        dy = event.y() - self.last_pos.y()

        if (
                (event.buttons() & QtCore.Qt.LeftButton)
                and not
                (event.modifiers() & QtCore.Qt.ControlModifier)):
            self.x_pan += 50*dx/self.zoom
            self.y_pan += 50*dy/self.zoom
            self.log.info("Panned to %3.3f, %3.3f", self.x_pan, self.y_pan)
            self.updateGL()
        elif (
                (event.buttons() & QtCore.Qt.RightButton)
                or
                ((event.buttons() & QtCore.Qt.LeftButton)
                    and
                    (event.modifiers() & QtCore.Qt.ControlModifier))):
            self.set_x_rotation(self.x_rot + 0.5 * dy)
            self.set_z_rotation(self.z_rot + 0.5 * dx)
            self.log.info("Now rotated to: %3.3d, %3.3d",
                    self.x_rot, self.z_rot)
        self.last_pos = QtCore.QPoint(event.pos())

    def toggle_layer(self, item):
        """We got a doubleclick on a layer, so
        we toggle it."""
        layer = item.text()
        self.log.debug("Toggling layer %s", layer)
        if layer in self.layers:
            item.setCheckState(QtCore.Qt.CheckState.Unchecked)
            self.layers.remove(layer)
        else:
            item.setCheckState(QtCore.Qt.CheckState.Checked)
            self.layers.append(layer)
        self.updateGL()


    def sync_layer(self, item):
        """We got a change state, so we do something
        to make sure the checkstate and the layer state
        match.
        Note; maybe I should refactor this to only use checkstate"""
        layer = item.text()
        if item.checkState() == QtCore.Qt.CheckState.Checked:
            if not layer in self.layers:
                self.layers.append(layer)
        else:
            if layer in self.layers:
                self.layers.remove(layer)
        self.updateGL()


    @property
    def _icons(self):
        """get/cache icons"""
        if self._iconcache:
            return self._iconcache
        ICO_PAINT = icon.by_name('paint-brush')
        ICO_LINE = icon.by_name('pencil')
        ICO_PLANE = icon.by_name('grid')
        ICO_SLICE = icon.by_name('cutter')
        self._iconcache = dict(
                wireframe=ICO_LINE,
                polygons=ICO_PAINT,
                platform=ICO_PLANE,
                slices = ICO_SLICE,
                )
        return self._iconcache


    def _sync_listwidget(self):
        """Sync the list widget in my parent to match my current layers."""
        parent = self.window()
        if not parent:
            return
        lwidg = parent.layer_list_widget
        lwidg.clear()
        layers = list(self.layers)
        #Fixup missing layers
        for layer in ['wireframe', 'polygons', 'platform', 'slices', ]:
            if not layer in layers:
                layers.append(layer)

        for layer in layers:
            if self._icons.has_key(layer):
                witem = QtGui.QListWidgetItem(self._icons[layer], layer)
            else:
                witem = QtGui.QListWidgetItem(layer)
            lwidg.addItem(
                    witem
                    )
            if layer != 'slices':
                witem.setCheckState(QtCore.Qt.CheckState.Checked)
            else:
                witem.setCheckState(QtCore.Qt.CheckState.Unchecked)
            #assert witem.icon() is not None




    def set_object(self, stl):
        """Set the object from an stl"""
        self._cleanup()
        self.objects['wireframe'] = self.load_object(stl, self.poly_line_color)
        self.objects['polygons'] = self.load_object(stl, self.poly_fill_color)
        self.objects['platform'] = self._build_plane(self.gl_platform_color)
        self._sync_listwidget()
        self.initializeGL()


    def _build_plane(self, color):
        """Build the platform plane."""
        plane_genlist = GL.glGenLists(1)
        GL.glNewList(plane_genlist, GL.GL_COMPILE)
        GL.glBegin(GL.GL_TRIANGLES)

        self.qglColor(color)
        GL.glNormal3d(0.0, 0.0, 1.0)
        GL.glVertex3d(-100.0, 100, -0.01)
        GL.glVertex3d(100.0, 100, -0.01)
        GL.glVertex3d(100.0, -100.0, -0.01)

        GL.glNormal3d(0.0, 0.0, 1.0)
        GL.glVertex3d(-100.0, 100, -0.01)
        GL.glVertex3d(100.0, -100, -0.01)
        GL.glVertex3d(-100.0, -100.0, -0.01)

        #GL.glNormal3d(0.0, 0.0, -1.0)
        #GL.glVertex3d(-101.0, 100, 0.0001)
        #GL.glVertex3d(101.0, 100, 0.0001)
        #GL.glVertex3d(101.0, -101.0, 0.0001)

        #GL.glNormal3d(0.0, 0.0, -1.0)
        #GL.glVertex3d(-101.0, 100, 0.0001)
        #GL.glVertex3d(101.0, -100, 0.0001)
        #GL.glVertex3d(-101.0, -101.0, 0.0001)

        GL.glEnd()
        GL.glEndList()
        return plane_genlist


    def load_object(self, stl, color):
        """Loads the object from an stl."""
        self.bottom = None
        self.top = None
        obj_genlist = GL.glGenLists(1)
        GL.glNewList(obj_genlist, GL.GL_COMPILE)

        GL.glBegin(GL.GL_TRIANGLES)

        self.qglColor(color)
        self.log.info("This STL has %d facets", len(stl.facets))
        for facet in stl.facets:
            GL.glNormal3d(*facet['n'])
            for point in facet['p']:
                #self.log.debug('Adding point %s', point)
                if point[2] < self.bottom or self.bottom is None:
                    self.bottom = point[2]
                if point[2] > self.top or self.bottom is None:
                    self.top = point[2]
                GL.glVertex3d(*point)


        GL.glEnd()
        GL.glEndList()

        if self.slice_slider is not None:
            self.slice_slider.setMinimum(math.floor(self.bottom))
            self.slice_slider.setMaximum(math.ceil(self.top))


        return obj_genlist

    def normalizeAngle(self, angle):
        """Keep in 0-360"""
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle
