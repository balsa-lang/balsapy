from tok import TK


def lex(lines: list[str]):
    """Given a `str`, return its tokens"""
    kind: TK = None
    substr: str = None
