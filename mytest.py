import math
import unittest


class MyTests(unittest.TestCase):
    def test_one():
        print(111)

    def test_2(self):
        assert (1 != 2)
        assert (1 == 1)
        assert (math.sqrt(4) == 2)
        assert isinstance("absdfk", str)
        assert isinstance(123, int)
        assert isinstance(1.2232, float)
