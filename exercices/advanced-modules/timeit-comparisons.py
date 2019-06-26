import timeit

print("We will create the string '0-1-2-3-...-99' w/ 3 different methods:")
print("1. Using a for loop.")
print("2. Using list comprehension.")
print("3. Using a map function.")

print("\nThen, using the timeit library we will see wich method is faster.")
print("Let's create the strings and see the results.")

result_1 = timeit.timeit('"-".join(str(n) for n in range(100))', number = 10000)
result_2 = timeit.timeit('"-".join([str(n) for n in range(100)])', number = 10000)
result_3 = timeit.timeit('"-".join(map(str, range(100)))', number = 10000)

print("\nUsing a for loop: " + str(result_1))
print("Using list comprehension: " + str(result_2))
print("Using a map function: " + str(result_3))

print("\nThrough the timeit library, it was possible to see that the faster method to create the string we wanted was using a map function.")
