list = [1,2,3,4,5]
print (len(list))

list.append(2)
print (list)

print (list.count(2))

list.extend([6,7,8])
print(list)

print(list.index(7))

list.insert(0,10)
print(list)

print(list[-1])

last_elem = list.pop()
print(last_elem)
print(list)

x = list.remove(4)
print(list)

list.reverse()
print(list)

list.sort()
print(list)

list.clear()
print(list)