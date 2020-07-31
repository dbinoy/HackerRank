#!/bin/python3

import math
import os
import random
import re
import sys
os.environ['OUTPUT_PATH'] = './ClimbingLeaderBoard.txt'
# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    uniuqeScores = sorted(list(set(scores)))
    numScores = len(uniuqeScores)
    ranks = []
    
    rank = 0
    for aliceScore in alice:        
        while(numScores > rank and  aliceScore >= uniuqeScores[rank]):
            rank += 1
        ranks.append(numScores-rank+1)
    print(ranks)
    return ranks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')#!/bin/python3

import math
import os
import random
import re
import sys

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


    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
