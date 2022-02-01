# def f1():
#     return "Hello World!"
# def f2():
#     return "bye World!"
#
# class StoreManager:
#     def __init__(self, filename, extensie):
#         self.filename = filename
#         self.extensie = extensie
#         self.file = None
#
#     def __enter__(self):
#         new_file_name = self.filename + self.extensie
#         self.file = open(new_file_name, "w")
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(self.file)
#         self.file.close()
#
#
# file1 = "fisier"
# extensie = ".txt"
# file2 = "fisier2"
# extensie2= ".csv"
#
# with StoreManager(file1, extensie) as sm:
#     print(sm)
#     result = f1()
#     sm.write(result)
#
#
# with StoreManager(file2, extensie2) as sm:
#     print(sm)
#     result = f2()
#     sm.write(result)
#

# Exercitiu 1:
#
# import datetime
#
# class FileManager():
#     def __init__(self, file, start, stop):
#         self.start = start
#         self.stop = stop
#         self.file = file
#
#     def __enter__(self, start):
#         self.start = datetime.datetime.now
#         # opening and sharing of resources
#         print(self.start)
#         self.file = open(self.file, 'w')
#         return self.file
#
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         self.stop = datetime.datetime.now
#         if self.file:
#             self.file.close()
#         print(self.stop)
#
#
#
# def func(a,b):
#     result = 0
#     for i in range(a,b):
#         result += i
#
# with FileManager('notes.txt') as file:
#     rez = func(10,20)
#     file.write(rez)

# context manager care sa primeasca 2
# argumente: start si stop
# def func(a, b):
# for i in range(a,b):
# def func(a,b):
#   result  = 0
#   for i in range(a,b):
#     result += i
# ycm:
# func(start,stop)

from datetime import datetime

class ContextManager:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.intermediate = None

    def __enter__(self):
        print(f"Am inceput sa rulez la {datetime.now()}.")
        return self.start, self.stop

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Am terminat rularea la {datetime.now()}.")

def func(a, b):
    result = 0
    for i in range(a,b):
        result += i
    return result

with ContextManager(10, 15000000) as cm:
    print(func(cm[0], cm[1]))
