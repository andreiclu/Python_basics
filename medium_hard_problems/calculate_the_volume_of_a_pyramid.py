"""
Calculate the Volume of a Pyramid
Create a function that takes the length, width, height (in meters) and output unit and returns the volume of a pyramid to three decimal places in the correct unit.

Examples
pyramid_volume(4, 6, 20, "centimeters") ➞ "160000000.000 cubic centimeters"

pyramid_volume(1843, 1823, 923, "kilometers") ➞ "1.034 cubic kilometers"

pyramid_volume(18, 412, 93, "millimeters") ➞ "229896000000000.000 cubic millimeters"
Notes
The units used are limited to: millimeters, centimeters, meters and kilometers.
Ensure you return the answer and add the correct unit in the format cubic <unit>.
"""


def pyramid_volume(length,width,height,unit):

    formula = (length*width*height)/3

    if unit == 'millimeters':
        return f'{formula*10000000:.3f} cubic milimeters'
    if unit == 'centimeters':
        return f'{formula*1000000:.3f} cubic centimeters'
    if unit == 'kilometers':
        return f'{formula*0.000000001:.3f} cubic kilometers'


print(pyramid_volume(18, 412, 93, "millimeters"))

print(pyramid_volume(1843, 1823, 923, "kilometers"))

print(pyramid_volume(4, 6, 20, "centimeters"))