"""
Create a function that takes a string as an argument and returns the Morse code equivalen
"""

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}


def encode_morse(txt):
    morse = ""
    for i in range(len(txt)):
        morse += char_to_dots[txt[i].upper()]
        if i < len(txt)-1:
            morse += " "
    return morse



print(encode_morse("This is a test code"))


def decode_morse(txt):
    rez = ''
    txt = txt.split(' ')

    for dot_bar in txt:
        if dot_bar == '':
            rez+= ' '
        for key, encoded_value in char_to_dots.items():
            if dot_bar == encoded_value:
                rez+=key
    return rez.replace("  ", ' ')


print(decode_morse("-.-. .... .- .-.. .-.. . -. --. ."))
