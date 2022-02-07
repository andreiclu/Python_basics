"""
You bought a few bunches of fruit over the weekend.
Create a function that splits a bunch into singular objects inside a list.

Examples
split_bunches([
  { "name": "grapes", "quantity": 2 }
]) ➞ [
  { "name": "grapes", "quantity": 1 },
  { "name": "grapes", "quantity": 1 }
]


split_bunches([
  { "name": "currants", "quantity": 1 },
  { "name": "grapes", "quantity": 2 },
  { "name": "bananas", "quantity": 2 }
]) ➞ [
  { "name": "currants", "quantity": 1},
  { "name": "grapes", "quantity": 1 },
  { "name": "grapes", "quantity": 1 },
  { "name": "bananas", "quantity": 1 },
  { "name": "bananas", "quantity": 1 }
"""


def split_bunches(bunches):
    a, b = [], []
    for i in bunches:
        a.append(i["quantity"])
        i["quantity"] = 1
    for i in range(len(bunches)):
        for j in range(a[i]):
            b.append(bunches[i])
    return b

print(split_bunches([
  { "name": "currants", "quantity": 1 },
  { "name": "grapes", "quantity": 2 },
  { "name": "bananas", "quantity": 2 }
]))