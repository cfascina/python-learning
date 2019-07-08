# Use filter to return the words from a list of words
# which start with a target letter.

def filter_words(word_list, letter):
    return list(filter(lambda word: word[0] == letter, word_list))

words = ['hello', 'are', 'cat', 'dog', 'ham', 'hi', 'go', 'to', 'heart']
result = filter_words(words, 'h')
print(result)
