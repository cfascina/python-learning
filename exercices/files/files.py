import os

test_file = "test_file.txt"

if(os.path.isfile(test_file) == True):
    os.remove(test_file)
    print("File deleted. Run again to create the file.")
else:
    test_file = open(test_file, "w+")

    print("1. Writing the first line:")
    test_file.write("First line.")
    test_file.seek(0)
    print(test_file.read())

    print("\n2. Writing the second line:")
    test_file.write("\nSecond line.")
    test_file.seek(0)
    print(test_file.read())

    print("\n3. Using readlines() method:")
    test_file.seek(0)
    print(test_file.readlines())

    test_file.seek(0)
    print("\n4. Iterating through file lines:")
    for line in test_file:
        print(line)

    print("\n5. File closed.")
    test_file.close()
