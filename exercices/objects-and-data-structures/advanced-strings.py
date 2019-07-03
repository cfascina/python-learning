string = "Donald"
print(f"Changing Case - String '{string}'")
print("string.capitalize(): " + string.capitalize())
print("string.upper(): " + string.upper())
print("string.lower(): " + string.lower())

string = "Amanda"
print(f"\nLocation and Counting - String '{string}'")
print("string.count('a'): " + str(string.count('a')))
print("string.find('m'): " + str(string.find('m')))

string = "Kevin\tOwen"
print(f"\nFormatting - String 'Kevin\\tOwen'")
print("string.expandtabs(): " + string.expandtabs())
print("string.center(20, '-'): " + string.center(20, '-'))

string = "Python3 Rocks"
print(f"\nIs Check Methods - String '{string}'")
print("string.isalnum(): " + str(string.isalnum()))
print("string.isalpha(): " + str(string.isalpha()))
print("string.islower(): " + str(string.islower()))
print("string.isspace(): " + str(string.isspace()))
print("string.istitle(): " + str(string.istitle()))
print("string.isupper(): " + str(string.isupper()))
print("string.endswith('s'): " + str(string.endswith('s')))

string = "Michael"
print(f"\nBuilt-in Regular Expressions - String '{string}'")
print("string.split('c'): " + str(string.split('c')))
print("string.partition('c'): " + str(string.partition('c')))
