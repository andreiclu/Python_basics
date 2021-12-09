# numers = [1,2,3,4,5]
#
# new_num = numers
#
# new_num[0] = 9
#
# print(numers)
# print(id(numers))
#
# print(new_num)
# print(id(new_num))

import copy

old_list = [[1,2,3], [4,5,6], [7,8,9]]

new_list = copy.deepcopy(old_list)

new_list[0][2] = 'c'

print("old list: ", old_list)
print("new_list: ", new_list)

