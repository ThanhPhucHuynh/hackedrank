
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):

    numPositive:int = 0
    numNegative:int = 0
    numZero:int     = 0
    numLengthArr:int=len(arr)

    for i in arr:
        if   i  > 0: numPositive+=1
        elif i  < 0: numNegative+=1
        elif i == 0: numZero    +=1
    print(numPositive/numLengthArr)
    print(numNegative/numLengthArr)
    print(numZero    /numLengthArr)

   
if __name__ == '__main__':
    # n = int(input())

    # arr = list(map(int, input().rstrip().split()))
    
    arr = [-4, 3, -9, 0, 4, 1]

    plusMinus(arr)
