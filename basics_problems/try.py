
#
#

# n = int(input("Give me a number to see what's n in S=1**4 + 2**4 + 3**4 + ... + n**4: "))
#
# def poli():
#     rez = (n*(n+1)*(2*n+1)*3*n**2 + 3*(n-1))/30
#     return rez
#
# print(poli())
#
#

# x = input("Let's find out what are the divisors of a your reversed number: ")
#
# w = ""
# for i in x:
#     w = i + w
# print ("The revered number is : ", w)
#
# result = []
# for i in range(1, int(w//2) + 1):
#         if int(w) % i == 0:
#             result.append(i)
# result.append(int(w))
#
# print(result)

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


# context manager care

# def func(a, b):
# for i in range(a,b):
# def func(a,b):
#   result  = 0
#   for i in range(a,b):
#     result += i
# with your_cm(start,stop) as ycm:
# func(start,stop)
from contextlib import contextmanager


# import datetime
#
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
# def func(a,b):
#     result = 0
#     for i in range(a,b):
#         result += i
#
#
# if __name__ == '__main__':
#     with Timed() as td:
#         print(func(10,20))
#



