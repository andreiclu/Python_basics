"""
Folosind operatorul conditional,
determinati daca 3 numere reale a,b,c pot fi lungimile laturilor unui triunghi.
"""

def triunghi(a,b,c):
    if (a+b)>c and (a+c)>b and (b+c)>a:
        return True
    else:
        return False

print(triunghi(10,20,30))

# a = int(input("Insert a numbber: "))
# b = int(input("Insert a number: "))
# c = int(input("Insert a number: "))
# if (a + b) > c and (a + c) > b and (b + c) > a:
#     print("True")
# else:
#     print("False")
#
#
