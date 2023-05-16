#Class and Objects

class Dog:
	attr1 = "mammal"
	attr2 = "dog"

	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)

Rodger = Dog()
print(Rodger.attr1)
Rodger.fun()

#self parameter can be replaced by another name
class DET:
	def __init__(somename, name, place):
		somename.name = name
		somename.place = place

	def show(somename):
		print("Hello my name is " + somename.name +
			" and I work in "+somename.place+".")

obj = DET("Sanjeevi", "Coimbatore")
obj.show()

#__str__ method
class EXP:
	def __init__(self, name, place):
		self.name = name
		self.place = place

	def __str__(self):
		return f"My name is {self.name} and I work in {self.place}."

my_obj = EXP("Sasuke", "Coimbatore")
print(my_obj)

#Instance Variable
# Python3 program to show that the variables with a value
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.

# Class for Dog


class Dog:
	animal = 'dog'

	def __init__(self, breed, color):
		self.breed = breed
		self.color = color

Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)
print("\nAccessing class variable using class name")
print(Dog.animal)