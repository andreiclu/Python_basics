
#Write a Python program to print the calendar of a given month and year.
import calendar
x = int(input("Input a year: "))
y = int(input("Input a month: "))

print(calendar.month(x,y))