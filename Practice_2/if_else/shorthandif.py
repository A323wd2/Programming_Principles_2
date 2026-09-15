#if you have only one statement to execute, you can put it on the same line as the if statement
a = 5
b = 2
if a > b: print("a is greater than b")

#if you have one statement for if and one for else, you can put them on the same line using a conditional expression
c = 2
d = 330
print("C") if c > d else print("D")

#one-line if/else to choose a value and assign it to a variable
x = 10
y = 20
bigger = x if x > y else y
print("Bigger is", bigger)

#multiple conditions on one line
q = 330
w = 330
print("Q") if q > w else print("=") if q == w else print("W")
