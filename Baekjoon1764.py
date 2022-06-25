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
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
a = dict()
for _ in range(n+m):
    name = input().rstrip()
    if name in a:
        a[name] += 1
    else:
        a[name] = 1
    
res= 0
li=[]
for i in a:
    if a[i]==2:
        res += 1
        li.append(i)
print(res)
for i in sorted(li):
    print(i)
        

    
    
