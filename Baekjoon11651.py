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
li=[]
for i in range(n):
    x,y = map(int,input().split())
    li.append((x,y))
li.sort(key=lambda x:(x[1],x[0]))
for i in li:
    print(i[0],i[1])
# -


