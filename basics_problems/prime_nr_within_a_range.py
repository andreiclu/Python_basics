# The prime numbers within a range:

first_nr = int(input("Enter the first number: "))
second_nr = int(input("Enter a second number: "))

for num in range(first_nr,second_nr+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)