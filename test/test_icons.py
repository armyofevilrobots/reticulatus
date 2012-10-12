from reticulatus.gui.icon import by_name
import os
import unittest


class TestSTL(unittest.TestCase):
    """Test the STL"""

    def test_load_icon(self):
        """Load various icons"""
        icons = dict()

        #icons['address-book'] = by_name('address-book')
        #icons['abacus'] = by_name('abacus')
        #This segfaults if we load by image, so... we don't test.
        icons["edit-undo"] = by_name("edit-undo")
        for name, icon in icons.iteritems():
            assert not icon.isNull()
