

# lucky = int(input("Let's see if the number is lucky, that means n*n = any sum of consecutive numbers: "))
#
# a = lucky ** 2
# list_ = []

# for i in range(0, a):
#
#     if i < a:
#         list_.append(i)
#         suma = suma + i
#     elif i > a:
#         i = 0 and list_.clear()
#     else:
#         print (list_)
# sum_ = 0
# while(sum_<=a):
#    if sum(range(1, int(a/2))) == a:
#        print (i for i in range(1,int(a/2)))
#    else:

#
# import pickle
# import csv
# import json
#
# def decorator(funct):
#     def bla():
#         funct()
#     return bla
#
#
# @decorator
# def pickle_():
#     with open('data.pickle', 'rb') as f:
#         data = pickle.load(f)
#     print(data)
#
# @decorator
# def csv_():
#     with open("employees.csv") as in_file:
#         reader = csv.reader(in_file)
#         for row in reader:
#             print(row)
#
# @decorator
# def json_():
#     with open("example.json") as in_file:
#         data = json.load(in_file)
#
#     print(data['dogs'])


# context manager start, stop

# def func(a, b):
# for i in range(a,b):
# def func(a,b):
#   result  = 0
#   for i in range(a,b):
#     result += i
# with your_cm(start,stop) as ycm:
# func(start,stop)
from contextlib import contextmanager


import datetime

# class Timed:
#
#     def __enter__(self):
#         self.start = datetime.datetime.now()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.stop = datetime.datetime.now()
#         print(self.stop-self.start)
#         return self.stop-self.start
#
#
#
# def func(a,b):
#     result = 0
#     for i in range(a,b):
#         result += i
#
# a=10
# b=20
# with Timed(a,b) as t:
#     print(t)

# x = [i/10 for i in range(11)]
#
# print(x)
#


# from math import sqrt
# #
# #
# def is_prime(n):
#     for i in range(2, int(sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
#

# def get_n_primes(n):
#     primes = []
#     i = 2
#     while len(primes) != n:
#         if is_prime(i):
#             primes.append(i)
#         i += 1
#     return primes

# print(get_n_primes(20))

# class PrimeIterator:
#     # Iterator that allows you to iterate over n primes
#     def __init__(self, n):
#         self.n = n
#         self.generated_numbers = 0
#         self.number = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.number += 1
#         if self.generated_numbers >= self.n:
#             raise StopIteration
#         elif is_prime(self.number):
#             self.generated_numbers += 1
#             return self.number
#         return self.__next__()
#
#
# iter = PrimeIterator(20)
# for elem in iter:
#     print(elem)

#
# def sq_numbers(n):
#     for i in range(1,n+1):
#         yield i*i
#
#
# a = sq_numbers(11)
#
# for i in a:
#     print(i)
#
#
# import re
# x = input("Insert a text:")
#
# dict = {
#     "COLEGIUL": "Co.",
#     "LICEUL": "Li.",
#     "NATIONAL": "Nat.",
#     "TEORETIC": "Tr."
# }
#
# # my_set = ('COLEGIUL', 'LICEUL', 'NATIONAL', 'TEORETIC')
#
#
# for i in x:
#     for key, value in dict.items():
#         if key == i:
#             new_str = (re.sub(key, value, new_str))
#             print(new_str)


