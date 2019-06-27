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

string = 'a ab abb abbb'
patterns = ['ab*', 'ab+', 'ab?', 'ab{2}', 'ab{3,4}']
# 'ab*'     - a followed by 0 or more b's
# 'ab+'     - a followed by 1 or more b's
# 'ab?'     - # a followed by 0 or 1 d
# 'ab{3}'   - a followed by 3 b's
# 'ab{2,3}' - a followed by 2 to 3 b's

find_patterns(patterns, string)
