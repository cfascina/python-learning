def sting_iterable(name):
    name_iterable = iter(name)

    for letter in name_iterable:
        yield 'Letter: ' + letter

name = "Caio Fascina"
print('Function sting_iterable() results:')
for letter in sting_iterable(name):
    print(letter)
