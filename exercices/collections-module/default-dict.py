from collections import defaultdict

my_dictionary = defaultdict(object)
print("Var 'my_dictionary' created as a defaultdict.")

my_dictionary['k1']
my_dictionary['k2']
print("\nSome key's for 'my_dictionary' created (no values assigned):")
print(my_dictionary)

print("\nPrinting 'my_dictionary':")
for item in my_dictionary:
    print(item + ': ' + str(my_dictionary[item]))

my_dictionary = defaultdict(lambda: 0)
print("\nVar 'my_dictionary' created as a defaultdict w/ '0' as default value.")

my_dictionary['k1']
my_dictionary['k2']
print("\nSome key's for 'my_dictionary' created:")
print(my_dictionary)

print("\nPrinting 'my_dictionary':")
for item in my_dictionary:
    print(item + ': ' + str(my_dictionary[item]))
