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
count = 0
length = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip()) 
        #strip:去除空格及換行符號
        length = length + len(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
        

print('檔案讀取完畢，總共有：', len(data),'筆data')
print('留言平均長度：', length / len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print(len(new))