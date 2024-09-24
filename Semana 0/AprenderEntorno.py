"""
print('Hello WORLD')

if(4>3):
    print("HELLO")
"""
"""
x,y,z = 1,2,3    

print(x)
print(y)
print(z)
"""
"""
Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables
This is called unpacking.
"""
"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
"""
"""
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
"""

x = "awesome"

"""
def myfunc():
  global x
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
print(type(x))
"""

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))