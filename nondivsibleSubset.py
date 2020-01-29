#!/bin/python

import math
import os
import random
import re
import sys

# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    print("aye")
    k=k
    remArr=[]
    arr=S
    for i in range(len(arr)):
        rem=arr[i]%k
        print(rem)
        remArr.append(rem)

    remArr=sorted(remArr)
    count=0
    sum=0
    while sum < k:
        sum=sum+remArr[count]
        count+=1
    print(sum)
    return count+1



S=[1 ,7 ,2 ,4]
print(nonDivisibleSubset(3,S))
