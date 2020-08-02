#!/bin/python3

import math
import os
import random
import re
import sys
os.environ['OUTPUT_PATH'] = './QueensAttack2.txt'

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    minE = n - c_q
    minW = c_q - 1
    minN = n - r_q
    minS = r_q - 1
    minNE = min(n - r_q, n - c_q)
    minNW = min(n - r_q, c_q - 1)   
    minSE = min(r_q - 1, n - c_q)
    minSW = min(r_q - 1, c_q - 1)
    for obstacle in obstacles:
        if obstacle[0] == r_q:
            if obstacle[1] > c_q:
                minE = min(minE, obstacle[1] - c_q - 1)
            if obstacle[1] < c_q:
                minW = min(minW, c_q - obstacle[1] - 1)
        elif obstacle[1] == c_q:
            if obstacle[0] > r_q:
                minN = min(minN, obstacle[0] - r_q - 1)
            if obstacle[0] < r_q:
                minS = min(minN, r_q - obstacle[0] - 1)
        else:
            del_r=abs(obstacle[0] - r_q)
            del_c=abs(obstacle[1] - c_q)
            if del_r == del_c:
                if obstacle[0] > r_q and obstacle[1] > c_q:
                    minNE = min(minNE, del_r - 1)
                if obstacle[0] > r_q and obstacle[1] < c_q:
                    minNW = min(minNW, del_r - 1)     
                if obstacle[0] < r_q and obstacle[1] > c_q:
                    minSE = min(minSE, del_r - 1)
                if obstacle[0] < r_q and obstacle[1] < c_q:
                    minSW = min(minSW, del_r - 1)                            
    return minE + minW + minN + minS + minNE + minNW + minSE + minSW 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    obstacles = []

    
    nk = input().split()
    
    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
    '''
    n = 5
    k = 6
    r_q = 4
    c_q = 3
    print(f'Queen   : {r_q}, {c_q}')
    
    obstaclelist = ['5 4', '5 2', '3 4', '2 5', '3 2', '2 1']
    for i in range(k):
        obstacles.append(list(map(int, obstaclelist[i].rstrip().split())))    
    '''

    result = queensAttack2(n, k, r_q, c_q, obstacles)
    print(f'Cells attacked = {result}')
    fptr.write(str(result) + '\n')

    fptr.close()
