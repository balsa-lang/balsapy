import unittest

from loc import Loc


class TestLoc(unittest.TestCase):
    def test_str(self):
        l = Loc("test.extension", 45, 37)
        self.assertEqual(str(l), "test.extension:45:37")

