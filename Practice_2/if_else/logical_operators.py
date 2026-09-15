#and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#or
d = 200
e = 33
f = 500
if d > e or d > f:
  print("At least one of the conditions is True")

#not
g = 33
h = 200
if not g > h:
  print("g is NOT greater than h")

#combining operators
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

#parentheses to make your intentions clear
temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")
