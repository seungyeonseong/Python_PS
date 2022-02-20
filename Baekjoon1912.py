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
li =[0]+ list(map(int,input().split()))

d=[min(li)]*(n+1)

for i in range(1,n+1):
    d[i] = max(li[i]+d[i-1],li[i])
print(max(d))
# -


