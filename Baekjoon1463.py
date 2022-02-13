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

x = int(input())
d=[0]*(x+1)
d[1] = 0
for i in range(2,x+1):
    d[i] = d[i-1]+1
    if i%3 == 0:
        d[i] = min(d[i],d[i//3]+1)
    if i%2 ==0:
        d[i] = min(d[i],d[i//2]+1)
print(d[x])
    


