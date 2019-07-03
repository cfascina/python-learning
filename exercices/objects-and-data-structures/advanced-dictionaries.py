print("Dictionary Comprehensions")
print("-" * 25)
my_dict = {x: x ** 2 for x in range(5)}
print("{x: x ** 2 for x in range(5)}:")
print(my_dict)
my_dict = {key: value ** 2 for key, value in zip(['key1', 'key2'], range(10))}
print("\n{key: value ** 2 for key, value in zip(['key1', 'key2'], range(10))}:")
print(my_dict)

print("\nIteration over Items, Keys and Values")
print("-" * 37)
my_dict = {'key1': 1, 'key2': 2}
print(f"my_dict: {my_dict}")

my_arr = []
for item in my_dict.items():
    my_arr.append(item)
print(f"Items: {my_arr}")

my_arr.clear()
for key in my_dict.keys():
    my_arr.append(key)
print(f"Keys: {my_arr}")

my_arr.clear()
for value in my_dict.values():
    my_arr.append(value)
print(f"Values: {my_arr}")

print("\nViewing Items, Keys and Values")
print("-" * 30)
my_dict = {'key1': 1, 'key2': 2}
print(f"my_dict: {my_dict}")
print(f"my_dict.items(): {my_dict.items()}")
print(f"my_dict.keys(): {my_dict.keys()}")
print(f"my_dict.values(): {my_dict.values()}")
