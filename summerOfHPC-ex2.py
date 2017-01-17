import math
import numpy as np

pi_true = np.pi
print(pi_true)

def pi_error(N):

    pi_err = np.abs(pi_true - pi_approx(N))

    #print("The true value of pi = {}, the approxiamtion = {}".format(pi_true, pi_approx(N)))
    #print("Thus, the error is = {}".format(pi_err))

    return pi_err

def pi_approx(N):
    summation = 0
    for i in range(N):
        alpha  = (i - 0.5)/N
        summation = summation + 1 / (1 + alpha**2)
        #print("i = {} and summation = {}".format(i, summation))

    result = (4 / N)*summation
    #print("pi approximation = {}".format(result))

    return result

# first search
guesses = []
guess = 10

while pi_error(guess) > 0.000001:
    guesses = [guess]
    guess = guess * 2
    guesses.append(guess)
    print(guess)

print(guesses.pop())

upper_lim = guess
lower_lim = guesses.pop()
middle = math.floor(upper_lim - lower_lim / 2)

print("Upper - {},\nLower - {},\nMiddle - {}".format(upper_lim, lower_lim, middle))
while True:
    #Is middle point above or below desired answer?
    if pi_error(middle) < 0.000001:
        print("Above")
        upper_lim = middle
        # lower, no change
        diff = math.floor((upper_lim - lower_lim) / 2)
        middle = lower_lim + diff
    else:
        print("Below")
        #upper_lim stays the same
        lower_lim = middle
        diff = math.floor((upper_lim - lower_lim) / 2)
        middle = lower_lim + diff
    print("Upper - {},\nLower - {},\nMiddle - {}".format(upper_lim, lower_lim, middle))
    if (middle == lower_lim or upper_lim):
        break
        # return middle

for input in range(lower_lim, upper_lim):

    if pi_error(input) < 0.000001:
        print("Got 'eeeem at {}".format(input))
        break

