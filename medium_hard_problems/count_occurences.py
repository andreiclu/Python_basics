def count_occurences(input_str, char):

    count = 0
    for i in range (0, len(input_str)):
        if input_str[i] == char:
            count += 1

    return count

result = count_occurences("Hello, World!", "l")
print(result)