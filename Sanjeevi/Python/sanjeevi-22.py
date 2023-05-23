# Errors and Exceptions

#Syntax Errors
amount = 10000
if(amount<2999):#syntax error
	print("You are eligible to purchase Dsa Self Paced")

#Logical Errors
marks = 10000
a = marks / 0
print(a)

if(a<3):
    print("gfg")#Indentation error

#--ERROR HANDLING--#
#Example-1
try:
	print("code start")
	print(1 / 0)

except:
	print("an error occurs")

finally:
	print("GeeksForGeeks")
	
#Example-2
try:
	amount = 1999
	if amount < 2999:
		raise ValueError("please add money in your account")
	else:
		print("You are eligible to purchase DSA Self Paced course")
		
except ValueError as e:
		print(e)