import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pi_true = np.pi
print(pi_true)

def pi_approx(N):
    summation = 0
    for i in range(N):
        alpha  = (i - 0.5)/N
        summation = summation + 1 / (1 + alpha**2)
        #print("i = {} and summation = {}".format(i, summation))

    result = (4 / N)*summation
    #print("pi approximation = {}".format(result))

    return result

pi_approx(5)

def pi_error(N):

    pi_err = np.abs(pi_true - pi_approx(N))

    #print("The true value of pi = {}, the approxiamtion = {}".format(pi_true, pi_approx(N)))
    #print("Thus, the error is = {}".format(pi_err))

    return pi_err

pi_error(5)

N = [1,2,10,50,100,500]

outputs_list = []
for input in N:
    outputs = pi_approx(input)
    outputs_list.append(pi_error(input))
    print("{} inputs = PI approximation of {}.".format(input, outputs))
    print(pi_error(input))
