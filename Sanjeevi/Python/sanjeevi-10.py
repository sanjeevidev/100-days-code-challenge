# Functions in Python

def func1():
    print("Hello World")
func1()

def var(x):
    print(x)
var(10)

#conditions in function
def func2(alist):
    if 4 in alist:
        print("The list contains 4")
    else:
        print("The list not contains 4")
func2([1,2,3,4,5])

#Built-in functions - #Refer https://www.w3schools.com/python/python_ref_functions.asp
def builtin(x,y):
    print(f"The absolute value of x : {abs(x)}")
    print(f"The sum of the given list : {sum(y)}")
    print(f"The length of the given list : {len(y)}")
    print(f"The minimum value in the given list : {min(y)}")
    print(f"The maximum value in the given list : {max(y)}")
builtin(-1,[10,20,30,40,50])

#global and local variable
length = 50 #global()
def area():
    breadth = 200 #local()
    area = length*breadth
    print("The area of Rectangle is",area)
area()

#Recursive Functions
def fact(num):
    if num == 0:
       return 1
    else:
        return num*fact(num-1)
print(f"The Factorial of 6 is {fact(6)}")

#Problem : To find a year is leap year or not using Function
def leap(year):
    for i in year:
        if i%4==0:
            print("The year is a leap year")
        else:
            print("The year is not a leap year")
leap([2004,2019,2023])