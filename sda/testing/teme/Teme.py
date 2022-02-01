def convCtoK(celsius):
    kelvin = celsius + 273.15
    return kelvin


def convKtoC(kelvin):
    celsius = kelvin - 273.15
    return celsius


def convKtoF(kelvin):
    fahrenheit = (kelvin * 9 / 5) - 459.67
    return fahrenheit


def convFtoK(fahrenheit):
    kelvin = (fahrenheit + 459.67) * 5 / 9
    return kelvin



if __name__ == '__main__':

    print(convCtoK(float(input("Temperatura in C:"))),end="°\n")
    print(convKtoC(float(input("Temperatura in K:"))),end="°\n")
    print(convKtoF(float(input("Temperatura in K:"))),end="°\n")
    print(convFtoK(float(input("Temperatura in F:"))),end="°\n")

# class Temp:
#     def __init__(self, temp_kelvin):
#         self.temp_kelvin = temp_kelvin
#
#     def conv_to_celsius(self):
#         celsius = self.temp_kelvin - 273.15
#         return celsius
#
#     def conv_to_fahrenheit(self):
#         fahrenheit = (self.temp_kelvin * 9 / 5) - 459.67
#         return fahrenheit
#
#
# class TempCelsius:
#     def __init__(self, val):
#         self.val = val
#
#     def to_fahrenheit(self):
#         return self.to_kelvin().to_fahrenheit()
#
#     def to_kelvin(self):
#         kelvin = self.val + 273.15
#         return TempKelvin(kelvin)
#
#     def __str__(self):
#         return f"{self.val}°C"
#
#
# class TempFahrenheit:
#     def __init__(self, val):
#         self.val = val
#
#     def to_celsius(self):
#         return self.to_kelvin().to_celsius()
#
#     def to_kelvin(self):
#         kelvin = (self.val + 459.67) * 5 / 9
#         return TempKelvin(kelvin)
#
#     def __str__(self):
#         return f"{self.val}°F"
#
#
# class TempKelvin:
#     def __init__(self, val):
#         self.val = val
#
#     def to_celsius(self):
#         celsius = self.val - 273.15
#         return TempCelsius(celsius)
#
#     def to_fahrenheit(self):
#         fahrenheit = (self.val * 9 / 5) - 459.67
#         return TempFahrenheit(fahrenheit)
#
#     def __str__(self):
#         return f"{self.val}°K"
#
#
#
# def test():
#     a = 5
#     return a ** 2
#
#
# a = TempCelsius(100)
# print(a)
# print(a.to_kelvin())
# print(a.to_fahrenheit())


