def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5]

print("Iteration w/ for loop:")
for number in numbers:
    print(square(number))

print("\nIteration w/ map:")
for number in map(square, numbers):
    print(number)
