#Loops in Python
#While loop
i = 1
while i<11:
 print(i)
 i+=1

#Looping through List
a = [1, 2, 3, 4]
while a:
    print(a.pop())

# Single statement while block
sum = 0
while (sum < 5): sum += 1; print("Sum",sum)

#break - Terminates iteration in while loop
i = 0
a = 'Programming'
while i < len(a):
	if a[i] == 'm' or a[i] == 'g':
		i += 1
		break
		
	print('Current Letter :', a[i])
	i += 1
        
#continue - Skips iteration in while loop
i = 0
a = 'Programming'
while i < len(a):
	if a[i] == 'm' or a[i] == 'g':
		i += 1
		continue
		
	print('Current Letter :', a[i])
	i += 1
	
#pass - If any error persists skips
a = 'Programming'
i = 0
while i < len(a):
	i += 1
	pass

print('Value of i :', i)

#User defined condition
a = int(input('Enter a number (<0 to quit): '))
while a > -1:
	a = int(input('Enter a number (<0 to quit): '))