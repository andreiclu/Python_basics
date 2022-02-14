"""
The insurance guy calls. They were about to pay you all that fortune you've been anxiously waiting for, but they detected further irregularities; the list of stolen items is misformatted and appears to contain other entries that don't belong there. Find and remove them.

You receive a dict with nested dicts with strings as values.
Convert their values to number and return a dict with entries that evaluate to type int.

Examples
find_and_remove({
    "workshop": {
      "bedsheets": "2000",
      "working": "v0g89t7t",
      "pen": "370",
      "movies": "wo1a3d5d",
    },
  }), {
    "workshop": {
      "bedsheets": 2000,
      "pen": 370
      }
  }
find_and_remove({
  "bedroom": {
    "slippers": "10000",
    "piano": "5500",
    "call": "vet",
    "travel": "world",
  },
}), {
  "bedroom": {
    "slippers": 10000,
    "piano": 5500,
  },
}
"""


def find_and_remove(dct):
    for a1,b1 in dct.items():
        t_dct = {}
        for a2,b2 in b1.items():
            if b2.isdigit():
                t_dct[a2] = int(b2)
        dct[a1] = t_dct

    return dct





print(find_and_remove({
    "workshop": {
      "bedsheets": "2000",
      "working": "v0g89t7t",
      "pen": "370",
      "movies": "wo1a3d5d",
    },
  }))