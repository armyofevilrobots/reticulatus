"""Main UI stuffs"""
from PySide import QtOpenGL, QtCore, QtGui
import math
import logging
from OpenGL import GL
from OpenGL.GL import shaders



#QT warnings due to pep8 != QT
# pylint: disable=C0103

class GLWidget(QtOpenGL.QGLWidget):
    """GL Wrapper widget"""
    def __init__(self, parent=None):
        self.log = logging.getLogger(__name__)
        self.log.info("Generating glwidget")
        QtOpenGL.QGLWidget.__init__(self, parent)

        self.object = None
        self.x_rot = 0
        self.y_rot = 0
        self.z_rot = 0

        self.last_pos = QtCore.QPoint()

        self.troll_tech_green = QtGui.QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.troll_tech_purple = QtGui.QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)

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
            self.emit(QtCore.SIGNAL("x_rotationChanged(int)"), angle)
            self.updateGL()

    def set_y_rotation(self, angle):
        """Change our rotation"""
        angle = self.normalizeAngle(angle)
        if angle != self.y_rot:
            self.y_rot = angle
            self.emit(QtCore.SIGNAL("y_rotationChanged(int)"), angle)
            self.updateGL()

    def set_z_rotation(self, angle):
        """Change our rotation"""
        angle = self.normalizeAngle(angle)
        if angle != self.z_rot:
            self.z_rot = angle
            self.emit(QtCore.SIGNAL("z_rotationChanged(int)"), angle)
            self.updateGL()

    def initializeGL(self):
        """Init"""
        self.qglClearColor(self.troll_tech_purple.darker())
        GL.glShadeModel(GL.GL_FLAT)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_CULL_FACE)
        GL.glPolygonMode( GL.GL_FRONT_AND_BACK, GL.GL_LINE );

    def paintGL(self):
        """Redraw"""
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glLoadIdentity()
        GL.glTranslated(0.0, 0.0, -10.0)
        GL.glRotated(self.x_rot / 16.0, 1.0, 0.0, 0.0)
        GL.glRotated(self.y_rot / 16.0, 0.0, 1.0, 0.0)
        GL.glRotated(self.z_rot / 16.0, 0.0, 0.0, 1.0)
        if self.object is not None:
            GL.glCallList(self.object)

    def resizeGL(self, width, height):
        """New window size."""
        self.log.debug("Resized gl win to %d, %d", width, height)
        side = min(width, height)
        GL.glViewport((width - side) / 2, (height - side) / 2, side, side)

        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        #GL.glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0)
        GL.glOrtho(-20, +20, +20, -20, -80.0, 80.0)
        GL.glMatrixMode(GL.GL_MODELVIEW)

    def mousePressEvent(self, event):
        """Push"""
        self.last_pos = QtCore.QPoint(event.pos())

    def mouseMoveEvent(self, event):
        """Drag, rotate."""
        dx = event.x() - self.last_pos.x()
        dy = event.y() - self.last_pos.y()

        if event.buttons() & QtCore.Qt.LeftButton:
            self.set_x_rotation(self.x_rot - 8 * dy)
            self.set_y_rotation(self.y_rot + 8 * dx)
            self.log.info("Rotated to xy: : %3.2f,%3.2f", self.x_rot - 8 * dy, self.y_rot + 8 * dx)
        elif event.buttons() & QtCore.Qt.RightButton:
            #TODO: Pan instead of rotate
            self.set_x_rotation(self.x_rot - 8 * dy)
            self.set_z_rotation(self.z_rot + 8 * dx)
        self.last_pos = QtCore.QPoint(event.pos())


    def set_object(self, stl):
        """Set the object from an stl"""
        self.object = self.load_object(stl)
        assert object is not None
        self.initializeGL()
        self.log.info("Set GL object to (dump) %s", self.object)


    def load_object(self, stl):
        """Loads the object from an stl."""
        genList = GL.glGenLists(1)
        GL.glNewList(genList, GL.GL_COMPILE)

        GL.glBegin(GL.GL_TRIANGLES)

        self.qglColor(self.troll_tech_green)
        self.log.info("This STL has %d facets", len(stl.facets))
        for facet in stl.facets:
            for point in facet['p']:
                #self.log.debug('Adding point %s', point)
                GL.glVertex3d(*point)

        GL.glEnd()
        GL.glEndList()

        return genList


    def extrude(self, x1, y1, x2, y2):
        """Extrude a wall"""
        self.qglColor(self.troll_tech_green.darker(250 + int(100 * x1)))

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
