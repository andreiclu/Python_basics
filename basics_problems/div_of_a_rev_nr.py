# x = input("Let's find out what are the divisors of a your reversed number: ")

def main():
    n = input("Insert a number")
    rev_n = reversed(n)
    rev_n = ''.join(rev_n)
    rev_n = int(rev_n)

    for i in range(2,int(rev_n/2) +1):
        if rev_n % i == 0:
            print(i)

if __name__ == '__main__':
    main()
    