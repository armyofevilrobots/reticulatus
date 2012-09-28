"""
The reticulate cmd
"""

import sys
from argparse import ArgumentParser


#from reticulatus.geo.model import Model
#from reticulatus.toolpath.layer import Layer
from reticulatus.i18n import _



def parse_args(argv):
    """Parse the args. WTF did you THINK it did
    (stupid pylint, pedantic whiny beaurocractic POS)."""
    parser = ArgumentParser(
            description=_(
                "Reticulate: 3d Printing Ginsu Fast Slicer/Filler"),
            )
    opts, args = parser.parse_args(argv)
    return opts, args


def main():
    """I probably should use argparser at some point...
    but this is convenient"""
    if "--gui" in sys.argv:
        from reticulatus.gui import MainWindow, App
        #from pyside import QtGui
        app = App(sys.argv)
        wid = MainWindow()
        wid.resize(250, 150)
        wid.setWindowTitle('Simple')
        wid.show()
        sys.exit(app.exec_())
    opts, args = parse_args(sys.argv)
    print opts, args



