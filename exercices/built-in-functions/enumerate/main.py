# enumerate() allows you to keep a count as you iterate through an object.
# It does this by returning a tuple in the form (count, element).

months = ['January', 'February', 'March', 'April', 'May']

print("Function enumerate() results:")
for index, month in enumerate(months):
    print(f"({index}): {month}")

print("\nBreaking at determined condition (index > 2):")
for index, month in enumerate(months):
    if index > 2:
        break
    else:
        print(f"({index}): {month}")

print("\nSetting option 'start' argument to override default value of '0':")
for index, month in enumerate(months, start = 1):
    print(f"({index}): {month}")
