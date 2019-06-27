import pdb

x = 1
y = 2
z = [3, 4]

print("x + y = " + str(x + y))

print("\nForced Error.")
print("At (Pdb) console you can check what's wrong. To quit, press 'q' and hit Enter.")
pdb.set_trace()
print("y + z = " + str(y + z))
