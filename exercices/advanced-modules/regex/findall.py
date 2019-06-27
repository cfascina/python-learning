import re

match = re.findall('test', 'The test one failed, the test 2 was successful.')

print("You can use the re.findall() method to find all instances of a pattern in a string.")
print("\nString: 'The test one failed, the test 2 was successful.'")
print("Pattern: 'test'")
print("Result: " + str(match))
