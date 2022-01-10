"""
Să se scrie o funcție C++ recursivă care determină cel mai mare
divizor comun a două numere transmise ca parametri și întoarce rezultatul prin intermediul unui parametru de ieșire.
"""

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

print(gcd(102,102**2))
