import Teme
import unittest

class VerifConvertor(unittest.TestCase):
    def c_to_k_test(self):
        celsius_0 = Teme.convCtoK(273.15)
        assert celsius_0 == 0

    def k_to_c_test(self):
        kelvin_0 = Teme.convKtoC(0)
        assert kelvin_0 == 273.15

    def k_to_f_test(self):
        kelvin_0 = Teme.convKtoF(0)
        assert kelvin_0 == -459.67

    def f_to_k_test(self):
        fahrenheit = Teme.convFtoK(3.2)
        assert fahrenheit == 257.15

if __name__ == '__main__':
    unittest.main()

