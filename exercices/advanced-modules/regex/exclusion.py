import re

string = 'This is a string, but it has punctuation. Can we remove it?'
match = re.findall('[^,.? ]+', string)

print(f"String: {string}")
print("\nPattern: '[^,.? ]+'")
print("Result: " + str(match))
