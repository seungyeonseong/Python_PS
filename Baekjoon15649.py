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
import itertools 

n,m =map(int,input().split())
li = [i for i in range(1,n+1)]
per = list(itertools.permutations(li,m))

for i in range(len(per)):
    for j in per[i]:
        print(j,end=" ")
    print("")

