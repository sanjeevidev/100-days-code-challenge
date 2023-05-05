# Tuple Operation
tuple_1 = ('Hello', 'Python', 3.14, 1.618, True, False, 32, [1,2,3], {1,2,3},(0, 1))
tuple_2 = (7,5,3,9,1,2,4,8,6)

#Indexing
print(f"{tuple_1[0]} {tuple_1[1]}")
#Concantenation
print(f"{tuple_1[0]} {tuple_2[3]}")
#Repetition
print(tuple_2*2)
#Membership Operation [is,is not,in,not in,Assignment Operators also included]
print(tuple_1[2] == 3.14)
#tuplefunction - creates a tuple
print(tuple('DATA TYPES'))
#Slicing 
print(tuple_1[:2])
#Sorting tuple
print(sorted(tuple_2))
#Count
print(len(tuple_1))
#Index
print(tuple_1.index(1.618))