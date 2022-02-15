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
li = input().split("-")
ans = 0
for i in range(len(li)):
    res = 0
    if i==0:
        arr = li[i].split("+")
        for j in arr:
            ans += int(j)
    else:
        arr = li[i].split("+")
        for j in arr:
            ans -= int(j)
        
print(ans)   
# -


