pra1 = 10
pra2 = 14
pra3 = 12


if (pra1 >= pra2) and (pra1 >= pra3):
   largest = pra1
elif (pra2 >= pra1) and (pra2 >= pra3):
   largest = pra2
else:
   largest = pra3

print("The largest number between",pra1,",",pra2,"and",pra3,"is",largest)
