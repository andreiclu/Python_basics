"""
Se citesc doua numere naturale n si k.
Afisat numerele naturale din intervalul [1,n] care au cel putin k divizori.
Exemplu: n=10, k=4 se vor afisa numerele 6 8 10
"""

n = int(input("Insert a number for the end of interval: "))
k = int(input("Insert the number of minimum divisors: "))


def count_of_div(x):
    count = 0
    for i in range(1,x+1):
        if x%i==0:
            count +=1
    return count

def numb_of_k_div(n):
    lst_of_k_div = []
    count = 0
    for i in range(1,n+1):
        if count_of_div(i) >= k:
            count +=1
            lst_of_k_div.append(i)
    print(count, lst_of_k_div)



numb_of_k_div(n)

# for i in range(1,n+1):
#     a = 0
#     for z in range(1,i+1):
#         if i%z == 0:
#             a +=1
#         if a>=k:
#             print(i)