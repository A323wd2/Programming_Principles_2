#creating variable outside of a function and using it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#creating variable inside a function with the same name as the global variable
a = "awesome"

def myfunc():
  a = "fantastic"
  print("Python is " + a)

myfunc()

print("Python is " + a)

#global variable inside a function
def myfunc():
  global b
  b = "cool"

myfunc()

print("Python is " + b)

#changing global variable
c = "hard"

def myfunc():
  global c
  c = "easy"

myfunc()

print("Python is " + c)
