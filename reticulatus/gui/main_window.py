"""Main UI stuffs"""
from PySide.QtGui import QMainWindow, QFileDialog
import logging
import os.path

from .reticulate_main import Ui_main_window
from .gl_widget import GLWidget
from ..geo.stl import STL

#QT warnings due to pep8 != QT
# pylint: disable=C0103


class MainWindow(QMainWindow, Ui_main_window):
    """The Main window, subclassed from the gui from qt designer."""
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.log = logging.getLogger(__name__)
        self.gl_widget = None #Pylint Complaint
        self.setupUi(self)
        self.basedir = os.getcwd()

    def setupUi(self, main_window):
        super(MainWindow, self).setupUi(main_window)
        self.gl_widget = GLWidget()
        self.gl_widget.setObjectName("gl_widget")
        self.object_3d_layout.addWidget(self.gl_widget, 0, 0, 1, 1)
        self.action_quit.setStatusTip('Exit application')
        self.action_quit.triggered.connect(self.close)
        self.action_open.setStatusTip('Open new File')
        self.action_open.triggered.connect(self.load_stl_file)

    def load_stl_file(self):
        """Load the stl"""
        fname, _ = QFileDialog.getOpenFileName(
                self, 'Open file',
                self.basedir)

        stl = STL(fname)
        stl.read()
        self.log.info("Loaded %s", stl)
        self.gl_widget.set_object(stl)



