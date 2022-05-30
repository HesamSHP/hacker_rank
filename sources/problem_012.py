#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    result = ""
    words = s.split(' ')
    for word in words:
        result += word.capitalize() + " "
    return result

hello   world  lol

if (__name__ == '__main__'):
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    print(result)
    # fptr.write(result + '\n')
    # fptr.close()
    # print(result)
