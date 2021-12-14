# functie ne-lambda/normala
from functools import reduce
def func_add(nr1, nr2):
  return nr1+nr2

f2 = func_add
f2(2,3)

f3 = lambda nr1, nr2: nr1 + nr2
f3(5,6)



l = [(2,6), (4,2), (6,16)]

min(l)

tuplu = (1,2)
print(tuplu[1])
tuplu[0]

l2 = [1,2,3,4,5,6]
min(l2, key= lambda el: el[1])

pairs = [(1, 10), (2, 9), (3, 8)]

l2 = (1,2,3,4,5,6)
f  = lambda el : el**2

def func(el):
  return el**2


list(map(lambda el : el**2, l2))
help(map)
# list(map(func, l2))



l2 = (1,2,3,4,5,6)
list(filter(lambda x: x % 3, l2))

map(f, l2) #returnteaza lista2
filter(f, l2) # returnezza lista3
reduce(f, l2) # el

from functools import reduce
reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])

reduce(f , [1, 2, 3, 4, 5])
f(f( f(1,2) , 3), 4),5 )