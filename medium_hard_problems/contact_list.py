"""
Write a sorting function that takes in a list of names and sorts them by last name either alphabetically (ASC) or reverse-alphabetically (DESC).

Examples
sort_contacts([
  "John Locke",
  "Thomas Aquinas",
  "David Hume",
  "Rene Descartes"
], "ASC") ➞ [
  "Thomas Aquinas",
  "Rene Descartes",
  "David Hume",
  "John Locke"
]

# Aquinas (A) < Descartes (D) < Hume (H) < Locke (L)

sort_contacts([
  "Paul Erdos",
  "Leonhard Euler",
  "Carl Gauss"
], "DESC") ➞ [
  "Carl Gauss",
  "Leonhard Euler",
  "Paul Erdos"
]

# Gauss (G) > Erdos (ER) > Euler (EU)
"""

def sort_contacts(lst, order):
    if not lst:
        return []
    m = []
    for i in lst:
        i = i.split()
        m.append(i)

    if order == "DESC":
        return sorted(m, key= lambda x: x[1], reverse= True)
    elif order == "ASC":
        return sorted(m, key= lambda x: x[1])

print(sort_contacts([
  "John Locke",
  "Thomas Aquinas",
  "David Hume",
  "Rene Descartes"
], "ASC"))



