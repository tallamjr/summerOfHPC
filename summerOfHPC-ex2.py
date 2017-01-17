# EXERCISE 2
## IMPORTS
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

pi_true = np.pi
print(pi_true)

def pi_approx(N):
    summation = 0
    for i in range(N):
        alpha  = (i - 0.5)/N
        summation = summation + 1 / (1 + alpha**2)

    result = (4 / N)*summation

    return result

def pi_error(N):

    pi_err = np.abs(pi_true - pi_approx(N))

    return pi_err

upper_bound = 5000000

def iterative_search(upper_bound):

    for input in range(500, upper_bound):
        if input % 5000 == 0:
            print("Iteration at {}".format(input))
        if pi_error(input) < 0.000001:
            print("Got 'eeeem at {}".format(input))
            break


start = time.time()

# Careful, a large upper will take a long time.
iterative_search(upper_bound)

end = time.time()
print("Took {} s".format((end - start)))

