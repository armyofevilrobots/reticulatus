"""
The reticulate cmd
"""

import sys
import logging
from argparse import ArgumentParser


#from reticulatus.geo.model import Model
#from reticulatus.toolpath.layer import Layer
from reticulatus.i18n import _



def parse_args():
    """Parse the args. WTF did you THINK it did
    (stupid pylint, pedantic whiny beaurocractic POS)."""
    parser = ArgumentParser(
            description=_(
                "Reticulate: 3d Printing Ginsu Fast Slicer/Filler"),
            )
    parser.add_argument('--gui',
            action='store_true',
            help='Run a GUI interface instead of slicing')
    parser.add_argument('-l', '--loglevel', dest='loglevel', action='store',
            default='warn',
            help='Loglevel: error, warn, info, debug [warn]')
    opts= parser.parse_args()
    return opts


def main():
    """I probably should use argparser at some point...
    but this is convenient"""
    opts = parse_args()
    logging.basicConfig(level=(
        {
        'error':logging.ERROR, 'warn':logging.WARN,
        'info':logging.INFO, 'debug':logging.DEBUG
        }.get(opts.loglevel, logging.WARN))
        )

    if opts.gui:
        from reticulatus.gui import MainWindow, App
        #from pyside import QtGui
        app = App(sys.argv)
        wid = MainWindow()
        wid.resize(250, 150)
        wid.show()
        sys.exit(app.exec_())



