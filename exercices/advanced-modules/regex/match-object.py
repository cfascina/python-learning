import re

pattern = "apple"
my_string = "This apple is tasty."
print(f"Searching for '{pattern}' at '{my_string}'")

match = re.search(pattern, my_string)
print("\nIf no pattern is found, the result of re.search() method is 'None'.")
print(f"If a pattern is found, the result of re.search() method is an object: {type(match)}")

print("\nThe result isn't just a Boolean, it gives more information about the match.")
print("As we found a pattern in our test, let's explore it:")

print(f"\nString searched: {match.string}")
print(f"Regex used: {match.re}")
print(f"Match start position: {match.start()}")
print(f"Match end position: {match.end()}")
print(f"Match by index: {match.group(0)}")
