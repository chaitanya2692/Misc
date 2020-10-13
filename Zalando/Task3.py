#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 08:42:37 2020

@author: jarvisonline
"""

import datetime
from time import strptime

def parse_by_line(f1):
    f1=S.splitlines()
    all_lines = []
    for x in f1:
        one_line = x.split()                
        all_lines.append(one_line)
    
    return all_lines

def check_size(all_files):
    filtered_files = []
    for file in all_files:
        if int(file[0]) >= 240*2**10:
            filtered_files.append(file)
    # filtered_files = [all_files[i] for i in size_indices]
    return filtered_files

def format_date(file):
# date in yyyy/mm/dd format 
    strptime('Feb','%b').tm_mon
    date = datetime.datetime(int(file[3]), strptime(file[2],'%b').tm_mon, int(file[1]))
    return date


def check_date(files):
    filtered_files = [] 
    given_date = datetime.datetime(1990, 1, 31)
    for file in files:
        if format_date(file) > given_date:
            filtered_files.append(file)
    # filtered_files = [files[i] for i in date_indices]       
    return filtered_files

def solution(S):
    all_files = parse_by_line(S)
    all_files = list(filter(None, all_files))
    size_filter = check_size(all_files)
    date_filter = check_date(size_filter)
    return len(date_filter)
   
        
if __name__ == "__main__":
    S = """
     779091968 23 Sep 2009 system.zip
 284164096 14 Aug 2013 to-do-list.xml
 714080256 19 Jun 2013 blockbuster.mpeg
       329 12 Dec 2010 notes.html
 444596224 17 Jan 1950 delete-this.zip
       641 24 May 1987 setup.png
    245760 16 Jul 2005 archive.zip
 839909376 31 Jan 1990 library.dll
    """
    print(solution(S))
