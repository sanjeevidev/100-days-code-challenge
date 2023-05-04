# List Operations
alist = [1,1,2,3,5,8,13,21,34]
blist = 'P,Y,T,H,O,N'
#Finding length method
print(len(alist))
#Slicing method
print(alist[1:3])
#Extending list method
alist.extend([1, 2, 3, 4, 5])
print(alist)
#Appending list method
alist.append([6, 7, 8, 9, 10])
print(alist)
#Count method
print(alist.count(1))
#Index method
print(alist.index(13))
#Update an element
alist[0]="List Methods"
print(alist)
#Split Method
print(blist.split("-"))