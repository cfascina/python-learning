# Use enumerate() and other skills to return the count of the number of items in
# the list whose value equals its index.

def count_match_index(numbers):
    return len([number for index, number in enumerate(numbers) if index == number])

result = count_match_index([0, 2, 2, 1, 5, 5, 6, 10])
print(result)
