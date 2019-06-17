my_list = [1, 2, 3, 4, 5]

list_as_generator = (item for item in my_list if item > 3)

print("Generator 'list_as_generator' results:")
for item in list_as_generator:
    print(item)
