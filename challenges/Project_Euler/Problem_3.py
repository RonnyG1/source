# Largest prime factor

#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?


num = 600851475143
for x in range(num+1):

    if x > 2:
       # check for factors
       for i in range(2,x):
           if (x % i) == 0:
               break
       else:
        print ("x", x)
        if num % x == 0:
            print(x)
        #print(x,"is a prime number")
           
    # if input number is less than
    # or equal to 1, it is not prime
    else:
       pass