import random

def random_numbers(lower, higher, numbers_qty):
    for number in range(numbers_qty):
        yield 'Random number: ' + str(random.randint(lower, higher))

print('Function random_numbers() results:')
for number in random_numbers(1, 10, 12):
    print(number)
