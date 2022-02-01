"""
Să se scrie o funcție C++ care să returneze suma cifrelor unui număr natural transmis ca parametru.
"""

def sum_of_dig(a):
    s = 0
    while(a):
        d = a%10
        a = a//10
        s = s + d
    return s

print(sum_of_dig(158))

