import unittest

from lexer import *
from loc import Loc

class TestLexer(unittest.TestCase):
    def test_fizzbuzz(self):
        f = 'fizzbuzz.bs'
        expected = [
            # Line 1
            Tok( TK.KEYWORD,    'use',   Loc(f, 1, 1)  ),
            Tok( TK.IDENTIFIER, 'std',   Loc(f, 1, 5)  ),
            Tok( TK.SYMBOL,     '::',    Loc(f, 1, 8)  ),
            Tok( TK.IDENTIFIER, 'io',    Loc(f, 1, 10) ),
            Tok( TK.SYMBOL,     '\n',    Loc(f, 1, 12) ),
            # Line 2
            Tok( TK.KEYWORD,    'use',   Loc(f, 2, 1)  ),
            Tok( TK.IDENTIFIER, 'std',   Loc(f, 2, 5)  ),
            Tok( TK.SYMBOL,     '::',    Loc(f, 2, 8)  ),
            Tok( TK.IDENTIFIER, 'str',   Loc(f, 2, 10) ),
            Tok( TK.SYMBOL,     '\n',    Loc(f, 2, 13) ),
            # Line 3
            Tok( TK.SYMBOL,     '\n',    Loc(f, 3, 1)  ),
            # Line 4
            Tok( TK.SYMBOL,     '\n',    Loc(f, 4, 1)  ),
            # Line 5
            Tok( TK.KEYWORD,    'func',  Loc(f, 5, 1)  ),
            Tok( TK.IDENTIFIER, 'main',  Loc(f, 5, 6)  ),
            Tok( TK.SYMBOL,     '(',     Loc(f, 5, 10) ),
            Tok( TK.SYMBOL,     ')',     Loc(f, 5, 11) ),
            Tok( TK.SYMBOL,     '{',     Loc(f, 5, 13) ),
            Tok( TK.SYMBOL,     '\n',    Loc(f, 5, 14) ),
            # Line 6
            Tok( TK.IDENTIFIER, 'u8',    Loc(f, 6, 5)  ),
            Tok( TK.IDENTIFIER, 'i',     Loc(f, 6, 8)  ),
            Tok( TK.OPERATOR,   '=',     Loc(f, 6, 10) ),
            Tok( TK.INT,        '0',     Loc(f, 6, 12) ), # Wrong
            Tok( TK.SYMBOL,     '\n',    Loc(f, 6, 13) ),
            # Line 7
            Tok( TK.KEYWORD,    'while', Loc(f, 7, 5)  ),
            Tok( TK.SYMBOL,     '(',     Loc(f, 7, 11) ),
            Tok( TK.IDENTIFIER, 'i',     Loc(f, 7, 12) ),
            Tok( TK.OPERATOR,   '<',     Loc(f, 7, 14) ),
            Tok( TK.INT,        '100',   Loc(f, 7, 16) ), # Wrong
            Tok( TK.SYMBOL,     ')',     Loc(f, 7, 19) ),
            Tok( TK.SYMBOL,     '{',     Loc(f, 7, 21) ),
            Tok( TK.SYMBOL,     '\n',    Loc(f, 7, 22) ),
            # Line 8
            # Line 9
            # Line 10
        ]

        self.assertEqual(lex(f), expected)
