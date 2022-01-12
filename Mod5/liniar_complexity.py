from time_decorator import measure_time


@measure_time
def calc_sum(given_array):
    my_sum = 0
    for elem in given_array:
        my_sum += elem

    return my_sum


my_arr = [4, 1, 7, 9, 10, 2, 5, 6]
my_big_list = [i for i in range(1_000_000)]
my_bigger_list = [i for i in range(2_000_000)]

print(calc_sum(my_arr))
print(calc_sum(my_big_list))
print(calc_sum(my_bigger_list))