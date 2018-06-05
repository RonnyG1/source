# 10001st prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?


primes = [2]

for i in range(3,1000000000000000,2):
    for x in range(3,int(i/2),2):
        if i%x == 0:
            break
    else:
        primes.append(i)
        if len(primes)>=10001:
            break
print(primes[-5:])