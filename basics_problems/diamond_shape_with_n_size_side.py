# Se citeste un numar natural n cu cel mult 2 cifre.
# Afisati pe ecran un romb cu latura n,
# format din caracterul #, ca in exemplul de mai jos pentru n=5.
    #
   ###
  #####
 #######
#########
 #######
  #####
   ###
    #

x = int(input('Give me a number up to 99: '))
sec_x = x
for i in range(1,x+1):
    print(' '*(x-1) + '#'*(2*i-1))
    x = x-1

for n in range(0,sec_x):
    print(' '*(n+1) + '#'*(2*(sec_x-1)-1))
    sec_x = sec_x - 1
