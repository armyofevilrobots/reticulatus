"""
This is a parser for gcode
"""
# PLY is a bit grungy and doesn't conform to pep8, so...
# pylint: disable=C0103
from ply.lex import lex
import tokens

lexer = lex(module = tokens)



