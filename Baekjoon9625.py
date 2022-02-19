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
n = int(input())
home=[]
for _ in range(n):
    home.append(list(map(int,input().split())))
for i in range(1,n):
    home[i][0] = min(home[i-1][1],home[i-1][2])+home[i][0]
    home[i][1] = min(home[i-1][0],home[i-1][2])+home[i][1]
    home[i][2] = min(home[i-1][0],home[i-1][1])+home[i][2] 
    
print(min(home[n-1]))
# -
k = int(input())
#a 10
#b 01
#ba 1 1
#bab1 2
#babba2 3
#babbabab 35
d=[[0,0] for i in range(k+1)]
d[1][0] = 0
d[1][1] = 1
if k >=2:
    for i in range(2,k+1):
        d[i][0] = d[i-1][1]
        d[i][1] = d[i-1][0]+d[i-1][1]
print(d[k][0],d[k][1])




