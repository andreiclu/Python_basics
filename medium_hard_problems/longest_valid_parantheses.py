"""
Longest Valid Parentheses
Given a string containing just the characters ( and ),
find the length of the longest valid (well-formed) parentheses substring.

Examples
longest_valid_parentheses("(()") ➞ 2
# Longest valid parentheses substring is "()"

longest_valid_parentheses(")()())") ➞ 4
# Longest valid parentheses substring is "()()"

longest_valid_parentheses("()))))(()())(") ➞ 6
"""

def longest_valid_parentheses(string):
    stack = []
    stack.append(-1)

    result = 0

    for i in range(len(string)):
        if string[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if stack:
                result = max(result, i-stack[-1])
            else:
                stack.append(i)
    return result

print(longest_valid_parentheses("()))))(()())("))

print(longest_valid_parentheses("()))))(()())(((()()()(((()()))(()("))