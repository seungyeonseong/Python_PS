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

n,k = map(int,input().split())
li = list(map(int,input().split()))
res = sum(li[0:k])
total = -987654321
for i in range(1,n-k+1):
    total = max(res,total)
    res =res-li[i-1]+li[i+k-1]
total = max(res,total)
print(total)

