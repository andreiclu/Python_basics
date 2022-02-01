x = input("Let's check if your text is palindrome or not: ")

w = ""
for i in x:
    w = i + w
"""In w incepem sa stocam primul element din textul dat, iar cu fiecare 
 intrare in for se va stoca urmatorul, astfel se va obtine textul oferit invers"""

if (x == w): # verificam daca textul initial este egal cu cel citit invers
    print("Yes, that's a palindrome") # daca da este palindrom
else:
    print("No, bad luck")

