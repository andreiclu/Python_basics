
x = int(input("Give me a nr: "))
y = int(input("Give me a second nr: "))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


print ("Your GCD is:", gcd(x,y))
