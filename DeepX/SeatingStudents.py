#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:01:20 2020

@author: jarvisonline
"""

def SeatingStudents(arr): 
    length = arr[0]
    occupied = arr[1:]
    ways = 0
    for i in range(1, length):
        if not (i in occupied):
            if i % 2 != 0:
                if not (i + 1 in occupied):
                    ways += 1
                if i <= length - 2 and not (i + 2 in occupied):
                    ways += 1
            else:
                if i <= length - 2 and not (i + 2 in occupied):
                    ways += 1

    # code goes here 
    return ways

# keep this function call here  
print (SeatingStudents(raw_input()))  


if __name__ == "__main__":
    