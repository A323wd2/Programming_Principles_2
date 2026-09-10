#strings are inside quotes
print("Hello")
print('Hello')

#quotes in quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#assighning string to a variable
a = "Hello"
print(a)

#multiple strings using 3 double quuotes
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

#or 3 single quotes
c = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(c)

#strings are arrays, example of outputting the element with id 1(it starts with 0)
d = "Hello, World!"
print(d[1])

#looping through string
for e in "banana":
  print(e)

#string lenght with len() function
f = "Hello, World!"
print(len(f))

#checking if a certain phrase or character is present in a string
txt = "The best things in life are free!"
print("free" in txt)

#using if
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#if not
txt2 = "The best things in life are free!"
print("expensive" not in txt2)
