# filter() offers a convenient way to filter out all the elements of an
# iterable, for which elements that are True to a parameter function.

# filter(function, list) needs a function as its first argument. The function
# needs to return a Boolean value (True or False). This function will be
# applied to every element of the iterable. Only if the function returns True,
# the element of the iterable be included in the result.

def is_even(number):
    return number % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

print("Function filter() results:")
for number in filter(is_even, numbers):
    print(number)
