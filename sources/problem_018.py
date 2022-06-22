#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    result = {}
    for c in s:
        if c not in result.keys():
            result[c] = 0
        result[c] = result[c] + 1
    result = dict(sorted(result.items(), key=lambda item: (-item[1], item[0])))
    counter = 1
    for item in result:
        if (counter <= 3):
            counter += 1
            print(item, result[item])

