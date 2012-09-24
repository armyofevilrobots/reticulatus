"""Binds gettext and contains catalogs eventually."""

import gettext
import os
gettext.bindtextdomain('reticulatus', os.path.abspath(
    os.path.join(os.path.dirname(__file__),
        'locales')))

_ = gettext.gettext

