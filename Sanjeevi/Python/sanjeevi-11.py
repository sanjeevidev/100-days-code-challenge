#Generators in Python

calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"
print(calc(20))

string = 'Generators'
# lambda returns a function object
print(lambda string: string)

filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("filter_nums():", filter_nums("Geeks101"))
do_exclaim = lambda s: s + '!'
print("do_exclaim():", do_exclaim("I am tired"))
find_sum = lambda n: sum([int(x) for x in str(n)])
print("find_sum():", find_sum(101))

def cube(y):
	print(f"Finding cube of number:{y}")
	return y * y * y
lambda_cube = lambda num: num ** 3
# invoking simple function
print("invoking function defined with def keyword:")
print(cube(30))
# invoking lambda function
print("invoking lambda function:", lambda_cube(30))

l = ["1", "2", "9", "0", "-1", "-2"]
print("Sorted numerically:",
	sorted(l, key=lambda x: int(x)))
print("Filtered positive even numbers:",
	list(filter(lambda x: not (int(x) % 2 == 0 and int(x) > 0), l)))
print("Operation on each item using lambda and map()",
	list(map(lambda x: str(int(x) + 10), l)))

# Example list
my_list = [1, 2, 3, 4, 5]
# Use lambda to filter out even numbers from the list
new_list = list(filter(lambda x: x % 2 != 0, my_list))
# Print the new list
print(new_list)