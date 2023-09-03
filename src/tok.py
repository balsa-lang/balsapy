from enum import Enum, auto
from dataclasses import dataclass

from loc import Loc

class TK(Enum):
    """Token Kind enum"""
    pass

@dataclass
class Tok:
    """A token, with a kind, and a value"""
    kind: TK
    value: str
    loc: Loc
