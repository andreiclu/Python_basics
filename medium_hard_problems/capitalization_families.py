"""
Write a function that groups words by the number of capital letters and returns a dictionary of object entries whose keys are the number of capital letters and the values are the groups.

Examples
grouping(["HaPPy", "mOOdy", "yummy", "mayBE"]) ➞ {
  0: ["yummy"],
  2: ["mayBE", "mOOdy"],
  3: ["HaPPy"]
}

grouping(["eeny", "meeny", "miny", "moe"]) ➞ {
  0: ["eeny", "meeny", "miny", "moe"]
}

grouping(["FORe", "MoR", "bOR", "tOR", "sOr", "lor"]) ➞ {
  0: ["lor"],
  1: ["sOr"],
  2: ["MoR", "bOR", "tOR"],
  3: ["FORe"]
}
Notes
The object entries have to be sorted by the number of capital letters.
The groups will be arrays of all words sharing the same number of capital letters.
The groups have to be sorted alphabetically (ignoring case).
Words will be unique.
"""
import pprint

def grouping(w):
    dic = {}
    for word in w:
        n = 0
        for j in word:
            if j.isupper():
                n+=1
        if n in dic:
            dic[n].append(word)
        else:
            dic[n] = [word]

    return pprint.pprint(dic)
    # for x in dic:
    #     dic[x] = sorted(dic[x], key=str.lower())

grouping(["FORe", "MoR", "bOR", "tOR", "sOr", "lor"])

grouping((["eeny", "meeny", "miny", "moe"]))