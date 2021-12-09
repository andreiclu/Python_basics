# importam module_a cu totul
import module_a

# apoi ne putem folosi de variabile/functii din acel modul
print(module_a.test)

my_list = [1, "txt", 19.2, "placeholder"]

print(module_a.find_index(my_list, "txt1"))

def find_index(collection, element):
    for index, value in enumerate(collection):
        if value == element:
            return index
    return -1

