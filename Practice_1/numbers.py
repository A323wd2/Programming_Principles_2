#int type
a = 1
b = 35656222554887711
c = -3255522

print(type(a))
print(type(b))
print(type(c))

#float type
d = 1.10
e = 1.0
f = -35.59e10

print(type(d))
print(type(e))
print(type(f))

#complex type
g = 3+5j
h = 5j
i = -5j

print(type(g))
print(type(h))
print(type(i))

#converting type
j = 1
k = 2.8
l = 1j


m = float(j)
n = int(k)
o = complex(l)

print(m)
print(n)
print(o)

print(type(m))
print(type(n))
print(type(o))

#random number
import random

print(random.randrange(1, 10))
