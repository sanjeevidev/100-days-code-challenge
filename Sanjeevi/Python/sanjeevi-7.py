# Dictionary Operations
sample = {'key_1': 3.14, 'key_2': 1.618,'key_3': True, 'key_4': False,'key_5':'Dictionary', 'key_6': 2023, 3.14: 'Pi', 1.618: 'Golden Ratio'}

#To get all keys in a dictionary
print(sample.keys())
#To get all values in a dictionary
print(sample.values())
#To get all items in a dictionary
print(sample.items())
#To add a new key-pair into the existing dictionary
sample['key_7']='Value Added'
print(sample)
#To remove/delete a key-pair
del(sample['key_7'])
print(sample)
#Membership operations
print('key_1'in sample)
print('key_1' not in sample)
#To remove all items in dictionary
sample.clear()
print(sample)
# To copy a dictionary
sample_copy = sample.copy()
print(sample)
print(sample_copy)
#To remove the specific element from the dictionary
sample.pop(3.14)
print(sample)
#To remove the abitrary/last element from the dictionary
sample.popitem()
print(sample)
# get() function - Returns the value of specified key if available ,if not returns None
print(sample.get('key_3'))
print(sample.get('Python'))
#fromkeys() function - Returns a new dictionary with certain items as keys and values are assigned to None
key = {'D','I','C','T'}
val = dict.fromkeys(key)
print(val)
#update() function - It integrates a dictionary with another dictionary or with an iterable of key:value pairs .
sample.update(val)
print(sample)
#setdefault() function - It returns the value of the key if the key is present in the dictionary ,else it returns the default value
print(sample.setdefault('key_7','Value Added'))