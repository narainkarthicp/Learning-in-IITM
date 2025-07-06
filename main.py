# ToDo: I need formal understanding of class and object.

class my_class: #class name
    x = 10 # property (or) attributes

# creating an object for the class
p1 = my_class() # why I'm using () ? // it's special kind of __init__() it will call automatically -> ()
print(p1.x) # will print the value of x in the class



class Person:
  def __init__(self):
    self.name = 34
    self.age = 34
  def display(self):
      print(self.name, self.age,"Yeah it's printed !! ")

p1 = Person()

print(p1.name)
print(p1.age)
