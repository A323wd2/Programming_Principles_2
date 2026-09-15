#while
i = 1
while i < 6:
  print(i)
  i += 1

#break
w = 1
while w < 6:
  print(w)
  if w == 3:
    break
  w += 1

#continue
q = 0
while q < 6:
  q += 1
  if q == 3:
    continue
  print(q)

#else
e = 1
while e < 6:
  print(e)
  e += 1
else:
  print("e is no longer less than 6")
