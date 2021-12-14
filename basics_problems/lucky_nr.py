# lucky = int(input("Let's see if the number is lucky, that means n*n = any sum of consecutive numbers: "))


#
def main():
    n = int(input("Insert a nr:"))
    n *= n
    i = 2
    a = 1
    while a > 0:
        x = (n + i - 1) / i
        a = x - i + 1
        if x == int(x) and a > 0:
            print(f"Lucky, {a},{x}")
            return
        i += 1
    print("Unlucky")


if __name__ == "__main__":
    main()
