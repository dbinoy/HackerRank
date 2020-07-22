#!/bin/python3

import os
import sys
os.environ['OUTPUT_PATH'] = './ConnectingTowns.txt'
#
# Complete the connectingTowns function below.
#
def connectingTowns(n, routes):
    r = 1
    for i in range(n-1):
        r *= routes[i]
    return r % 1234567

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        routes = list(map(int, input().rstrip().split()))

        result = connectingTowns(n, routes)
        print(result)
        fptr.write(str(result) + '\n')

    fptr.close()
