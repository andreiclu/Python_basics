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

#Exercitiu 1:


