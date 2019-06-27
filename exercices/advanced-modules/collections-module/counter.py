from collections import Counter

my_list = [1, 2, 2, 3, 4, 5, 5, 5]
items = Counter(my_list)
print("My list is: " + str(my_list))
print("Occurency of each item: " + str(items))
print("List of unique items: " + str(list(items)))
print("Set: " + str(set(items)))
print("Current Counter(): " + str(items))
print("Current Counter() cleaned: " + str(items.clear()))
print("Current Counter() rebooted: " + str(items + Counter()))

my_string = "test"
letters = Counter(my_string)
letters_list = letters.items()
letters_dictionary = dict(letters_list)
print("\nMy string is: " + str(my_string))
print("Occurency of each letter: " + str(letters))
print("Number of letters: " + str(sum(letters.values())))
print("List of (letter, occurency) pairs: " + str(letters_list))
print("Dicitionary: " + str(letters_dictionary))

my_phrase = "I am hungry. I am sleepy. But I will keep moving."
words = my_phrase.split()
words_counter = Counter(words)
words_dictionary = dict(words_counter)
print("\nMy phrase is: " + str(my_phrase))
print("Occurency of each word: " + str(words_counter))
print("The most common word: " + str(words_counter.most_common(1)))
print("The two most common words: " + str(words_counter.most_common(2)))
print("The least common words: " + str(words_counter.most_common()[:-6-1:-1]))
print("Dictionary: " + str(dict(words_counter)))
print("Dicitionary value of key 'am': " + str(words_dictionary['am']))
