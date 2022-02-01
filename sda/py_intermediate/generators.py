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
# def prime_generator(n):
#     # Generator to iterate over n prime numbers
#     number = 2
#     generated_numbers = 0
#     while generated_numbers != n:
#         if is_prime(number):
#             yield number
#             generated_numbers += 1
#         number += 1
#
#
# gen = prime_generator(100)
# for elem in gen:
#     print(elem)
#
#
#
