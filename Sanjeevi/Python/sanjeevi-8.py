# Loops in Python

# Range
print(range(5))
print(range(10))

#For loop
for i in range(10):
    print(i),"\n"

for year in ['2003','2004','2023','2024']:
    print(year),"\n"

arr = ['A','B','C','D','E']
print("\n")
for i in range(len(arr)):
    print(i,arr[i])

# Multiplication Table using for loop
print("\nMultiplication Table of 10\n")
for mul in range(1,11):
    print(mul,'* 10 = ',mul*10)

#Pyramid pattern using for loop
print("\nPyramid Pattern-5")
for i in range(6):
    print(i*'*')

#break - To terminate a loop
for br in range(1,10):
    if br==7:
        print("Terminated after 7")
        break
    print(br)

#continue - To skip an iteration
for br in range(1,10):
    if br==7:
        print("Skipped -7")
        continue
    print(br)

#Nested Loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)