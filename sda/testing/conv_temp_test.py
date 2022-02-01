import mod3

import unittest


class TestStringMethods(unittest.TestCase):

    def test_f_c(self):
        celsius_0 = mod3.convertor_f_c(32)
        assert celsius_0 == 0

    def test_c_f(self):
        fahrenheit_0 = mod3.convertor_c_f(0)
        assert fahrenheit_0 == 32


if __name__ == '__main__':
    unittest.main()












