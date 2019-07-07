def is_even(number):
    return number % 2 == 0

numbers = [1, 2, 3, 4, 5]

print("The filter() function is similar to map() function.")
print("But it returns only the elements that are true to the parameter function.")
for number in filter(is_even, numbers):
    print(number)
