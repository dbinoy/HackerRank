#!/bin/python3

import os
import sys
import math
from functools import reduce
os.environ['OUTPUT_PATH'] = './PrimeFactors.txt'
#
# Complete the primeCount function below.
#

def isPrime(x):
    x2 = int(x)
    if abs(x2) < 2:
        return False
    p = True
    for i in range(2,round(math.sqrt(x2))+1,1):
        if x2%i == 0:
            p = False
            break
    return p

def primeCount(n):
    
    f = []
    ctr = 0
    prod = 1    
    for i in range(n+1):
        if isPrime(i):
            prod *= i            
            f.append(i)
            if prod >= n:
                print(f)
                if prod == n:
                    ctr +=1
                break            
            ctr += 1
    return ctr
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)
        fptr.write(str(result) + '\n')

    fptr.close()
