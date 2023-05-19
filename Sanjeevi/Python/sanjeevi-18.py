# Inheritance 

class Person(object):
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)

class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post
		Person.__init__(self, name, idnumber)

a = Employee('Sanjeevi', 886012, 200000, "Student")
a.display()

#Single Inheritance
class Base1(object):
	def __init__(self):
		self.str1 = "Geek1"
		print("Base1")

class Base2(object):
	def __init__(self):
		self.str2 = "Geek2"
		print("Base2")

class Derived(Base1, Base2):
	def __init__(self):
		Base1.__init__(self)
		Base2.__init__(self)
		print("Derived")

	def printStrs(self):
		print(self.str1, self.str2)

ob = Derived()
ob.printStrs()

#Multiple Inheritance
class Mother:
	mothername = ""
	def mother(self):
		print(self.mothername)
		
class Father:
	fathername = ""
	def father(self):
		print(self.fathername)
		
class Son(Mother, Father):
	def parents(self):
		print("Father :", self.fathername)
		print("Mother :", self.mothername)

s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()

#Multilevel Inheritance
class Base(object):
	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

class Child(Base):
	def __init__(self, name, age):
		Base.__init__(self, name)
		self.age = age
		
	def getAge(self):
		return self.age

class GrandChild(Child):
	def __init__(self, name, age, address):
		Child.__init__(self, name, age)
		self.address = address
		
	def getAddress(self):
		return self.address

g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())

#Hierarichal Inheritance
class Parent:
	def func1(self):
		print("This function is in parent class.")

class Child1(Parent):
	def func2(self):
		print("This function is in child 1.")

class Child2(Parent):
	def func3(self):
		print("This function is in child 2.")

object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

#Hybrid Inheritance
class School:
	def func1(self):
		print("This function is in school.")

class Student1(School):
	def func2(self):
		print("This function is in student 1. ")

class Student2(School):
	def func3(self):
		print("This function is in student 2.")

class Student3(Student1, School):
	def func4(self):
		print("This function is in student 3.")

object = Student3()
object.func1()
object.func2()