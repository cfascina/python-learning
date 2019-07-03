print("Append()")
print("-" * 8)
my_list = [1, 2, 3]
print(f"my_list: {my_list}")
my_list.append(4)
print("my_list.append(4)")
print(f"my_list: {my_list}")

print("\nCount()")
print("-" * 7)
my_list = [1, 2, 2, 2]
print(f"my_list: {my_list}")
print(f"my_list.count(1): {my_list.count(1)}")
print(f"my_list.count(2): {my_list.count(2)}")

print("\nExtend()")
print("-" * 8)
my_list = [1, 2, 3]
print(f"my_list: {my_list}")
my_list.extend([4, 5])
print("my_list.extend([4, 5])")
print(f"my_list: {my_list}")

print("\nIndex()")
print("-" * 7)
my_list = [1, 2, 3]
print(f"my_list: {my_list}")
print(f"my_list.index(1): {my_list.index(1)}")
print(f"my_list.index(2): {my_list.index(2)}")
print(f"my_list.index(3): {my_list.index(3)}")

print("\nInsert()")
print("-" * 8)
my_list = [1, 2, 4, 5]
print(f"my_list: {my_list}")
my_list.insert(2, 3)
print("my_list.insert(2, 3)")
print(f"my_list: {my_list}")

print("\nPop()")
print("-" * 5)
my_list = [1, 2, 3, 4, 5]
print(f"my_list: {my_list}")
my_list.pop()
print("my_list.pop()")
print(f"my_list: {my_list}")
my_list.pop(2)
print("my_list.pop(2)")
print(f"my_list: {my_list}")

print("\nRemove()")
print("-" * 8)
my_list = [1, 2, 3, 3]
print(f"my_list: {my_list}")
my_list.remove(3)
print("my_list.remove(3)")
print(f"my_list: {my_list}")

print("\nReverse()")
print("-" * 9)
my_list = [1, 2, 3]
print(f"my_list: {my_list}")
my_list.reverse()
print("my_list.reverse()")
print(f"my_list: {my_list}")

print("\nSort() and Sort(reverse = True)")
print("-" * 21)
my_list = [2, 1, 4, 5, 3]
print(f"my_list: {my_list}")
my_list.sort()
print("my_list.sort()")
print(f"my_list: {my_list}")

my_list = [2, 1, 4, 5, 3]
print(f"\nmy_list: {my_list}")
my_list.sort(reverse = True)
print("my_list.sort(reverse = True)")
print(f"my_list: {my_list}")

print("\nAssignment")
print("-" * 10)
my_list_1 = [1, 2, 3]
print(f"my_list_1: {my_list_1}")
my_list_2 = my_list_1.append(4)
print("my_list_2 = my_list_1.append(4)")
print(f"my_list_2: {my_list_2}")
print("This doesn't work. You must copy 'my_list_1' to 'my_list_2' and then append the value:")
my_list_1 = [1, 2, 3]
print(f"my_list_1: {my_list_1}")
my_list_2 = my_list_1.copy()
print("my_list_2 = my_list_1.copy()")
my_list_2.append(4)
print("my_list_2.append(4)")
print(f"my_list_2: {my_list_2}")
print(f"my_list_1: {my_list_1}")
