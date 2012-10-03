"""Main UI stuffs"""
from PySide.QtGui import QMainWindow, QPushButton, QApplication
from PySide import QtOpenGL, QtCore, QtGui
import math
from OpenGL import GL
import sys

from .gl_widget import GLWidget
from .main_window import MainWindow



class App(QApplication):
    """This is a subclass of the regular app, for
    adding new functionality later on."""
    pass


