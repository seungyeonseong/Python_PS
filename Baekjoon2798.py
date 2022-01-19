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

def fibo(n):
    if n == 0:
        return 0
    if n==1:
        return 1
    return fibo(n-1)+fibo(n-2)

print(fibo(n))
# +
n, m = map(int,input().split())

card = list(map(int,input().split()))
li=[]
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            li.append(card[i]+card[j]+card[k])
li.sort()
if m in li:
    print(m)
else:
    
# -



