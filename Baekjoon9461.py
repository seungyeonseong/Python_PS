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
for _ in range(int(input())):
    n = int(input())
    dp=[1]*(n+1)
    if n >=4:
        for i in range(4,n+1):
            dp[i] = dp[i-3]+dp[i-2]
            
    print(dp[n])
        
        
    
