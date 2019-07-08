# Use enumerate() and other skills to return a dictionary which has the values
# of the list as keys and the index as the value. You may assume that a value
# will only appear once in the given list.

def convert_to_dictionary(letters):
    return {index: letter for letter, index in enumerate(letters)}

result = convert_to_dictionary(['a', 'b', 'c'])
print(result)
