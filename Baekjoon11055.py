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
li = list(map(int,input().split()))

d=li[0:n]
for i in range(n):
    for j in range(i):
        if li[i] > li[j]:
            d[i] = max(d[j]+li[i],d[i])
print(max(d))
# -

li

d


