"""Basic parser setup for gcode input"""
import ply.lex as lex
# PLY is a bit grungy and doesn't conform to pep8, so...
# pylint: disable=C0103
tokens = ("GCODE", "LINENO", "COMMENTSHORT", "VEC", "FEED")

t_GCODE = r'[GM]\d+(\.\d)?' #G21 M103 G102.3
t_LINENO = r'N\d+' #N102 N0001
t_COMMENTSHORT = r';.*'
t_VEC = r'[XYZE][-+]?\d+(\.\d+)?' #X102 Y32.2 E104.51231
t_FEED = r'F\d+(\.\d+)?' #F103 special case so we see a different token.


# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    '''Handle errors.'''
    t.lexer.skip(1)
