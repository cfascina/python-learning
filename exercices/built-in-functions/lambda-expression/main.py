# Lambda expressions are anonymous functions that you will use only once.
# The following square() function will be converted into a lambda expression,
# step by step.

# Step 1:
# def square(number):
#     result = number ** 2
#     return result

# Step 2:
# def square(number):
#     return number ** 2

# Step 3:
# def square(number): return number ** 2

# Step 4, final lambda expression:
# lambda number: number ** 2"

numbers = [1, 2, 3, 4, 5]

for number in map(lambda number: number ** 2, numbers):
    print(number)

# This code does exactly the same thing as the following, but we don't need to
# declare the function square(), since we will only use it once.

# for number in map(square, numbers):
#     print(number)
