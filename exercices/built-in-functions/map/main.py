# The map function receives a function as the first parameter, and an object to
# be iterade as the second parameter. Using it inside a for loop, the elements
# inside the object will be automatically iterade within the function.

# map() takes 2 or more arguments: a function and one or more iterables,
# in the form:
# map(function, iterable, ...)

# map() returns an iterator - that is, map() returns a special object where the
# iterables passed automatically by the the function.

def square(number):
    return number ** 2

numbers = [1, 2, 3]

print("Function map() results:")
for number in map(square, numbers):
    print(number)

# map() can accept more than one iterable, since they have the same length.
# In the following example, we added the elements of the first list w/ the
# elements of the second list, using a lambda expression instead of a
# previously defined function:

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

print("\nFunction map() w/ two iterables results:")
for number in map(lambda x, y: x + y, list_1, list_2):
    print(number)
