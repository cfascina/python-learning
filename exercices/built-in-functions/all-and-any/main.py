# all() and any() are built-in functions in Python that allow us to
# conveniently check for boolean matching in an iterable.
# all() will return True if all elements in an iterable are True.
# any() will return True if any of the elements in the iterable are True.

list_1 = [True, True, True]
list_2 = [False, False, False]
list_3 = [False, True, False]
print(f"list_1: {list_1}")
print(f"list_2: {list_2}")
print(f"list_3: {list_3}")

print(f"\nall(list_1): {all(list_1)}")
print(f"all(list_2): {all(list_2)}")
print(f"all(list_3): {all(list_3)}")

print(f"\nany(list_1): {any(list_1)}")
print(f"any(list_2): {any(list_2)}")
print(f"any(list_3): {any(list_3)}")
