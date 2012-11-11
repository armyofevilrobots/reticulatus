"""
Nasty little icon helper.
"""

from PySide.QtGui import QIcon
import os.path

ICONROOT = os.path.join(os.path.dirname(__file__), 'icons/icons')

def by_name(name):
    """Locates and loads an icon for the user, finding by name"""
    filename = os.path.join(ICONROOT, "%s.png" % name)
    if os.path.isfile(filename):
        #pixmap = QPixmap(filename)
        #icon = QIcon(pixmap)
        icon = QIcon(filename)
        return icon

    if QIcon.hasThemeIcon(name):
        return QIcon.fromTheme(name)

    raise KeyError, "No such icon %s exists." % name




