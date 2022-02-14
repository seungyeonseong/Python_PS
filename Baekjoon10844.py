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
##점화식으로 접근 --> 실패
#마지막 숫자에 따라 다음항에 영향을 준다

# +
n = int(input())
d = [[0]*10 for _ in range(n+1)]
for i in range(1,10):
    d[1][i] = 1
    
for i in range(2,n+1):
    for j in range(10):
        if j==0:
            d[i][j] = d[i-1][j+1]
        elif j ==9:
            d[i][j] = d[i-1][j-1]
        else:
            d[i][j] = d[i-1][j-1] +d[i-1][j+1]
            
print(sum(d[n])%1000000000)

