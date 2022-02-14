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
d = [[1]*10 for _ in range(n+1)]

if n >=2:
    for i in range(2,n+1):
        for j in range(1,10):
            d[i][j] = d[i-1][j] +d[i][j-1]
print(sum(d[n])%10007)
    

# -


