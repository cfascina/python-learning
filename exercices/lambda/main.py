print("Lambda expressions are anonymous functions that you will use only once.")

print("\nLet's convert the square() function into a lambda expression:")

print("\nStep 1:")
print("def square(number):")
print("\tresult = number ** 2")
print("\treturn result")

print("\nStep 2:")
print("def square(number):")
print("\treturn number ** 2")

print("\nStep 3:")
print("def square(number): return number ** 2")

print("\nStep 4, the final lambda expression:")
print("lambda number: number ** 2")

print("\nApplying it w/ the map(function):")
print("numbers = [1, 2, 3, 4, 5]")
print("for number in map(lambda number: number ** 2, numbers):")
print("\tprint(number)")

print("\nWill result in:")
numbers = [1, 2, 3, 4, 5]
for number in map(lambda number: number ** 2, numbers):
    print(number)
