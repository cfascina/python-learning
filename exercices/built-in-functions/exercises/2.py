# Use reduce() to take a list of digits and return the number that they
# correspond to. For example, [1, 2, 3] corresponds to one-hundred-twenty-three.
# Do not convert the integers to strings!

from functools import reduce

def digits_to_num(digits):
    return reduce(lambda x, y: x * 10 + y, digits)

result = digits_to_num([3, 4, 3, 2, 1])
print(result)
