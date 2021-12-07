x = input("Give me a number to see how many times will 2 or 3 appear:")

def count_of_2_or_3():
    count_2 = 0
    count_3 = 0
    for i in x:
        if i == '2':
            count_2 +=1
        if i == '3':
            count_3 +=1
    return count_2, count_3

print(count_of_2_or_3())