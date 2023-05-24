# User-defined Exceptions

#Example-1
class MyError(Exception):

	def __init__(self, value):
		self.value = value

	def __str__(self):
		return(repr(self.value))

try:
	raise(MyError(3*2))
except MyError as error:
	print('A New Exception occurred: ', error.value)

#Example-2 with Inheritance
class Error(Exception):
	"""Base class for other exceptions"""
	pass

class zerodivision(Error):
	"""Raised when the input value is zero"""
	pass

try:
	i_num = int(input("Enter a number: "))
	if i_num == 0:
		raise zerodivision
except zerodivision:
	print("Input value is zero, try again!")
	print()

#Example-3 with Super Class
class Error(Exception):
	pass

class TransitionError(Error):
	def __init__(self, prev, nex, msg):
		self.prev = prev
		self.next = nex
		self.msg = msg

try:
	raise(TransitionError(2, 3*2, "Not Allowed"))

except TransitionError as error:
	print('Exception occurred: ', error.msg)

#Example-4 as base class
class Networkerror(RuntimeError):
	def __init__(self, arg):
		self.args = arg

try:
	raise Networkerror("Error")

except Networkerror as e:
	print(e.args)