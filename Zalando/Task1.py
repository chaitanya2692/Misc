#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 08:35:32 2020

@author: jarvisonline
"""

def solution(n):
    ans=[]
    for i in range(1,n//2+1):
        ans.append(i)
        ans.append(-i)
    if n % 2 !=0:
        ans.append(0)
    return ans