# reduce(function, sequence) continually applies the function to a sequence,
# returning a single value.

# If whe have the following list: [1, 2, 3, 4, 5], and a function add(), calling
# reduce(add, list), will works like this:

# 1. The add() function will be called for the first two elements of the
# list: add(1, 2).
# 2. The list on wich reduce will look like this: [(1 + 2), 3, 4, 5],
# the same as [3, 4, 5].
# 3. In the next step, the add() function will be applied on the previous result
# and the third element of the list: add((1 + 2), 3), or add(3, 3).
# 4. It continues like this until just one element is left in the list and return
# this element as the result of reduce().

from functools import reduce

list =[1, 2, 3, 4, 5]
results = reduce(lambda x, y: x + y, list)

print("Function reduce() results:")
print(results)
