def find_digit_char_symbol(sample_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0

    for char in sample_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1
    print("Chars=", char_count, "Digit=", digit_count, "Symbol=", symbol_count)


sample_str = input("Give me a strig with everthing: ")

find_digit_char_symbol(sample_str)
