# Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.


def palin(x):
    x = str(x)
    cnt=0
    for i in range(len(x)):
        if x[i] == x[len(x)-1-i]:
            cnt +=1
    if cnt ==len(x):
        return True
    else:
        return False

lista =[]
for x in range(100,1000):
    for y in range(100,1000):
        if palin(x*y):
            lista.append(x*y)

print (max(lista))
