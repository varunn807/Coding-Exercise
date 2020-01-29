#!/bin/python

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):



    leftD=0
    rightD=0
    n = len(arr)

    arr = arr

    for i in range(n):

        row=i
        col=n-(i+1)

        rightD=rightD+arr[row][col]
        leftD=leftD+arr[i][i]


    result=leftD-rightD




arr=[[11,2,4],[4,5,6],[10,8,-12]]
#print(arr[0][3])
print(diagonalDifference(arr))
