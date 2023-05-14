#First Class Functions

# 1.Functions are objects
def upper(text):
	return text.upper()
print (upper('Hello'))

obj = upper
print (obj('Hello'))

# 2.Functions can be passed as arguments to other functions
def upper(text):
	return text.upper()

def lower(text):
	return text.lower()

def arg(func):
	greeting = func("Function passed as a Arguement")
	print (greeting)

arg(upper)
arg(lower)

# 3.Functions can return another function
def pre_adder(x):
	def adder(y):
		return x+y
	return adder

sum_15 = pre_adder(15)
print (sum_15(10))