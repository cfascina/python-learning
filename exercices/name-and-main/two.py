import one

print('Top level print() in two.py.')

one.func()

if __name__ == '__main__':
    print('The file two.py is being run directly.')
else:
    print('The file two.py has been imported.')
