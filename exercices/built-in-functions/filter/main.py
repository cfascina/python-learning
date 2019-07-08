# The filter() function is similar to map() function.
# But it only returns elements that are returned as True
# from the parameter function.

def is_even(number):
    return number % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

for number in filter(is_even, numbers):
    print(number)
