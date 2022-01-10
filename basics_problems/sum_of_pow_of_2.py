def sumpow(x):
    power = []
    list_of_num = []
    while(x>0):
        power.append(x%2)
        x = x//2

    for i in range (len(power)):
        if (power[i] ==1):
            list_of_num.append(i)
    print(list_of_num)
def main():
    number = 23342
    print(f"Pow of 2 that sum up to{number} are: ")
    sumpow(number)

if __name__ == '__main__':
    main()

