from random import random
from multiprocessing import Pool
import timeit

def find_pi(num):
    inside = 0

    for i in range(0, num):
        x = random()
        y = random()

        if(x * x + y * y) ** 0.5 <= 1: # If 'i' falls inside the circle.
            inside += 1

    return(4 * inside / num)

# The original code would be:

# total = 0
# for count in range(0, 2):
#     for pi_estimation in pool.map(find_pi, [iterations // processes] * processes):
#         total += pi_estimation
#         print(f"{pi_estimation:0.7f}")

# But we'll use a lambda expression w/ timeit() to measure our code performance.

iterations = 10 ** 7

# Results w/ 1 process:
processes = 1
pool = Pool(processes)

print(f"{iterations:,} iterations with {processes} process")
print("-" * 36)
print("\nTotal time: " + str(timeit.timeit(lambda: print(f"Estimated Pi: {sum(pool.map(find_pi, [iterations // processes] * processes)) / processes:0.7f}"), number = 10)))

pool.close()
pool.join()

# Results w/ 5 processes:
processes = 5
pool = Pool(processes)

print(f"\n{iterations:,} iterations with {processes} processes")
print("-" * 38)
print("\nTotal time: " + str(timeit.timeit(lambda: print(f"Estimated Pi: {sum(pool.map(find_pi, [iterations // processes] * processes)) / processes:0.7f}"), number = 10)))

pool.close()
pool.join()
