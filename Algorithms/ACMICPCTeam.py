#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
os.environ['OUTPUT_PATH'] = './ACMICPCTeam.txt'

# Complete the acmTeam function below.
def acmTeam(topic):
    u = 0
    c = 0
    teams = list(combinations(topic, 2))
    for team in teams:
        k = bin(int(team[0], 2) | int(team[1], 2)).count("1")
        if k > u:
            u = k
            c = 1
        elif k == u:
            c += 1
    print(u, c)
    return u, c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    topic = []
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)
    '''

    n = 4
    m = 5
    topic_item = ['10101', '11100', '11010', '00101']
    for i in range(n):
        topic.append(topic_item[i])    
    '''

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
