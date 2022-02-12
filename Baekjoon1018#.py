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
n,m = map(int,input().split())
chess=[]
for i in range(n):
    chess.append(list(input()))
    

res=[]
for i in range(n):
    for j in range(m):
        idx1,idx2 =0, 0
        if i+7 >= n or j+7 >= m:
            continue
        for p in range(i,i+8):
            for q in range(j,j+8):
                if (p+q)%2 == 0:
                    if chess[p][q] != "W": idx1 += 1
                    if chess[p][q] != "B": idx2 += 1
                else:
                    if chess[p][q] != "B": idx1 += 1
                    if chess[p][q] != "W": idx2 += 1
        res.append(idx1)
        res.append(idx2)
print(min(res))
        
# -


