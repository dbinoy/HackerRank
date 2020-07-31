#!/bin/python3

import math
import os
import random
import re
import sys
os.environ['OUTPUT_PATH'] = './EqualizeTheArray.txt'

# Complete the equalizeArray function below.
def equalizeArray(arr):
    modes ={}
    for i,num in enumerate(arr):
        if num in modes:
            modes[num] += 1
        else:
            modes[num] = 1
    print(modes)
    maxMode = max(modes.values())
    return len(arr) - maxMode

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
