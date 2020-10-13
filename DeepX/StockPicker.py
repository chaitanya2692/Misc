#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:27:19 2020

@author: jarvisonline
"""

def StockPicker(arr):
  greatest = 0
  for i in range(len(arr)):
      for x in range(len(arr[i:])):
          if(arr[x]-arr[i] > greatest):
              greatest = arr[x]-arr[i]
  return greatest

print(StockPicker([44, 30, 24, 32, 35, 30, 40, 38, 15]))