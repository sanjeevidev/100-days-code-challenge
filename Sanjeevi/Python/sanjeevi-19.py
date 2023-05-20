# Encapsulation

#Protected members
class Base:
	def __init__(self):
		self._a = 2

class Derived(Base):
	def __init__(self):
		Base.__init__(self)
		print("Calling protected member of base class: ",
			self._a)
		self._a = 3
		print("Calling modified protected member outside class: ",
			self._a)

obj1 = Derived()
obj2 = Base()

print("Accessing protected member of obj1: ", obj1._a)
print("Accessing protected member of obj2: ", obj2._a)

#Private members

class Base:
	def __init__(self):
		self.a = "GeeksforGeeks"
		self.__c = "GeeksforGeeks"

class Derived(Base):
	def __init__(self):
		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__c)

obj1 = Base()
print(obj1.a)