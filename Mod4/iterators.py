# a = [1, 2, 3, 4]
# for item in a:
#     print(item)
#
# a = "Alice has a cat"
# for item in a:
#     print(item)
#
# a = {'name': "Adam", 'surname': "Smith"}
# for item in a:
#     print(item)
#

#
# from math import sqrt
#
#
# def is_prime(n):
#     for i in range(2, int(sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
#
#
# def get_n_primes(n):
#     primes = []
#     i = 2
#     while len(primes) != n:
#         if is_prime(i):
#             primes.append(i)
#         i += 1
#     return primes
#
#
# lst = get_n_primes(100)
# for elem in lst:
#     print(elem)



class Fib:
    def __init__(self):
        self.b = 1
        self.c = 1
    def __iter__(self):
        return self

    def __next__(self):
        self.c = self.b
        self.a = self.b
        self.b = self.c + self.a
        return self.c

a = Fib()
i = iter(a)

for k in range(20):
    print(next(i), end = ' ')

# n = 0
# n1= 1
#
# for i in range(10):
#     print(n, end=" ")
#     rez = n + n1
#
#     n=n1
#     n1=rez


#
# def fibonacci(n):
#     f = [0, 1]
#
#     for i in range(2, n + 1):
#         f.append(f[i - 1] + f[i - 2])
#     return f[n]
#
# print(fibonacci(9))

