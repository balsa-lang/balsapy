import contextlib
import io
import unittest

from loc import Loc
from errors import compiler_error, compiler_warning


class TestErrorMethods(unittest.TestCase):
    def test_compiler_error(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            compiler_error(Loc("file.txt", 69, 420), "big chungulus")
        self.assertEqual("error: big chungulus\n at file.txt:69:420\n", f.getvalue())

    def test_compiler_warning(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            compiler_warning(Loc("file.txt", 69, 420), "big chungulus")
        self.assertEqual("warning: big chungulus\n at file.txt:69:420\n", f.getvalue())


