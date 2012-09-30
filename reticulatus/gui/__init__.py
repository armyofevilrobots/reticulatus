"""Main UI stuffs"""
from PySide.QtGui import QMainWindow, QPushButton, QApplication
from PySide import QtOpenGL, QtCore, QtGui
import math
from OpenGL import GL
import sys

from .reticulate_main import Ui_MainWindow
from .gl_widget import GLWidget



class App(QApplication):
    """This is a subclass of the regular app, for
    adding new functionality later on."""
    pass


class MainWindow(QMainWindow, Ui_MainWindow):
    """The Main window, subclassed from the gui from qt designer."""
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

    def setupUi(self, main_window):
        super(MainWindow, self).setupUi(main_window)
        print self.object_3d.parentWidget().parentWidget()
        #self.object_3d_layout.removeWidget(self.object_3d)
        #del self.object_3d
        #self.object_3d = GLWidget()
        #self.object_3d.setObjectName("object_3d")
        #self.object_3d_layout = QtGui.QGridLayout(self.object_3d)
        #self.object_3d_layout.addWidget(self.object_3d)
        self.object_3d_layout.removeWidget(self.gl_widget)
        del self.gl_widget
        self.gl_widget = GLWidget()
        self.gl_widget.setObjectName("gl_widget")
        self.object_3d_layout.addWidget(self.gl_widget, 0, 0, 1, 1)


