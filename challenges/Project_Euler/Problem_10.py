# Summation of primes

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.


import time
 
def prime_sum(n):
    if n < 2: return 0
    if n == 2: return 2
    if n % 2 == 0: n += 1
    primes = [True] * n
    primes[0],primes[1] = [None] * 2
    print(primes[:12], "primes do 12")
    sum = 0
    for ind,val in enumerate(primes):
        print(ind,val,"ind and val")
        if val is True and ind > n ** 0.5 + 1:
            print(ind, n ** 0.5 + 1,"-<<<<<")
            sum += ind
            print(sum, ind, "if")
        elif val is True:
            primes[ind*2::ind] = [False] * (((n - 1)//ind) - 1)
            print (((n - 1)//ind) )
            print(primes, "primes po modyfikacji elif")
            sum += ind
            print(sum,ind,'elif')
    return sum
 
start = time.time()
sum = prime_sum(30)
elapsed = (time.time() - start)
 
print ("found %s in %s seconds" % (sum,elapsed))