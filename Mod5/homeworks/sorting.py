"""
15.	Write the elements of a list to a file in the following way: each row will contain one number from the list. Do this thing both in an iterative and recursive way.
Method calls :
   write_elem_using_recursion(filename, [1, 2, 5, 6, 8,])
   write_elem_iterative(filename, [1, 2, 5, 6, 8,])
"""



def write_elem_iterative(filename, list_a):
    f = open(filename + ".txt", 'w')

    for elem in list_a:
        f.write(str(elem) + "\n")
    f.close()


def write_elem_recursive(filename, list_a):

    def write_recursive(fp, list_b):
        if not list_b:
            return
        n = list_b.pop()
        write_recursive(fp, list_b)
        fp.write(str(n) + "\n")
    f = open(filename + ".txt", 'w')
    write_recursive(f, list(list_a))
    f.close()




new_list = [1, 454, 3, 2, 3, 4, 5, 6, 77, 5, 3, 22]

write_elem_iterative("iterative", new_list)
write_elem_recursive("recursive", new_list)