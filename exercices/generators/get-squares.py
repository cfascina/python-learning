def get_squares(higher):
    for number in range(higher):
        yield 'Square of ' + str(number) + ': ' + str(number**2)

print('Function get_squares() results:')
for number in get_squares(10):
    print(number)
