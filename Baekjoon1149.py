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


