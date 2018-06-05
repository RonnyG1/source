# Special Pythagorean triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.



natur_list= [x for x in range(1,1000)]


for i in natur_list:
    for j in natur_list[i:]:
        c_1 = (1000-(i+j))**2
        c_2 = (i**2 + j**2)
        if c_1 == c_2:
            print (i*j*(1000-(i+j)), "wynik")


