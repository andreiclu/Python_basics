"""
Implement the system of displaying the number of "likes" known from Facebook.
"""
x = list(map(str,input("Insert the names of who likes the photo: ").split()))

print(type(x[0]))

def likes(x):
    number_of_names = len(x)
    if number_of_names == 0:
        output = "No likes yet."
    elif number_of_names == 1:
        output = f"{x[0]} liked your post"
    elif number_of_names == 2:
        output = f"{x[0]} and {x[1]} liked your post"
    elif number_of_names == 3:
        output = f"{x[0]}, {x[1]} and {x[2]} liked your post"
    else:
        output = f"{x[0]}, {x[1]}, {x[2]} and {len(x)-3} others people like your post"

    return output


print(likes(x))


