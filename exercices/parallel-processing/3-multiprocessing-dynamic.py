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

iterations = int(input(f"Type how many iterations do you want: "))
processes = int(input(f"Type how many processes do you want: "))

with Pool(processes) as pool:
    print(f"\n{iterations:,} iterations with {processes} process")
    print("-" * (len(f"\n{iterations:,} iterations with {processes} process") - 1))
    print("\nTotal time: " + str(timeit.timeit(lambda: print(f"Estimated Pi: {sum(pool.map(find_pi, [iterations // processes] * processes)) / processes:0.7f}"), number = 10)))
