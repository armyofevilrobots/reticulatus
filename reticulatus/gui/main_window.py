"""Main UI stuffs"""
from PySide.QtGui import QMainWindow, QFileDialog, QErrorMessage
from PySide.QtCore import SIGNAL
import logging
import os.path
import time

from .reticulate_main import Ui_main_window
from .gl_widget import GLWidget
import icon
from ..geo.stl import STL
from ..project import Project

#QT warnings due to pep8 != QT
# pylint: disable=C0103


class MainWindow(QMainWindow, Ui_main_window):
    """The Main window, subclassed from the gui from qt designer."""
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.log = logging.getLogger(__name__)
        self.gl_widget = None #Pylint Complaint
        self.setupUi(self)
        self.setWindowTitle('Reticulatus')
        self.setWindowIcon(icon.by_name('spectacle-3d'))
        self.project = None
        self.err_dialog = None
        self.basedir = os.getcwd()


    def setupUi(self, main_window):
        """Set's up the UI, connects actions."""
        super(MainWindow, self).setupUi(main_window)
        self.gl_widget = GLWidget(self)
        self.gl_widget.setObjectName("gl_widget")
        self.object_3d_layout.addWidget(self.gl_widget)#, 0, 0, 1, 1)
        self.gl_widget.set_slice_slider(self.layer_slider)
        self.action_quit.setStatusTip('Exit application')
        self.action_quit.triggered.connect(self.close)
        self.action_open.setStatusTip('Open new File')
        self.action_open.triggered.connect(self.load_stl_file)
        self.action_new.triggered.connect(self.reset_model)
        self.action_slice.triggered.connect(self.slice_project)
        self.action_slice.setStatusTip("Slice the current project")
        self.connect(self.layer_list_widget,
                SIGNAL("itemChanged(QListWidgetItem *)"),
                    self.gl_widget.sync_layer)
        self.layer_slider.valueChanged.connect(self.layer_lcd.display)
        self.err_dialog = QErrorMessage(self)

    def _loader_cb(self, total, loaded):
        """Show us the progress of the file loading."""
        if total is not None:
            assert total >= loaded
            self.log.debug("total, loaded %s %s", total, loaded)
            self.log.debug("total, loaded %s %s", type(total), type(loaded))
            self.statusBar().showMessage(
                    "Loaded: %02.1f%%" % ((100.0*loaded)/total))
        else:
            self.statusBar().showMessage("Loaded polys: %8d" % loaded)

    def slice_project(self):
        """Do the slicer."""
        #self.log.info("Slicing %s", self.project)
        if self.project is None:
            self.log.warn("Tried to slice non-existent project.")
            self.err_dialog.showMessage("Failed to slice non-existent project.")
            self.statusBar().showMessage("Cannot slice a non-existent project.")
        else:
            now = time.time()
            statusbar = self.statusBar()
            #statusbar.showMessage("Slicing...")
            #TODO: Get height/start/thickness/etc from the config eh?
            self.project.slice(0.3, 0.2, 0.5,
                    callback = lambda x: statusbar.showMessage(x)
                    )
            statusbar.showMessage("Sliced %d layers in %02.1f seconds." %
                    (len(self.project.layers), time.time()-now))
            self.layer_slider.setMaximum(len(self.project.layers))


    def _load_stl_file(self, fname):
        """Actually load it."""
        stl = STL(fname)
        stl.read(self._loader_cb)
        self.log.info("Loaded %s", stl)
        self.statusBar().showMessage("Processing...")
        self.project = Project.from_stl(stl)
        self.gl_widget.set_project(self.project)
        assert self.gl_widget.project == self.project
        self.basedir = os.path.dirname(fname)
        return stl

    def load_stl_file(self):
        """Load the stl"""
        fname, _ = QFileDialog.getOpenFileName(
                self, 'Open file',
                self.basedir,
                "STL Files (*.stl);;All Files (*)")

        if not fname:
            self.statusBar().showMessage("No file selected.")
            return
        now = time.time()
        stl = self._load_stl_file(fname)
        self.statusBar().showMessage(
                "Loaded model %s with %d polygons in %0.1f seconds" %
                (
                    os.path.basename(fname),
                    len(stl.facets),
                    time.time()-now
                    )
                )

    def reset_model(self):
        """Basically just clear everything."""
        self.gl_widget.reset_model()



