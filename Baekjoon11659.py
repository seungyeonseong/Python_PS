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
li = list(map(int,input().split()))
dp=[0]
ans = 0
for i in range(n):
    ans += li[i]
    dp.append(ans)
print(dp)
for _ in range(m):
    x,y = map(int,input().split())
    print(dp[y]-dp[x-1])
    
    
# -



