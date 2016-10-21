import unittest

import f


def is_odd(n):
    return n % 2 == 1


class MyTests(unittest.TestCase):
    def test_is_odd(self):
        self.failUnless(is_odd(1))
        self.failIf(is_odd(2))

    def test_f_is_some_number(self):
        self.failIf(f.is_some_number("öaksdjf"))
        self.failIf(f.is_some_number("AAA"))
        self.failIf(f.is_some_number("#"))
        self.failIf(f.is_some_number(""))
        self.failIf(f.is_some_number("."))
        self.failUnless(f.is_some_number(221))
        self.failUnless(f.is_some_number(22.2))
        self.failUnless(f.is_some_number(-22.2))
        self.failUnless(f.is_some_number("225"))
        self.failUnless(f.is_some_number("22.6"))
        self.failUnless(f.is_some_number("22,6"))
        self.failUnless(f.is_some_number("-22,6"))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
