# Destructors in Python

class Employee:
	def __init__(self):
		print('Employee created.')
	def __del__(self):
		print('Destructor called, Employee deleted.')

obj = Employee()
del obj

#Example-2
class Employee:
	def __init__(self):
		print('Employee created')
	def __del__(self):
		print("Destructor called")

def Create_obj():
	print('Making Object...')
	obj = Employee()
	print('function end...')
	return obj

print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')

#Example-3
class RecursiveFunction:
	def __init__(self, n):
		self.n = n
		print("Recursive function initialized with n =", n)

	def run(self, n=None):
		if n is None:
			n = self.n
		if n <= 0:
			return
		print("Running recursive function with n =", n)
		self.run(n-1)

	def __del__(self):
		print("Recursive function object destroyed")
obj = RecursiveFunction(5)
obj.run()
del obj