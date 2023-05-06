# Sets Operations
x = {'Hello Python!', 3.14, 1.618, 'Hello World!', 3.14, 1.618, True, False, 2023,'Sets'}
y = {3.14, 1.618, True, False, 2023,'Sets'}

#Add - To add an single element
x.add('7')
print(x)
#Update - To add multiple elements
x.update({2,0,2,3})
print(x)
#Remove - To delete an element from set
x.remove(1.618)
print(x)
#Discard - It leaves the set unchanged if the element is not available
x.discard(3.14)
print(x)
#Intersection - Returns the common elements in two sets
i1 = y.intersection(set(x))
print(i1)
#Union - Returns the union of two sets
u1 = y.union(x)
print(u1)
#Difference - Returns the set difference of two sets
d1 = y.difference(x)
print(d1)
#Symmetric Difference - Returns the symmetric difference of two sets
sd1 = y.symmetric_difference(x)
print(sd1)
#Copy - Returns a shallow copy of the set
c1 = y.copy()
print(c1)
#Pop - Returns and removes the last element of the set
p1 = y.pop()
print(y)
#Isdisjoint - Returns True if the two sets have no common elements  
dis1 = y.isdisjoint(x)
print(dis1)
#Issubset - Returns True if the set is a subset of the other set
sub1 = y.issubset(x)
print(sub1)
#Issuperset - Returns True if the set is a superset of the other set
sup1 = x.issuperset(y)
print(sup1)
#Clear - Deletes all the elements from the set
cl1 = y.clear()
print(y)