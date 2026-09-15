#pass
a = 33
b = 200

if b > a:
  pass

#pass in development
age = 20

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")

#pass with comments
score = 85

if score > 90:
  pass # This is a comment
print("Score processed")

#pass in different branches
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")
