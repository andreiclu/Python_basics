"""
Write the function WeIrD CaSe, which accepts a string and returns it with all even numbers as characters, all uppercase, and odd letters lowercase. Use indexing from zero.
"""

def weird_str(string: str):
    i = 0
    new_str = ''

    for char in string:
        if char != ' ':
            if i % 2 == 0:
                new_str += str.upper(char)
            else:
                new_str += char
            i +=1
        else:
            i = 0
            new_str += char
    return new_str

print(weird_str("ana are mere si pere "))


