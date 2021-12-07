# add any number of ingredients


def add_ingredients(*args, **kwargs):
    result = 0
    for arg in args:
        result += arg
    for key in kwargs:
        print(key)
        result += kwargs[key]
    return result

# print(add_ingredients(1,2,3, eggs= 3, smap =5, cheese=2, lettuce=6))