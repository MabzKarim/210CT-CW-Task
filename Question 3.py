##Pseudocode for Highest Perfect Square:
"""This is the pseudocode for the highest perfect square, it will return
   the highest perfect square for the number the user has chosen"""
    
## HIGHEST_PERF_SQUARE(p)
##  temp <- int sqrt(p)
##  hps <- temp ^ 2
##  return hps

import math

def HIGHEST_PERF_SQUARE(r):
    """ This function would find the highest perfect square for any given number """
    temp = int(math.sqrt(r))
    # the sqrt of the given number is rounded down(truncated)
    hps = temp**2
    # the rounded down number is squared to find the highest perfect square
    return hps

