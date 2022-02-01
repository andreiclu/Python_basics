from time_decorator import measure_time

# big O notation
# O(1) < O(log(n)) < O(n) < O(n*log(n)) < O(n^2) < O(2^n) < O(n!)


# complexitate polinomiala: puterea 2, 3, 4
# ce am folosit aici, puterea 2 (complexitate patratica)

my_2d_array_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n_1 = 100
my_big_2d_array_1 = [[i for i in range(n_1)] for j in range(n_1)]
my_bigger_2d_array_1 = [[i for i in range(n_1*n_1)] for j in range(n_1*n_1)]

# print(my_2d_array_1[2][2])
# print(my_2d_array_1[0][:2])
# print(my_2d_array_1[:2])
# print(my_2d_array_1[:2][:2])


# def pretty_print_2d_list(my_2d_list):
#     for elem in my_2d_list:
#         print(elem)

@measure_time
def calc_sum(my_array):
    my_sum = 0
    for elem in my_array:
        for sub_elem in elem:
            my_sum += sub_elem
    return my_sum


print(calc_sum(my_2d_array_1))
print(calc_sum(my_big_2d_array_1))
print(calc_sum(my_bigger_2d_array_1))
# pretty_print_2d_list(my_big_list)