import re

def find_patterns(patterns, string):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''

    print(f"Searching the string: '{string}'.")

    for pattern in patterns:
        print(f"\nWith the regex: {pattern}")
        print(f"Result: {re.findall(pattern, string)}")

string = 'a b ab aa aaa abb aba'
patterns = ['[ab]', 'a[ab]+']
# '[ab]'    - either a or b
# 'a[ab]+'  - a followed by 1 or more a or b

find_patterns(patterns, string)
