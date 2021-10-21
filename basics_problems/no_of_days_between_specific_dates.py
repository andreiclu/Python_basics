# Write a Python program to calculate number of days between two dates.

from datetime import date

fdate = date(2014,7,2)
sdate = date(2014,7,11)
output = sdate - fdate
print(output.days,"Days")

