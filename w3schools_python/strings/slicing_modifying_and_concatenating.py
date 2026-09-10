#get charachters through index range from 2 to 5(not included
a = "Hello, World!"
print(a[2:5])

#from start
b = "Hello, World!"
print(b[:5])

#to end
c = "Hello, World!"
print(c[2:])

#negative indexes
d = "Hello, World!"
print(d[-5:-2])

#upper()
e = "Hello, World!"
print(e.upper())

#lower()
f = "Hello, World!"
print(f.lower())

#strip()
g = " Hello, World! "
print(g.strip()) # returns "Hello, World!"

#replace()
h = "Hello, World!"
print(h.replace("H", "J"))

#split()
i = "Hello, World!"
print(i.split(",")) # returns ['Hello', ' World!']

#combining with + operator
j = "Hello"
k = "World"
l = j + k
print(l)

#combining with + operator with white space
m = "Hello"
n = "World"
o = m + " " + n
print(o)
