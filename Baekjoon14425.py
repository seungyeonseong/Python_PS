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
n,m = map(int,input().split())
s = set()
for _ in range(n):
    s.add(input())
ans = 0
for _ in range(m):
    word = input()
    if word in s:
        ans += 1
print(ans)
    
    
# -


