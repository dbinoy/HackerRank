#!/bin/python3

import os
import sys
os.environ['OUTPUT_PATH'] = './SummingNSeries.txt'

#
# Complete the summingSeries function below.
#
def summingSeries(n):
    return (n*n) % 1000000007

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = summingSeries(n)

        fptr.write(str(result) + '\n')

    fptr.close()
