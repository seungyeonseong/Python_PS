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
t = int(input())

for _ in range(t):
    k = int(input()) #k층 n호
    n = int(input())
    total = []
    
    for i in range(0,k):
            li=[]
            for j in range(1,n+1):
                li.append(j)
            total.append(li)
    #print(total)
    #print("\n\n")
    
    for i in range(1,k):
        for j in range(1,n):
            summ = 1
            for m in range(1,j+1):
                summ += total[i-1][m]
            total[i][j] = summ
   # print(total)
    
    print(sum(total[k-1]))
# -

#141020..
#13610
#1234..

