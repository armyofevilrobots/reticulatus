import sys
import os
import unittest
import cairo
from argparse import ArgumentParser
from configobj import ConfigObj


from reticulatus.geo.stl import STL
from reticulatus.geo.model import Model
from reticulatus.toolpath.layer import Layer
from reticulatus.i18n import _



def parse_args(argv):
    """Parse the args. WTF did you THINK it did
    (stupid pylint, pedantic whiny beaurocractic POS)."""
    parser = ArgumentParser(
            description=_("Reticulate: Turn meshes into toolpaths for FDM 3D printers."),
            )

    opts, args = parser.parse(argv)

    return opts, args


def main():
    opts, args = parse_args(sys.argv)



