
"""
16.	Write a program in which:
-	Write a method in which we generate first m numbers divisible by n. In this case, we want to get in a list and print the first 500 numbers divisible by 7.
-	save all of those numbers in a file, one number per each row. The file will be called „file_numbers.txt”
In the next steps, we’re interested in using as little memory as possible.
-	create a generator which does exactly the same thing as above: generate the first 500 numbers divisible by 7 (the number of numbers generated is parametrizable) and save it to a file called “file_numbers_new.txt”
-	read the numbers from file (“file_numbers_new.txt”) and compute their average without keeping the entire list in memory.
"""



def first_m_div_by_n(m, n):
    divs = []
    for i in range(m):
        divs.append(i * n)
    f = open("file_numbers.txt", "w")
    for elem in divs:
        f.write(str(elem)+'\n')
    f.close()

first_m_div_by_n(500,7)


def generator_div(m, n):
    for i in range(m):
        yield i*n

def write_gen_to_file(m,n):
    f = open("file_name_new.txt", 'w')

    for i in generator_div(m,n):
        f.write(str(i)+'\n')
    f.close()

write_gen_to_file(500,7)

def avg_of_file():
    count = 0
    s = 0
    with open("file_name_new.txt", 'r') as fp:

        for line in fp:
            nr = int(line)
            s += nr
            count +=1
    return s/count


print(avg_of_file())
