"""
Create a function that creates a box based on dimension n.
"""

def make_box(n):
    if n == 1:
        return 1
    else:
        top = ['#' * n]
        print(f"{top}")
        i = 0
        while(n!=0):
            middle = ['#' + ' ' * (n - 2) +"#"]
            if i < n-2:
                print(middle)
            else:
                break
            i +=1
        bottom = ['#' * n]
        print(bottom)

make_box(6)

