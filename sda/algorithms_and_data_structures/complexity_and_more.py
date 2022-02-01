# import time
#
#
# def do_nothing(my_list):
#     # print(my_list)
#     a=3
#     return a
#
# def get_first_elem(my_list):
#     return my_list[0]
#
# my_arr = [4, 1, 7, 9, 10, 2, 5, 6]
#
# # my_big_list = []
# # for i in range(1_000_000):
# #     my_big_list.append(i)
# # sau
# my_big_list = [i for i in range(1_000_000)]
#
# start_time = time.time()
# do_nothing(my_arr)
# end_time = time.time()
# print(end_time-start_time)
#
# start_time = time.time()
# do_nothing(my_big_list)
# end_time = time.time()
# print(end_time-start_time)
#
# start_time = time.time()
# get_first_elem(my_arr)
# end_time = time.time()
# print(end_time-start_time)
#
# start_time = time.time()
# get_first_elem(my_big_list)
# end_time = time.time()
# print(end_time-start_time)

import time_decorator


@time_decorator.measure_time
def do_nothing(my_list):
    # print(my_list)
    a = 3
    return a


@time_decorator.measure_time
def get_first_elem(my_list):
    return my_list[0]


my_arr = [4, 1, 7, 9, 10, 2, 5, 6]

# my_big_list = []
# for i in range(1_000_000):
#     my_big_list.append(i)
# sau
my_big_list = [i for i in range(1_000_000)]


do_nothing(my_arr)



do_nothing(my_big_list)



get_first_elem(my_arr)



get_first_elem(my_big_list)

