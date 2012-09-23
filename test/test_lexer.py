"""Test lexer"""
from reticulatus.parser import tokens
from reticulatus.parser import lexer

import unittest

GCODE = """; Comment...
N0001 G91
N0002 G02 X0 Y0.001
N0003 G01 F10 X0Y0Z-0.01
"""

class TestTokens(unittest.TestCase):
    """Test the lexer"""

    def _tok(self, src_code=GCODE):
        """Helper func."""
        lexer.input(src_code)
        _tokens = list()
        while True:
            token = lexer.token()
            if token:
                _tokens.append(token)
            else:
                break
        return _tokens


    def test_basic_lex(self):
        """Will it lex?"""
        _tokens = self._tok(GCODE)
        self.assertEquals(len(_tokens), 13)

    def test_correct_tokens(self):
        tnames = [(token.type, token.value) for token in self._tok(GCODE)]
        self.assertEquals(tnames,
                [
                    ('COMMENTSHORT', '; Comment...'),
                    ('LINENO', 'N0001'),
                    ('GCODE', 'G91'),
                    ('LINENO', 'N0002'),
                    ('GCODE', 'G02'),
                    ('VEC', 'X0'),
                    ('VEC', 'Y0.001'),
                    ('LINENO', 'N0003'),
                    ('GCODE', 'G01'),
                    ('FEED', 'F10'),
                    ('VEC', 'X0'),
                    ('VEC', 'Y0'),
                    ('VEC', 'Z-0.01')
                ])


