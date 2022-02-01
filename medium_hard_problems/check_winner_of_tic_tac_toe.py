"""
Create a function that takes a Tic-tac-toe board and returns "X" if the X's are placed in a way that there are three X's in a row or returns "O" if there is three O's in a row.

Examples
who_won([
  ["O", "X", "O"],
  ["X", "X", "O"],
  ["O", "X", "X"]
]) ➞ "X"

who_won([
  ["O", "O", "X"],
  ["X", "O", "X"],
  ["O", "X", "O"]
]) ➞ "O"

"""














def who_won(lst):
        for line in range(3):
            # check for row win
            if lst[line][0] == lst[line][1] == lst[line][2]:
                return lst[line][0];
            # check for col win
            if lst[0][line] == lst[1][line] == lst[2][line]:
                return lst[0][line];
        # For diagonal
        if lst[0][0] == lst[1][1] == lst[2][2]:
            return lst[0][0]
        if lst[0][2] == lst[1][1] == lst[2][0]:
            return lst[2][0]

print(who_won([
  ["O", "O", "X"],
  ["X", "O", "X"],
  ["O", "X", "O"]
]))


print(who_won([
  ["O", "X", "O"],
  ["X", "X", "O"],
  ["O", "X", "X"]
]))