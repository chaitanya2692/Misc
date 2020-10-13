#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 08:02:30 2020

@author: jarvisonline
"""

def solution(A, B):
   n = len(A)
   if (n == 0): 
       return 0
   
   presumsA = 0
   presumsB = 0

   for i in range(n):
       presumsA += A[i]
       presumsB += B[i]
   
   if (presumsA != presumsB): 
       return 0
   halfSum = presumsA / 2
   presumsA = 0
   presumsB = 0
   result = 0
   for i in range(n-1) :
       presumsA += A[i];
       presumsB += B[i];
       if (presumsA == presumsB & presumsA == halfSum):
           result = result + 1
   return result

if __name__ == "__main__":
    print(solution([2, -2, -3, 3], [0, 0, 4, -4]))
    