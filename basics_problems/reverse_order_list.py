 # Print list in reverse order using a loop
list1 = input("Give me an list:")
#Version1
x = reversed(list1)

for i in x:
    print(i)
#Version2
# size = len(list1) - 1
#
# for i in range(size, -1,-1):
#     print(list1[i])

