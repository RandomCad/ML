from copy import deepcopy

pot = [2**i for i in range (0,100)]
print (pot)

b = a = [ "ich", "mag", "Kuchen"]
c = a[:]
d = deepcopy(a)
b[1] = "hasse"
c[2] = "Orange"
print ( a)
print (b)
print (c)
print (d)

squars = { (i, i**2) for i in range (0,100)}
print (squars)
keys = [i[0] for i in squars]
print (keys)

evan = [i for i in range(1,100) if i%2==0]
print (evan)
