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
d=[0]*1001

d[1] =1
d[2] = 3

if n >=3:
    for i in range(3,n+1):
        d[i] = (2*d[i-2]+d[i-1])%10007
    
print(d[n])
# -



