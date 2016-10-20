import math
import unittest


def IsOdd(n):
    return n % 2 == 1


class IsOddTests(unittest.TestCase):
    def testOne(self):
        self.failUnless(IsOdd(1))

    def testTwo(self):
        self.failIf(IsOdd(2))


def test_2(self):
    assert (1 != 2)
    assert (1 == 1)
    assert (math.sqrt(4) == 2)
    assert isinstance("absdfk", str)
    assert isinstance(123, int)
    assert isinstance(1.2232, float)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
