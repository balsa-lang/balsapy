import unittest

from lexer import Tok, TK, lex
from loc import Loc


class TestLexer(unittest.TestCase):
    def test_even_odd(self):
        f = "../test/even_odd.bs"
        expected = [
            # Line 1
            Tok( TK.KEYWORD,    'use',   Loc(f,  1,  1) ),
            Tok( TK.IDENTIFIER, 'std',   Loc(f,  1,  5) ),
            Tok( TK.SYMBOL,     '::',    Loc(f,  1,  8) ),
            Tok( TK.IDENTIFIER, 'io',    Loc(f,  1, 10) ),
            Tok( TK.SYMBOL,     '\n',    Loc(f,  1, 12) ),
            # Line 2
            Tok( TK.SYMBOL,     '\n',    Loc(f,  2,  1) ),
            # Line 3
            Tok( TK.SYMBOL,     '\n',    Loc(f,  3,  1) ),
            # Line 4
            Tok( TK.KEYWORD,    'func',  Loc(f,  4,  1) ),
            Tok( TK.IDENTIFIER, 'main',  Loc(f,  4,  6) ),
            Tok( TK.SYMBOL,     '(',     Loc(f,  4, 10) ),
            Tok( TK.SYMBOL,     ')',     Loc(f,  4, 11) ),
            Tok( TK.SYMBOL,     '{',     Loc(f,  4, 13) ),
            Tok( TK.SYMBOL,     '\n',    Loc(f,  4, 14) ),
            # Line 5
            Tok( TK.IDENTIFIER, 'u8',    Loc(f,  5,  5) ),
            Tok( TK.IDENTIFIER, 'i',     Loc(f,  5,  8) ),
            Tok( TK.OPERATOR,   '=',     Loc(f,  5, 10) ),
            Tok( TK.INT,        1,       Loc(f,  5, 12) ),
            Tok( TK.SYMBOL,     '\n',    Loc(f,  5, 13) ),
            # Line 6
            Tok( TK.KEYWORD,    'while', Loc(f,  6,  5) ),
            Tok( TK.SYMBOL,     '(',     Loc(f,  6, 11) ),
            Tok( TK.IDENTIFIER, 'i',     Loc(f,  6, 12) ),
            Tok( TK.OPERATOR,   '<=',    Loc(f,  6, 14) ),
            Tok( TK.INT,        100,     Loc(f,  6, 17) ),
            Tok( TK.SYMBOL,     ')',     Loc(f,  6, 20) ),
            Tok( TK.SYMBOL,     '{',     Loc(f,  6, 22) ),
            Tok( TK.SYMBOL,     '\n',    Loc(f,  6, 23) ),
            # Line 7
            Tok( TK.KEYWORD,    'if',    Loc(f,  7,  9) ),
            Tok( TK.SYMBOL,     '(',     Loc(f,  7, 12) ),
            Tok( TK.IDENTIFIER, 'i',     Loc(f,  7, 13) ),
            Tok( TK.OPERATOR,   '%',     Loc(f,  7, 15) ),
            Tok( TK.INT,        2,       Loc(f,  7, 17) ),
            Tok( TK.OPERATOR,   '==',    Loc(f,  7, 19) ),
            Tok( TK.INT,        0,       Loc(f,  7, 22) ),
            Tok( TK.SYMBOL,     ')',     Loc(f,  7, 23) ),
            Tok( TK.SYMBOL,     '{',     Loc(f,  7, 25) ),
            Tok( TK.SYMBOL,     '\n',    Loc(f,  7, 26) ),
            # Line 8
            Tok( TK.IDENTIFIER, 'io',    Loc(f,  8, 13) ),
            Tok( TK.SYMBOL,     '::',    Loc(f,  8, 15) ),
            Tok( TK.IDENTIFIER, 'print', Loc(f,  8, 17) ),
            Tok( TK.SYMBOL,     '(',     Loc(f,  8, 22) ),
            Tok( TK.STRING,     'even',  Loc(f,  8, 23) ),
            Tok( TK.SYMBOL,     ')',     Loc(f,  8, 29) ),
            Tok( TK.SYMBOL,     '\n',    Loc(f,  8, 30) ),
            # Line 9
            Tok( TK.SYMBOL,     '}',     Loc(f,  9,  9) ),
            Tok( TK.KEYWORD,    'else',  Loc(f,  9, 11) ),
            Tok( TK.SYMBOL,     '{',     Loc(f,  9, 16) ),
            Tok( TK.SYMBOL,     '\n',    Loc(f,  9, 17) ),
            # Line 10
            Tok( TK.IDENTIFIER, 'io',    Loc(f, 10, 13) ),
            Tok( TK.SYMBOL,     '::',    Loc(f, 10, 15) ),
            Tok( TK.IDENTIFIER, 'print', Loc(f, 10, 17) ),
            Tok( TK.SYMBOL,     '(',     Loc(f, 10, 22) ),
            Tok( TK.STRING,     'odd',   Loc(f, 10, 23) ),
            Tok( TK.SYMBOL,     ')',     Loc(f, 10, 28) ),
            Tok( TK.SYMBOL,     '\n',    Loc(f, 10, 29) ),
            # Line 11
            Tok( TK.SYMBOL,     '}',     Loc(f, 11,  9) ),
            Tok( TK.SYMBOL,     '\n',    Loc(f, 11, 10) ),
            # Line 12
            Tok( TK.IDENTIFIER, 'i',     Loc(f, 12,  9) ),
            Tok( TK.OPERATOR,   '=',     Loc(f, 12, 11) ),
            Tok( TK.IDENTIFIER, 'i',     Loc(f, 12, 13) ),
            Tok( TK.OPERATOR,   '+',     Loc(f, 12, 15) ),
            Tok( TK.INT,        1,       Loc(f, 12, 17) ),
            Tok( TK.SYMBOL,     '\n',    Loc(f, 12, 18) ),
            # Line 13
            Tok( TK.SYMBOL,     '}',     Loc(f, 13,  5) ),
            Tok( TK.SYMBOL,     '\n',    Loc(f, 13,  6) ),
            # Line 14
            Tok( TK.SYMBOL,     '}',     Loc(f, 14,  1) ),
            Tok( TK.SYMBOL,     '\n',    Loc(f, 14,  2) ),
        ]

        self.assertEqual(lex(f), expected)
