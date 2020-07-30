#!/bin/python3

import math
import os
import random
import re
import sys
os.environ['OUTPUT_PATH'] = './JumpingOnTheClouds.txt'

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n = 0
    i = 0
    while True:
        if i+2 < len(c) and c[i+2] == 0:
            i += 2
        else:
            i += 1
        n += 1
        if i == len(c)-1:
            break
    return n

    '''
    var n = 0;
    for (var i = 0; i < c.length - 1;) {
        i += (c[i+2] ? 1 : 2);
        n++;
    }
    return n;    
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
