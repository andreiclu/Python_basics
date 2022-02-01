


#
# def dec_to_bin(d):
#     binary_str = ''
#     while d>0:
#         r = d % 2
#         if r == 1:
#             binary_str = '1' + binary_str
#             d = d//2
#         else:
#             binary_str = '0' + binary_str
#             d = d//2
#     return binary_str
#
#
# print(dec_to_bin(112))
#
#
#
#
#
#
#
# def GCD(a,b):
#     while a!=b:
#         if a>b:
#             a = a-b
#         else:
#             b = b-a
#     return a
#
# print(GCD(120,44))


"""
2. Set total to zero

Set grade counter to one

While grade counter is less than or equal to ten

Input the next grade
Add the grade into the total
Set the class average to the total divided by ten

Print the class average.
"""


# def cls_avg():
#     total = 0
#     counter = 1
#     while counter<=10:
#         grade = int(input("Enter grade: "))
#         total += grade
#         counter +=1
#     class_average = total/10
#     return class_average
#
# print(cls_avg())

"""
Initialize total to zero

Initialize counter to zero

Input the first grade

while the user has not as yet entered the sentinel

add this grade into the running total
add one to the grade counter
input the next grade (possibly the sentinel)
if the counter is not equal to zero

set the average to the total divided by the counter
print the average
else

print 'no grades were entered'
"""

def cls_avg_sent():
    total = 0
    counter = 0
    grade = int(input("Enter the first grade: "))
    while grade!=-1:
        total += grade
        counter += 1
        grade = int(input("Enter grade, -1 to end: "))
    if counter !=0:
        avg = float(total/counter)
        return avg
    else:
        return "No grades were entered! "

print(cls_avg_sent())
#-

"""
initialize passes to zero

initialize failures to zero

initialize student to one

while student counter is less than or equal to ten

input the next exam result
if the student passed
add one to passes
else

add one to failures
add one to student counter

print the number of passes

print the number of failures

if eight or more students passed

print "raise tuition"
"""

# def exam_rez():
#     passes = 0
#     failures = 0
#     student = 1
#     while student <=10:
#         result = int(input("Enter result/(1=passes, 2=fail): "))
#         if result ==1:
#             passes += 1
#         else:
#             failures +=1
#         student += 1
#     print(f'Passes:{passes}, Failures:{failures}')
#     if passes >= 8:
#         print("Raise tuition")
#
# (exam_rez())


