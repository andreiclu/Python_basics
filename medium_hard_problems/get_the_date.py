"""
Get the Date
Write a function that, given a date (in the format MM/DD/YYYY), returns the day of the week as a string. Each day name must be one of the following strings: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", or "Saturday".

To illustrate, the day of the week for "12/07/2016" is "Wednesday".

Examples
get_day("12/07/2016") ➞ "Wednesday"

get_day("09/04/2016") ➞ "Sunday"

get_day("12/08/2011") ➞ "Thursday"
Notes
This challenge assumes the week starts on Sunday.
"""

#The strftime() method returns a
# string representing date and time using date, time or datetime object.
#%A	Full weekday name.
from datetime import *
def get_day(d):
    m,d,y = map(int,d.split('/'))
    return date(y,m,d).strftime('%A')


print(get_day("12/08/2011"))