x = int(input("Give me a nr to find other numbers with exactly 9 divizors: "))




def count_of_div(x):
    count = 0
    for i in range(1, x+1):
        if x % i == 0:
            count +=1
    return count
def check_9_fact(x):
    c = 0
    for z in range(1, x+1):
        if count_of_div(z) == 9:
            c +=1
            print(f"The number which has exactly 9 divisors are: {z}")
            print(f"Total: {c}")

check_9_fact(x)

