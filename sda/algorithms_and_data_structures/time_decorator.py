# import time
#
#
# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         end_time = time.time()
#         print(end_time - start_time)
#
#     return wrapper

import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('Measured time:', end_time - start_time)
        return result

    return wrapper