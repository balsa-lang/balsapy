from enum import Enum, auto
from dataclasses import dataclass

from loc import Loc


OPERATORS = [
    '+', '-', '*', '/', '%',          # Arithmetic
    '==', '!=', '>', '>=', '<', '<=', # Comparison
    '!', '&&', '||', '^^',            # Logical
    '~', '&', '|', '^',               # Bitwise
    '=',                              # Assignment
]

SYMBOLS = [
    '\n',
    '::', ',',
    '(', ')',
    '{', '}',
    '[', ']',
]

KEYWORDS = [
    'use',
    'func',
    'while',
    'if',
    'else',
]

IGNORE = [
    ' ',
]


class TK(Enum):
    """Token type enum"""
    IDENTIFIER = auto()
    KEYWORD    = auto() # During lexing, a subset of IDENTIFIER
    SYMBOL     = auto()
    OPERATOR   = auto() # During lexing, a subset of SYMBOL
    STRING     = auto()
    CHAR       = auto()
    INT        = auto()
    FLOAT      = auto() # During lexing, a subset of INT


@dataclass
class Tok:
    """A token with a kind and a value"""
    kind: TK
    value: str | int | float
    loc: Loc


def lex(file: str):
    """Given a filename, return its tokens"""
    kind = None
    tok_str: str = ""
    line = 1
    col = 1
    with open(file) as f:
        input: str = f.read()

    # Step through input
    toks: list[Tok] = []
    for i, char in enumerate(input):
        # Check whether current token has ended
        tok_ended: bool = True
        match kind:
            case None:
                tok_ended = False
            case TK.IDENTIFIER:
                tok_ended = not char.isalnum()
            case TK.SYMBOL:
                new_str = tok_str + char
                tok_ended = new_str not in SYMBOLS and new_str not in OPERATORS
            case TK.STRING:
                tok_ended = len(tok_str) > 1 and input[i - 1] == '"'
            case TK.CHAR:
                tok_ended = len(tok_str) > 1 and char[i - 1] == "'"
            case TK.INT:
                tok_ended = not (char.isnumeric() or char == '.')

        # If current token has ended, add it to the list and start a new one
        if tok_ended:
            # Specify token kind if neccessary
            if kind == TK.IDENTIFIER and tok_str in KEYWORDS:
                kind = TK.KEYWORD
            elif kind == TK.SYMBOL and tok_str in OPERATORS:
                kind = TK.OPERATOR
            elif kind == TK.INT and not tok_str.isnumeric():
                kind = TK.FLOAT

            toks.append(Tok(kind, tok_str, Loc(file, line, col)))

            # Update location
            col += len(tok_str)
            if tok_str == '\n':
                col = 1
                line += 1

            # Reset token data
            kind = None
            tok_str = ''

        # If the character is meaninful, find out what it means
        if char not in IGNORE:
            tok_str += char
            if kind == None:
                # Infer token kind using its first character
                if char.isalpha():
                    kind = TK.IDENTIFIER
                elif char == '"':
                    kind = TK.STRING
                elif char == "'":
                    kind = TK.CHAR
                elif char.isnumeric():
                    kind = TK.INT
                else:
                    kind = TK.SYMBOL
        # If the character isn't meaningful, just update location
        else:
            col += 1

    return toks
