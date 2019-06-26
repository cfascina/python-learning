import re

patterns = ['for', 'regular', 'word']
my_string = "String for testing regular expressions."

print("Searching for patterns at the following string:")
print(my_string)

for pattern in patterns:
    print(f"\nSearching for pattern: '{pattern}'")
    if re.search(pattern, my_string):
        print("Pattern found.")
    else:
        print("Pattern not found.")
