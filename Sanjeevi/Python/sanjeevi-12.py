#Global and Local Keywords

def f():
	# local variable
	s = "I love Python"
	print(s)
f()

def f():
	# local variable
	s = "I love Python"
	print("Inside Function:", s)
f()
print(s)

# This function uses global variable s
def f():
	print("Inside Function", s)
# Global scope
s = "I love Python"
f()
print("Outside Function", s)

# This function has a variable with
# name same as s.
def f():
	s = "Me too."
	print(s)
# Global scope
s = "I love Python"
f()
print(s)

a = 1

# Uses global because there is no local 'a'
def f():
	print('Inside f() : ', a)

# Variable 'a' is redefined as a local
def g():
	a = 2
	print('Inside g() : ', a)
# Uses global keyword to modify global 'a'
def h():
	global a
	a = 3
	print('Inside h() : ', a)
# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)