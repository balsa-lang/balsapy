from enum import Enum, auto
from dataclasses import dataclass

from loc import Loc

class TK(Enum):
    """Token Kind enum"""
    IDENTIFIER = auto
    KEYWORD = auto
    OPERATOR = auto
    SYMBOL = auto
    STR = auto
    CHAR = auto
    INT = auto
    FLOAT = auto

@dataclass
class Tok:
    """A token with a kind and a value"""
    kind: TK
    value: str | int | float
    loc: Loc
