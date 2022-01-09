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
x = int(input())

#대각선 범위 찾기
#1/2/3/4..
d=1
total=1
while (1):
    if total <x:
        d += 1
        total += d #t=3,d=2,t=3,d=3
    else:
        break
#print(d)
index = total-x
#print(index)

arr=[]
if d%2!=0:
    for i in range(1,d+1):
        arr.append("%d/%d" %(i, d-i+1))
else:
    for i in range(1,d+1):
        arr.append("%d/%d" %(d-i+1,i))
#print(arr)        
print(arr[index])

# -


