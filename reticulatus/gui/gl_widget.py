"""Main UI stuffs"""
from PySide import QtOpenGL, QtCore, QtGui
import math
import logging
from OpenGL import GL

class GLWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        self.log=logging.getLogger(__name__)
        self.log.info("Generating glwidget")
        QtOpenGL.QGLWidget.__init__(self, parent)

        self.object = 0
        self.x_rot = 0
        self.y_rot = 0
        self.z_rot = 0

        self.last_pos = QtCore.QPoint()

        self.troll_tech_green = QtGui.QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.troll_tech_purple = QtGui.QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)

    def x_rotation(self):
        return self.x_rot

    def y_rotation(self):
        return self.y_rot

    def z_rotation(self):
        return self.z_rot

    def minimumSizeHint(self):
        return QtCore.QSize(50, 50)

    def sizeHint(self):
        return QtCore.QSize(400, 400)

    def set_x_rotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.x_rot:
            self.x_rot = angle
            self.emit(QtCore.SIGNAL("x_rotationChanged(int)"), angle)
            self.updateGL()

    def set_y_rotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.y_rot:
            self.y_rot = angle
            self.emit(QtCore.SIGNAL("y_rotationChanged(int)"), angle)
            self.updateGL()

    def set_z_rotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.z_rot:
            self.z_rot = angle
            self.emit(QtCore.SIGNAL("z_rotationChanged(int)"), angle)
            self.updateGL()

    def initializeGL(self):
        self.qglClearColor(self.troll_tech_purple.darker())
        self.object = self.makeObject()
        GL.glShadeModel(GL.GL_FLAT)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_CULL_FACE)

    def paintGL(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glLoadIdentity()
        GL.glTranslated(0.0, 0.0, -10.0)
        GL.glRotated(self.x_rot / 16.0, 1.0, 0.0, 0.0)
        GL.glRotated(self.y_rot / 16.0, 0.0, 1.0, 0.0)
        GL.glRotated(self.z_rot / 16.0, 0.0, 0.0, 1.0)
        GL.glCallList(self.object)

    def resizeGL(self, width, height):
        self.log.info("Resized to %d, %d", width, height)
        side = min(width, height)
        GL.glViewport((width - side) / 2, (height - side) / 2, side, side)

        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GL.glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0)
        GL.glMatrixMode(GL.GL_MODELVIEW)

    def mousePressEvent(self, event):
        self.last_pos = QtCore.QPoint(event.pos())

    def mouseMoveEvent(self, event):
        dx = event.x() - self.last_pos.x()
        dy = event.y() - self.last_pos.y()

        if event.buttons() & QtCore.Qt.LeftButton:
            self.set_x_rotation(self.x_rot - 8 * dy)
            self.set_y_rotation(self.y_rot + 8 * dx)
        elif event.buttons() & QtCore.Qt.RightButton:
            self.set_x_rotation(self.x_rot - 8 * dy)
            self.set_z_rotation(self.z_rot + 8 * dx)

        self.last_pos = QtCore.QPoint(event.pos())

    def makeObject(self):
        genList = GL.glGenLists(1)
        GL.glNewList(genList, GL.GL_COMPILE)

        GL.glBegin(GL.GL_QUADS)

        x1 = +0.06
        y1 = -0.14
        x2 = +0.14
        y2 = -0.06
        x3 = +0.08
        y3 = +0.00
        x4 = +0.30
        y4 = +0.22

        self.quad(x1, y1, x2, y2, y2, x2, y1, x1)
        self.quad(x3, y3, x4, y4, y4, x4, y3, x3)

        self.extrude(x1, y1, x2, y2)
        self.extrude(x2, y2, y2, x2)
        self.extrude(y2, x2, y1, x1)
        self.extrude(y1, x1, x1, y1)
        self.extrude(x3, y3, x4, y4)
        self.extrude(x4, y4, y4, x4)
        self.extrude(y4, x4, y3, x3)

        Pi = 3.14159265358979323846
        NumSectors = 200

        for i in range(NumSectors):
            angle1 = (i * 2 * Pi) / NumSectors
            x5 = 0.30 * math.sin(angle1)
            y5 = 0.30 * math.cos(angle1)
            x6 = 0.20 * math.sin(angle1)
            y6 = 0.20 * math.cos(angle1)

            angle2 = ((i + 1) * 2 * Pi) / NumSectors
            x7 = 0.20 * math.sin(angle2)
            y7 = 0.20 * math.cos(angle2)
            x8 = 0.30 * math.sin(angle2)
            y8 = 0.30 * math.cos(angle2)

            self.quad(x5, y5, x6, y6, x7, y7, x8, y8)

            self.extrude(x6, y6, x7, y7)
            self.extrude(x8, y8, x5, y5)

        GL.glEnd()
        GL.glEndList()

        return genList

    def quad(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.qglColor(self.troll_tech_green)

        GL.glVertex3d(x1, y1, -0.05)
        GL.glVertex3d(x2, y2, -0.05)
        GL.glVertex3d(x3, y3, -0.05)
        GL.glVertex3d(x4, y4, -0.05)

        GL.glVertex3d(x4, y4, +0.05)
        GL.glVertex3d(x3, y3, +0.05)
        GL.glVertex3d(x2, y2, +0.05)
        GL.glVertex3d(x1, y1, +0.05)

    def extrude(self, x1, y1, x2, y2):
        self.qglColor(self.troll_tech_green.darker(250 + int(100 * x1)))

        GL.glVertex3d(x1, y1, +0.05)
        GL.glVertex3d(x2, y2, +0.05)
        GL.glVertex3d(x2, y2, -0.05)
        GL.glVertex3d(x1, y1, -0.05)

    def normalizeAngle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle
