"""
Create a function that converts color in RGB format to Hex format.

Examples
rgb_to_hex(0, 128, 192) ➞ "#0080c0"

rgb_to_hex(45, 255, 192) ➞ "#2dffc0"

rgb_to_hex(0, 0, 0) ➞ "#000000"
"""






def rgb_to_hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

print(rgb_to_hex(0, 128, 192))

print(rgb_to_hex(45, 255, 192))


