# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
###1번 풀이: 마지막 계단부터 출발

# +
n = int(input())
li=[0]
for _ in range(n):
    li.append(int(input()))
    
d=[0]*(n+1)    
d[n] = li[n]
if n>=2:
    d[n-1] = d[n]+li[n-1]
if n>=3:
    d[n-2] = d[n]+li[n-2]
    for i in range(n-3,0,-1):
            d[i] = max(d[i+3]+li[i+1]+li[i],d[i+2]+li[i])
print(max(d))

# +
###2번 풀이:계단 리스트를 reverse한 풀이-> 틀림

# +
n = int(input())
li=[]
for _ in range(n):
    li.append(int(input()))
li.append(0)
li.reverse()
    
d=[0]*(n+1)
d[1] = li[1]
if n>=2:
    d[2] = d[1]+li[1]
if n>=3:
    for i in range(3,n+1):
        d[i] = max(d[i-3]+li[i-1]+li[i],d[i-2]+li[i])
print(max(d))

