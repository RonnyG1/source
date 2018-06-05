# Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time

start = time.time()

lista = [x for x in range(21) if x >10]
print (lista)

x =10
while True:
    for i in lista:
        if x%i !=0:
            break
    else:
        print (x)
        break
    x += 10