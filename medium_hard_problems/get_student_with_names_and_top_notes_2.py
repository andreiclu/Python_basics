"""Create a function that takes a list of dictionaries like [{ "name": "John", "notes": [3, 5, 4]},
{ "name": "Mich", "notes": [1, 3, 5]}] and returns a list of dictionaries like [{ "name": "John", "top_note": 5 },
{"name": "Mich", "top_note": 5}].

If a student has no notes (an empty list), return top_note: 0.

Examples
get_name_and_top_note([{ "name": "John", "notes": [2, 4, 5]}, { "name": "Mich", "notes": [1, 3, 5]}])  ➞
[{ "name": "John", "top_note": 5 }, {"name": "Mich", "top_note": 5}]

get_name_and_top_note([{ "name": "Paul", "notes": []}, {"name": "Victoria", "notes": [3, 4, 2, 1]}])  ➞
[{ "name": "Paul", "top_note": 0 }, {"name": "Victoria", "top_note": 4}]
"""


def get_name_and_top_note(students):

    lst = []
    for dict_ in students:
        if len(dict_['notes']) > 0:
            lst.append({'name': dict_['name'], 'top_note': max(dict_['notes'])})
        else:
            lst.append({'name': dict_['name'], 'top_note': 0})
    return lst

print(get_name_and_top_note([{ "name": "Paul", "notes": []}, {"name": "Victoria", "notes": [3, 4, 2, 1]}]))


print(get_name_and_top_note([{ "name": "John", "notes": [2, 4, 5]}, { "name": "Mich", "notes": [1, 3, 5]}]))

