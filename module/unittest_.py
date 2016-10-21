import unittest


def is_odd(n):
    return n % 2 == 1


class MyTests(unittest.TestCase):
    def test_1(self):
        self.failUnless(is_odd(1))

    def test_2(self):
        self.failIf(is_odd(2))


def main():
    unittest.main()

if __name__ == '__main__':
    main()
