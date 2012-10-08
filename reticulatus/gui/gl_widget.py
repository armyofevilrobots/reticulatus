"""Main UI stuffs"""
from PySide import QtOpenGL, QtCore, QtGui
import math
import logging
from OpenGL import GL
from OpenGL import GLUT
from OpenGL import GLU
from OpenGL.GL import shaders



#QT warnings due to pep8 != QT
# pylint: disable=C0103

class GLWidget(QtOpenGL.QGLWidget):
    """GL Wrapper widget"""
    def __init__(self, parent=None):
        self.log = logging.getLogger(__name__)
        self.log.info("Generating glwidget")
        QtOpenGL.QGLWidget.__init__(self, parent)

        self.wireframe = None
        self.x_rot = 90.0
        self.y_rot = 0.0
        self.z_rot = 0.0

        self.x_pan = 0.0
        self.y_pan = 0.0
        self.zoom = 100.0

        self.o_width = 0.0
        self.o_height = 0.0
        self.layers = ['wireframe', 'polys']

        self.last_pos = QtCore.QPoint()
        self.wireframe = None
        self.polygons = None

        self.poly_line_color = QtGui.QColor.fromCmykF(0.40, 0.0, 1.0, 0.3)
        self.poly_fill_color =  QtGui.QColor.fromCmykF(0.40, 0.8, 1.0, 0.0)
        self.gl_bg_color = QtGui.QColor.fromCmykF(0.19, 0.19, 0.0, 0.0)

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
            #self.emit(QtCore.SIGNAL("x_rotationChanged(int)"), angle)
            self.updateGL()

    def set_y_rotation(self, angle):
        """Change our rotation"""
        angle = self.normalizeAngle(angle)
        if angle != self.y_rot:
            self.y_rot = angle
            #self.emit(QtCore.SIGNAL("y_rotationChanged(int)"), angle)
            self.updateGL()

    def set_z_rotation(self, angle):
        """Change our rotation"""
        angle = self.normalizeAngle(angle)
        if angle != self.z_rot:
            self.z_rot = angle
            #self.emit(QtCore.SIGNAL("z_rotationChanged(int)"), angle)
            self.updateGL()

    def initializeGL(self):
        """Init"""
        self.qglClearColor(self.gl_bg_color.darker())
        GL.glShadeModel(GL.GL_FLAT)
        GL.glEnable(GL.GL_DEPTH_TEST)
        #GL.glEnable(GL.GL_AUTO_NORMAL)
        GL.glClearDepth(1.0)

        GL.glEnable(GL.GL_CULL_FACE)
        #GL.glPolygonMode( GL.GL_FRONT_AND_BACK, GL.GL_LINE );
        #GL.glPolygonMode( GL.GL_FRONT, GL.GL_LINE );

    def paintGL(self):
        """Redraw"""
        GL.glDepthFunc(GL.GL_LEQUAL);
        GL.glDepthMask(GL.GL_TRUE);
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glLoadIdentity()
        GL.glScaled(self.zoom/100, self.zoom/100, self.zoom/100)
        GL.glTranslated(self.x_pan, self.y_pan, 0.1)
        GL.glRotated(self.x_rot , 1.0, 0.0, 0.0)
        GL.glRotated(self.y_rot , 0.0, 1.0, 0.0)
        GL.glRotated(self.z_rot , 0.0, 0.0, 1.0)
        if 'polys' in self.layers:
            GL.glPolygonOffset(1, 1);
            GL.glEnable(GL.GL_POLYGON_OFFSET_FILL);
            if self.polygons is not None:
                GL.glPolygonMode( GL.GL_FRONT, GL.GL_FILL );
                GL.glCallList(self.polygons)
        if 'wireframe' in self.layers:
            if self.wireframe is not None:
                GL.glPolygonMode( GL.GL_FRONT, GL.GL_LINE );
                GL.glCallList(self.wireframe)

    def resizeGL(self, width, height):
        """New window size."""
        self.o_width = width
        self.o_height = height
        self.log.debug("Resized gl win to %d, %d", width, height)
        side = min(width, height)
        GL.glViewport(0, 0, width, height)
        self.log.debug("Setting glviewport: %f, %f, %f, %f", (width - side) / 2, (height - side) / 2, side, side)
        #GL.glViewport(width,height, width, height)

        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        #GLU.gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)
        GL.glOrtho((-100.0*width)/height, (+100.0*width)/height, 100, -100, 1500.0, -1500.0)
        GL.glMatrixMode(GL.GL_MODELVIEW)

    def mousePressEvent(self, event):
        """Push"""
        self.last_pos = QtCore.QPoint(event.pos())

    def wheelEvent(self, event):
        num_degrees = event.delta() / 8.0
        num_steps = num_degrees
        self.zoom += num_steps
        if self.zoom < 100.0:
            self.zoom = 100.0
        self.updateGL()


    def mouseMoveEvent(self, event):
        """Drag, rotate."""
        dx = event.x() - self.last_pos.x()
        dy = event.y() - self.last_pos.y()

        if event.buttons() & QtCore.Qt.LeftButton:
            self.x_pan += 50*dx/self.zoom
            self.y_pan += 50*dy/self.zoom
            self.log.info("Panned to %3.3f, %3.3f", self.x_pan, self.y_pan)
            self.updateGL()
        elif event.buttons() & QtCore.Qt.RightButton:
            self.set_x_rotation(self.x_rot - 0.5 * dy)
            self.set_z_rotation(self.z_rot + 0.5 * dx)
            self.log.info("Now rotated to: %3.3d, %3.3d", self.x_rot, self.z_rot)
        self.last_pos = QtCore.QPoint(event.pos())


    def set_object(self, stl):
        """Set the object from an stl"""
        self.wireframe = self.load_object(stl, self.poly_line_color)
        self.polygons = self.load_object(stl, self.poly_fill_color)
        assert self.wireframe is not None
        self.initializeGL()
        self.log.info("Set GL object to (dump) %s", self.wireframe)


    def load_object(self, stl, color):
        """Loads the object from an stl."""
        genList = GL.glGenLists(1)
        GL.glNewList(genList, GL.GL_COMPILE)

        GL.glBegin(GL.GL_TRIANGLES)

        self.qglColor(color)
        self.log.info("This STL has %d facets", len(stl.facets))
        for facet in stl.facets:
            GL.glNormal3d(*facet['n'])
            for point in facet['p']:
                #self.log.debug('Adding point %s', point)
                GL.glVertex3d(*point)

        GL.glEnd()
        GL.glEndList()

        return genList


    def extrude(self, x1, y1, x2, y2):
        """Extrude a wall"""
        self.qglColor(self.poly_line_color.darker(250 + int(100 * x1)))

        GL.glVertex3d(x1, y1, +0.05)
        GL.glVertex3d(x2, y2, +0.05)
        GL.glVertex3d(x2, y2, -0.05)
        GL.glVertex3d(x1, y1, -0.05)

    def normalizeAngle(self, angle):
        """Keep in 0-360"""
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle
