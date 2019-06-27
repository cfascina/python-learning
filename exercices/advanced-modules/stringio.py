import io

# StringIO method sets the string as file like object
file = io.StringIO("This is just a normal string.")

# Read the file and print it
print(file.read())

# Reset the cursor and writes a new string
file.seek(0)
file.write("Second line written to the file like object.")

# Reset the cursor, read the file again and print it
file.seek(0)
print(file.read())

# Close the file like object when contents are no longer needed
file.close()
