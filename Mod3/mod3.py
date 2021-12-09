# def convertor_c_f(celsius):
#     fahrenheit = celsius * 9 / 5 + 32
#     return fahrenheit
#
#
# def convertor_f_c(fahrenheit):
#     celsius = (fahrenheit - 32) * 5 / 9
#     return celsius
#
#
# if __name__ == '__main__':
#     print(convertor_c_f(float(input("introduce temp C: "))))
#     print(convertor_f_c(float(input("introduce temp F: "))))


# import unittest
#
# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)
#
#     if __name__ == '__main__':
#         unittest.main()

# def medart(a,b,c):
#     ma = a+b+c/
#     return ma
#
# print(medart(1,2,3))


def format_price(pret):
    #rounded = round(pret,2)
    pret *= 100
    pret = int(pret)
    pret /= 100
    return f'{pret:.2f} Lei'

if __name__ == '__main__':

    print(format_price(123.568981))








