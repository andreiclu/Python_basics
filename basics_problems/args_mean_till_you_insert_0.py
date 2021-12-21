"""
Se citesc numere naturale pana cand se introduce numarul 0.

Sa se afiseze media aritmetica a numerelor introduse.

"""



def ma(*args):
    rez = 0
    count = 0
    for arg in args:
        rez += arg
        count +=1
        if arg == 0:
            return (rez/(count-1))

if __name__ == '__main__':

    print(ma(1,2,3,4,5,6,7,8,0))
