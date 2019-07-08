# Use zip() and a list comprehension to return a list of the same length where
# each value is the two strings from L1 and L2 concatenated together with
# connector between them.

def concatenate(list_1, list_2, connector):
    return [word_1 + connector + word_2 for (word_1, word_2) in zip(list_1, list_2)]

result = concatenate(['A','B'], ['a','b'], '-')
print(result)
