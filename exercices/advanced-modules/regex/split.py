import re

split_term = "@"
email = "cfascina@gmail.com"
print(f"Searching for '{split_term}' at '{email}'")

match = re.split(split_term, email)
print("\nThe re.split() method returns a list.")
print("The term to split is removed and the between values are converted to strings into the list:")
print(match)
