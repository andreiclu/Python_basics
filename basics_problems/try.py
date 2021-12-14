

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
#
# [x. lower() for x in ["A","B","C"]] ['a', 'b', 'c']
#
# [x. upper() for x in ["a","b","c"]] ['A', 'B', 'C']
# map(lambda x:x. lower(),["A","B","C"]) ['a', 'b', 'c']
# map(lambda x:x. upper(),["a","b","c"]) ['A', 'B', 'C']

from functools import reduce
input_map = ['ala', 'bala', 'portocala', 'ion', 'pop', 'al', 'glanestasului']
a = []
print (list(map(lambda input_map:input_map.upper(),a)))


print(list(filter(lambda x: x[0] in "aeiou", input_map)))



