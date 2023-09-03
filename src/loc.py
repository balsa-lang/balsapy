from dataclasses import dataclass


@dataclass
class Loc:
    file: str
    line: int
    col: int

    def __str__(self):
        return f"{self.file}:{self.line}:{self.col}"
