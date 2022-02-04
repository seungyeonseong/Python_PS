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
word=[]
for i in range(n):
    word.append(input())

word.sort(key = lambda x:(len(x),x))
res =[]
for i in word:
    if i not in res:
        res.append(i)
        print(i)

