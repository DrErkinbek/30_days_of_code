#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        return res
print(factorial(4))