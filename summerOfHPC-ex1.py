## IMPORTS
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

pi_true = np.pi
print("The true value of PI is {}".format(pi_true))

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

for input in range(1999900, 2001000):
                   #1747627
    #outputs = pi_approx(input)

    if pi_error(input) < 0.000001:
        print("Got 'eeeem at {}".format(input))
        break
    #else:
        #print("Where they at doh?")
    #outputs_list.append(pi_error(input))
    #print("{} inputs = PI approximation of {}.".format(input, outputs))
    #print(pi_error(input))

## EXERCISE 3

def find_min_interval(guess, lower_lim, upper_lim):

    # find mid-range of interval
    mid = math.floor((upper_lim - lower_lim) / 2)
    new_guess = upper_lim - mid

    tol = upper_lim - new_guess
    if tol < 5000:
        print("Answer = {}, with tolerance of less than 5000".format(new_guess))
        return new_guess

    find_min(new_guess, upper_lim)


guess = 10

def find_min(guess, upper_lim=100000000):
    print("Guessing {}".format(guess))
    if pi_error(guess) < 0.000001:
            print("Got 'eeeem at {}".format(guess))
            # The true min will be equal to or at least less that the above discovered result
            # Therefore, we shall look in the interval using the above result as an upper limit
            print("Now looking for true min in closet interval range...")
            # maybe better to search backward

            #new_upper_lim = guess
            #lower_lim = math.floor(guess / 2)
            #mid = math.floor((new_upper_lim - lower_lim) / 2)
            #new_guess = new_upper_lim - mid

            lower_lim = math.floor(upper_lim / 2)
            mid = math.floor((upper_lim - lower_lim) / 2)
            new_guess = upper_lim - mid
            print("New guess 1 = {}".format(new_guess))
            print("New upperlim 1 = {}".format(upper_lim))

            #find_min_interval(guess, lower_lim, new_upper_lim)
            # new guess is the middle

            #new_guess = lower_lim + math.floor((new_upper_lim / 4))
            #print("trying new guess of {}".format(new_guess))

            tol = upper_lim - new_guess
            if tol < 5000:
                print("Answer = {}, with tolerance of less than 5000".format(new_guess))
                return new_guess

            #tol = new_upper_lim - new_guess
            #if tol < 50000:
            #    return new_guess
            find_min(new_guess, upper_lim)
    else:
        if guess*2 > upper_lim:
            print("It's toooo high!!")

            #new_upper_lim = guess
            lower_lim = math.floor(upper_lim / 2)
            mid = math.floor((upper_lim - lower_lim) / 2)
            new_guess = upper_lim - mid
            print("New guess 2 = {}".format(new_guess))
            print("New upperlim 2 = {}".format(upper_lim))

            find_min(new_guess, upper_lim)

            #new_upper_lim = guess
            #lower_lim = math.floor(guess / 2)
            #find_min_interval(guess, lower_lim, new_upper_lim)

            #lower_lim = math.floor(guess / 2)
            #addition = math.floor((upper_lim - lower_lim)/2)
            #guess = guess + addition
            #find_min(guess, upper_lim)
            #return "Fammm"
        else:
            guess = guess * 2
            find_min(guess)

find_min(guess)

