#!/bin/python3

import math
import os
import random
import re
import sys
os.environ['OUTPUT_PATH'] = './PickingNumbers.txt'
#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    print(a)
    n = len(a)
    arrPos = [0]*n
    arrNeg = [0]*n
    for i in range(n):
        seed = a[i]
        for j in range(n):
            if seed-a[j] >= 0 and seed-a[j] <= 1:
                arrPos[i] += 1
            if seed-a[j] <= 0 and seed-a[j] >= 1:
                arrNeg[i] += 1                
    return max(max(arrPos), max(arrNeg))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
