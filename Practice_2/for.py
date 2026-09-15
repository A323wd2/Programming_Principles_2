#for
fruits = ["apple", "banana", "cherry"]
for a in fruits:
  print(a)

#looping through string
for n in "banana":
  print(n)

#break
fruits2 = ["apple", "banana", "cherry"]
for b in fruits2:
  print(b)
  if b == "banana":
    break

#continue
fruits3 = ["apple", "banana", "cherry"]
for c in fruits3:
  if c == "banana":
    continue
  print(c)

#range()
for t in range(6):
  print(t)

#else
for f in range(6):
  print(f)
else:
  print("Finally finished!")

#nested loop
adj = ["red", "big", "tasty"]
fruits4 = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits4:
    print(x, y)

#pass in for

for k in [0, 1, 2]:
  pass
