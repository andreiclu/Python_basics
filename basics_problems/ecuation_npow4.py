
# n = int(input("Give me a number to see what's n in S=1**4 + 2**4 + 3**4 + ... + n**4: "))



def main():
    s = 0
    nr = int(input())
    for i in range(1,nr+1):
        s = s + i**4
    print(s)

if __name__ == '__main__':
    main()



