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
d=[[0]*2 for _ in range(n+1)]

d[1][1] = 1

if n >=2:
    d[2][0] = 1
    for i in range(3,n+1):
        for j in range(2):
            if j ==0:
                d[i][j] = d[i-1][1]+d[i-1][0]
            else:
                d[i][j]  = d[i-1][0]
            
print(sum(d[n]))
