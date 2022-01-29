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
from itertools import permutations

n = int(input())
li = list(map(int,input().split()))

#순열
per = list(permutations(li,n))
#print(per)

result = 0
for i in range(len(per)):
    ans = 0
    for j in range(n-1):
        ans += abs(per[i][j]-per[i][j+1])
    result = max(ans,result)
print(result)
# -


