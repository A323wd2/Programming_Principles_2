#else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#without elif
c = 200
d = 33
if d > c:
  print("d is greater than c")
else:
  print("d is not greater than c")

#else statement acts as a fallback that executes when none of the preceding conditions are true
username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")
