# The map function receives a function as the first parameter, and an object to
# be iterade as the second parameter. Using it inside a for loop, the elements
# inside the object will be automatically iterade within the function.

def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5]

for number in map(square, numbers):
    print(number)

# Using a for loop, to obtain the same results reached w/ the map function, the
# code would be like the following:
# for number in numbers:
    # print(square(number))
