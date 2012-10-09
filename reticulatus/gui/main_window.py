"""Main UI stuffs"""
from PySide.QtGui import QMainWindow, QFileDialog
import logging
import os.path
import time

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
        """Set's up the UI, connects actions."""
        super(MainWindow, self).setupUi(main_window)
        self.gl_widget = GLWidget()
        self.gl_widget.setObjectName("gl_widget")
        self.object_3d_layout.addWidget(self.gl_widget, 0, 0, 1, 1)
        self.action_quit.setStatusTip('Exit application')
        self.action_quit.triggered.connect(self.close)
        self.action_open.setStatusTip('Open new File')
        self.action_open.triggered.connect(self.load_stl_file)

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


    def load_stl_file(self):
        """Load the stl"""
        now = time.time()
        fname, _ = QFileDialog.getOpenFileName(
                self, 'Open file',
                self.basedir,
                "STL Files (*.stl);;All Files (*)")

        if not fname:
            self.statusBar().showMessage("No file selected.")
            return
        stl = STL(fname)
        #stl.debug=True
        stl.read(self._loader_cb)
        self.log.info("Loaded %s", stl)
        self.statusBar().showMessage("Processing...")
        if fname:
            self.gl_widget.set_object(stl)
            self.basedir = os.path.dirname(fname)
        self.statusBar().showMessage(
                "Loaded model %s with %d polygons in %0.1f seconds" %
                (
                    os.path.basename(fname),
                    len(stl.facets),
                    time.time()-now
                    )
                )



