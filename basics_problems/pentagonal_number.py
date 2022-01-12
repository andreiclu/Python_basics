"""
Write a function that takes a positive integer num and calculates how many dots exist in a pentagonal shape around the center dot on the Nth iteration.

In the image below you can see the first iteration is only a single dot. On the second, there are 6 dots. On the third, there are 16 dots, and on the fourth there are 31 dots.
"""
def pentagonal(x):
    if x==1:
        return 1
    else:
        return x*5-5 + pentagonal(x-1)

print(pentagonal(8))