
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    value = 0
    v_len = len(arr)
    
    for i in range(v_len):

        
        value += arr[i][i]
        value -= arr[i][v_len-i-1]
    
    return abs(value)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
