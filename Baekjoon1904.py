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
#메모리초과
# -

n = int(input())
dp=[0]*(n+1)
dp[1] = 1
if n >=2:
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = (dp[i-1]+dp[i-2])%15746
print(dp[n])

dp

# +
#시간초과

# +
n = int(input())

def func(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return func(n-2)+func(n-1)
print(func(n)%15746)

