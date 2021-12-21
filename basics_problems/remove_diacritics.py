def remove_diacritics(string):
    diacritcs = {"ă":"a",
                 "â":"a",
                 "î":"i",
                 "ș":"s",
                 "ț":"t"
                 }
    str_as_list = list(string)
    for i in range(0, len(string)):
        char_ = string[i]
        if char_ in diacritcs:
            str_as_list[i] = diacritcs[char_]
    return "".join(str_as_list)


print(remove_diacritics("aaadsdăâîșț"))

