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

string = "The password is admin@123"
patterns = [r'\d+', r'\D+', r'\s+', r'\S+', r'\w+', r'\W+']

# r'\d+' - sequence of digits
# r'\D+' - sequence of non-digits
# r'\s+' - sequence of whitespace
# r'\S+' - sequence of non-whitespace
# r'\w+' - alphanumeric characters
# r'\W+' - non-alphanumeric

find_patterns(patterns, string)
