# din module_a importam doar ce avem nevoie (in acest caz doar variabila test)
from module_a import test
# apoi folosim direct variabila/functia importata
print(test)

# daca importam aceeasi variabila/metoda din module diferite trebuie sa folosim alias-uri diferite ca as avem access la ambele
from module_a import find_index as find_index_a
from module_b import find_index as find_index_b


my_list = [1, "txt", 19.2, "placeholder"]

print(find_index_b(my_list, "txt"))
