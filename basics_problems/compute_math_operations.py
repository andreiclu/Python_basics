



def compute_math_operations(a,b,c):

    if c == 1:
        result = a + b
    elif c == 2:
        result = a - b
    elif c == 3:
        result = a * b
    elif c == 4:
        result = a / b
    else:
        result = None
    return result

def read_numbers():

    a1 = int(input("Give first nr: "))
    b2 = int(input("Give  second nr:"))
    c3 = int(input("Choose your operation: 1 - Add, 2 - Subs, 3-Multi,4-Div "))
    return a1,b2,c3

a1, b2, c3 = read_numbers()
function_result = compute_math_operations(a1,b2,c3)
print('Function result: ', function_result)
