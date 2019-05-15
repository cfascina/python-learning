try:
    x = 5
    y = 0
    z = x / y
except ZeroDivisionError:
    print('A ZeroDivisionError occurred.')
finally:
    print("All done.")
