#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 15:40:38 2021

@author: juicy
"""

#r讀取模式
#w寫入模式
#as 當作
#f file

data = []
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip()) 
        #strip:去除空格及換行符號
        
print(len(data))
print(data[67])
    