# Remove a specific(3) number from a given list:

my_list = [3,2,4,7,9.1,0,5,3,4,7,1,3,1,4,3]

# for i in my_list:
#     if my_list[i] == 3:
#         my_list.remove(3)
# print(my_list)
# Error : list will be out of range because it keeps getin smaller that's
# because we remove one element

#
# while my_list.count(3)>0:
#     my_list.remove(3)
# print(my_list)

# Best one so far:
#
print('my_list', my_list)
my_set = set(my_list)
print('my_set: ', my_set)
my_new_list = list(my_set)
print('my_newlist:', my_new_list)