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

string = "Just a test sentence. Trying to find some patterns."
patterns = ['[a-z]+', '[A-Z]+', '[a-zA-Z]+', '[A-Z][a-z]+']
# '[a-z]+'          - sequences of lower case letters
# '[A-Z]+'          - sequences of upper case letters
# '[a-zA-Z]+'       - sequences of lower or upper case letters
# '[A-Z][a-z]+']    - one upper case letter followed by lower case letters

find_patterns(patterns, string)
