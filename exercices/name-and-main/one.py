def func():
    print('Function func() in one.py.')

print('Top level print() in one.py.')

if __name__ == '__main__':
    print('The file one.py is being run directly.')
else:
    print('The file one.py has been imported.')
