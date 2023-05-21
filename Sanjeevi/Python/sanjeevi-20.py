# Polymorphism

#Example-1 len() method
print(len("geeks"))
print(len([10, 20, 30]))

#Example-2 Function call
def add(x, y, z = 0):
	return x + y+z

print(add(2, 3))
print(add(2, 3, 4))

#Example-3 With Inheritance


class Bird:
  def intro(self):
    print("There are many types of birds.")
     
  def flight(self):
    print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
    def flight(self):
	    print("Sparrows can fly.")
	
class ostrich(Bird):
    def flight(self):
	    print("Ostriches cannot fly.")
	
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

#Example-4 Method Overloading
class Animal:
	def speak(self):
		raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
	def speak(self):
		return "Woof!"

class Cat(Animal):
	def speak(self):
		return "Meow!"

animals = [Dog(), Cat()]

for animal in animals:
	print(animal.speak())