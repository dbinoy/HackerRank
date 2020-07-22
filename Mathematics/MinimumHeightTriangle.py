#!/bin/python3

import os
import sys
import math

def lowestTriangle(base, area):
    return math.ceil(float(2*area)/base)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        base, area = input().split()

        base, area = [int(base), int(area)]

        height = lowestTriangle(base, area)

        fptr.write(str(height) + '\n')

    fptr.close()
