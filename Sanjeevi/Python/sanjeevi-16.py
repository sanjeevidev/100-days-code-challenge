#Constructors in Python

class Constructor:
	#default constructor
	def __init__(self):
		self.geek = "Constructor"
		
	def print_cons(self):
		print(self.geek)
# Creating object of the class
obj = Constructor()
# Calling the instance method using the object obj
obj.print_cons()

#Addition of two numbers with constructors
class Addition:
	first = 0
	second = 0
	answer = 0
	def __init__(self, f, s):
		self.first = f
		self.second = s

	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second

obj1 = Addition(1000, 2000)
obj2 = Addition(10, 20)

obj1.calculate()
obj2.calculate()

obj1.display()
obj2.display()

#Types of constructor
class MyClass:
	def __init__(self, name=None):
		if name is None:
			print("Default constructor called")
		else:
			self.name = name
			print("Parameterized constructor called with name", self.name)
	
	def method(self):
		if hasattr(self, 'name'):
			print("Method called with name", self.name)
		else:
			print("Method called without a name")

# Create an object of the class using the default constructor
obj1 = MyClass()
# Call a method of the class
obj1.method()

# Create an object of the class using the parameterized constructor
obj2 = MyClass("John")
# Call a method of the class
obj2.method()