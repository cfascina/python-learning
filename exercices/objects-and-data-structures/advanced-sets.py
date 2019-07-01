set_1 = set()
print("set_1 = set()")
print("set_1: " + str(set_1))

print("\nAdd")
set_1.add(1)
print("set_1.add(1)")
print("set_1: " + str(set_1))

set_1.add(2)
print("set_1.add(2)")
print("set_1: " + str(set_1))

print("\nClear")
set_1.clear()
print("set_1.clear()")
print("set_1: " + str(set_1))

print("\nCopy")
set_1 = {1, 2, 3}
set_2 = set_1.copy()
print("set_1: " + str(set_1))
print("set_2 = set_1.copy()")
print("set_2: " + str(set_2))
set_1.add(4)
print("set_1.add(4)")
print("set_1: " + str(set_1))
print("set_2: " + str(set_2))

print("\nDifference and Difference Update")
print("set_1: " + str(set_1))
print("set_2: " + str(set_2))
print("set_1.difference(set_2): " + str(set_1.difference(set_2)))
print("set_1: " + str(set_1))
set_1.difference_update(set_2)
print("set_1.difference_update(set_2)")
print("set_1: " + str(set_1))

print("\nDiscard")
set_1 = {1, 2, 3, 4}
print("set_1: " + str(set_1))
set_1.discard(2)
print("set_1.discard(2)")
print("set_1: " + str(set_1))

print("\nIntersection and Intersection Update")
set_1 = {1, 2, 3}
set_2 = {1, 2, 4}
print("set_1: " + str(set_1))
print("set_2: " + str(set_2))
print("set_1.intersection(set_2): " + str(set_1.intersection(set_2)))
print("set_1: " + str(set_1))
set_1.intersection_update(set_2)
print("set_1.intersection_update(set_2)")
print("set_1: " + str(set_1))

print("\nIs Disjoint")
set_1 = {1, 2}
set_2 = {1, 2, 3, 4}
set_3 = {3, 4}
print("set_1: " + str(set_1))
print("set_2: " + str(set_2))
print("set_3: " + str(set_3))
print("set_1.isdisjoint(set_2): " + str(set_1.isdisjoint(set_2)))
print("set_1.isdisjoint(set_3): " + str(set_1.isdisjoint(set_3)))

print("\nIs Subset and Is Superset")
set_1 = {1, 2}
set_2 = {1, 2, 3}
set_3 = {2, 3, 4}
print("set_1: " + str(set_1))
print("set_2: " + str(set_2))
print("set_3: " + str(set_3))
print("set_1.issubset(set_2): " + str(set_1.issubset(set_2)))
print("set_1.issubset(set_3): " + str(set_1.issubset(set_3)))
print("set_2.issuperset(set_1): " + str(set_2.issuperset(set_1)))
print("set_2.issuperset(set_3): " + str(set_2.issuperset(set_3)))

print("\nSymmetric Difference, Union and Update")
set_1 = {1, 2}
set_2 = {1, 2, 3}
print("set_1: " + str(set_1))
print("set_2: " + str(set_2))
print("set_1.symmetric_difference(set_2): " + str(set_1.symmetric_difference(set_2)))
print("set_1.union(set_2): " + str(set_1.union(set_2)))
print("set_1: " + str(set_1))
print("set_2: " + str(set_2))
set_1.update(set_2)
print("set_1.update(set_2)")
print("set_1: " + str(set_1))
print("set_2: " + str(set_2))
