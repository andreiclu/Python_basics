import unittest
import mod3


class FormatUtilsTests(unittest.TestCase):
    def test_price_formats(self):
        first = mod3.format_price(96.36514)
        first_expected = '96.36 Lei'
        print(first)
        print(first_expected)

        assert first == first_expected

        assert mod3.format_price(985.857646) == '985.85 Lei'
        assert mod3.format_price(17.5) == '17.50 Lei'
        assert mod3.format_price(123.569874) == '123.56 Lei'


if __name__ == '__main__':
    unittest.main()


    