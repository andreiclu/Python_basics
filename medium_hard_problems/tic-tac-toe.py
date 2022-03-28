"""
Tic Tac Toe
Given a tic-tac-toe board, create a function that determines whether X won, O won, or there's a tie.

The board is represented as a 2-dimensional list. A board does not have to be completely filled. Blank squares are represented with the letter "B". For each board, X begins and O goes second.

Examples
who_won([
  ["X", "O", "B"],
  ["B", "X", "O"],
  ["B", "B", "X"]
]) ➞ "X"

who_won([
  ["X", "O", "X"],
  ["O", "X", "B"],
  ["X", "B", "O"]
]) ➞ "X"

who_won([
  ["X", "X", "O"],
  ["O", "O", "X"],
  ["X", "X", "O"]
]) ➞ "Tie"
"""


def who_won(board):
    for i in board:
        if i[0] == i[1] == i[2]:
            return i[0]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return board[0][0]
    else:
        return "Tie"


print(who_won([
  ["X", "X", "O"],
  ["O", "O", "X"],
  ["X", "X", "O"]
]))

print(who_won([
  ["X", "O", "X"],
  ["O", "X", "B"],
  ["X", "B", "O"]
]))