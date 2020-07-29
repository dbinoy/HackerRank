
#!/bin/python3

import math
import os
import random
import re
import sys
os.environ['OUTPUT_PATH'] = './RepeatedString.txt'

# Complete the repeatedString function below.
def repeatedString(s, n):
    l = len(s)
    
    fo = n//l
    pol = n%l

    fc = s.count('a')
    poc = s[:pol].count('a')

    return fc*fo + poc

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
