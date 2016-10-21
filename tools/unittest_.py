import math
import unittest

import f


class MyTests(unittest.TestCase):
    def test_check_if_odd(self):
        self.failUnless(f.check_if_odd(1))
        self.failIf(f.check_if_odd(2))

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
        assert f.is_some_number("8") == True
        assert f.is_some_number("dddasdf") == False
        assert f.is_some_number("ddd322a2s2d1f") == False
        assert f.is_some_number(math.pi)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
