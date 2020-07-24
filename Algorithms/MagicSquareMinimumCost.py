#!/bin/python3

import math
import os
import random
import re
import sys
os.environ['OUTPUT_PATH'] = './MagicSquareMinimumCost.txt'
# Complete the formingMagicSquare function below.
def computeSums(s):
    n = len(s)
    rowSums = [0] * n
    colSums = [0] * n
    diagSums = [0] * 2
    
    for i in range(n):
        for j in range(n):
            rowSums[i] += s[i][j]
            colSums[j] += s[i][j]
            if i == j:
                diagSums[0] += s[i][j]
            if i+j == n-1:
                diagSums[1] += s[i][j] 

    return rowSums + colSums + diagSums


def formingMagicSquare(s):
    n = [s[i][j] for i in range(3) for j in range(3)]
    p = [
            [8, 1, 6, 3, 5, 7, 4, 9, 2],
            [6, 1, 8, 7, 5, 3, 2, 9, 4],
            [4, 9, 2, 3, 5, 7, 8, 1, 6],
            [2, 9, 4, 7, 5, 3, 6, 1, 8],
            [8, 3, 4, 1, 5, 9, 6, 7, 2],
            [4, 3, 8, 9, 5, 1, 2, 7, 6],
            [6, 7, 2, 1, 5, 9, 8, 3, 4],
            [2, 7, 6, 9, 5, 1, 4, 3, 8]
        ]
    sums = []
    for c in p:
        sums.append(sum([abs(n[i]-c[i]) for i in range(9)]))
    minCost = min(sums)
    return minCost
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
