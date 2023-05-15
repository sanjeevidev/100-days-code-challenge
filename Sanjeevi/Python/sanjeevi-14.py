# Decorators in Python

def hello_decorator(func):
	def inner1():
		print("Hello, this is before function execution")
		func()
		print("This is after function execution")
	return inner1

def function_to_be_used():
	print("This is inside the function !!")
	
function_to_be_used = hello_decorator(function_to_be_used)
function_to_be_used()

#To find out the execution time of a function using a decorator.
import time
import math
def calculate_time(func):
	def inner1(*args, **kwargs):
		begin = time.time()	
		func(*args, **kwargs)
		end = time.time()
		print("Total time taken in : ", func.__name__, end - begin)
	return inner1

@calculate_time
def factorial(num):
	time.sleep(2)
	print(math.factorial(num))
	
factorial(10)

#Chaining Decorators
def decor1(func):
	def inner():
		x = func()
		return x * x
	return inner

def decor(func):
	def inner():
		x = func()
		return 2 * x
	return inner

@decor1
@decor
def num():
	return 10

@decor
@decor1
def num2():
	return 10

print(num())
print(num2())