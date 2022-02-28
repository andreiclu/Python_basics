"""
Shiritori Game
This challenge is an English twist on the Japanese word game Shiritori. The basic premise is to follow two rules:

First character of next word must match last character of previous word.
The word must not have already been said.
Below is an example of a Shiritori game:

["word", "dowry", "yodel", "leader", "righteous", "serpent"]  #valid!

["motive", "beach"]  # invalid! - beach should start with "e"

["hive", "eh", "hive"]  # invalid! - "hive" has already been said
Write a Shiritori class that has two instance variables:

words: a list of words already said.
game_over: a boolean that is true if the game is over.
and two instance methods:

play: a method that takes in a word as an argument and checks if it is valid (the word should follow rules #1 and #2 above).

If it is valid, it adds the word to the words list, and returns the words list.
If it is invalid (either rule is broken), it returns "game over" and sets the game_over boolean to true.
restart: a method that sets the words list to an empty one [] and sets the game_over boolean to false. It should return "game restarted".

Examples
my_shiritori = Shiritori()

my_shiritori.play("apple") ➞ ["apple"]
my_shiritori.play("ear") ➞ ["apple", "ear"]
my_shiritori.play("rhino") ➞ ["apple", "ear", "rhino"]
my_shiritori.play("corn") ➞ "game over"

# Corn does not start with an "o".

my_shiritori.words ➞  ["apple", "ear", "rhino"]

# Words should be accessible.

my_shiritori.restart() ➞ "game restarted"
my_shiritori.words ➞ []

# Words list should be set back to empty.

my_shiritori.play("hostess") ➞ ["hostess"]
my_shiritori.play("stash") ➞ ["hostess", "stash"]
my_shiritori.play("hostess") ➞ "game over"

# Words cannot have already been said.
"""



class Shiritori:
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self,word):
        if not self.words:
            self.words.append(word)
            return self.words
        if word not in self.words and self.words[-1][-1] == word[0]:
            self.words.append(word)
            return self.words
        self.game_over = True
        return 'game over'

    def restart(self):
        self.words = []
        self.game_over = False
        return 'game restarted'

my_shiritori = Shiritori()
print(my_shiritori.play("apple"))
print(my_shiritori.play("ear"))
print(my_shiritori.play("rhino"))
print(my_shiritori.play("corn"))

print(my_shiritori.words)

print()# Words should be accessible.)

print(my_shiritori.restart())
print(my_shiritori.words)
print()# Words list should be set back to empty.)

print(my_shiritori.play("hostess"))
print(my_shiritori.play("stash"))
print(my_shiritori.play("hostess"))





