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

#합을 구하는 함수
def func(a,p):
    li = list(str(a))
    ans = 0
    for i in range(len(li)):
        ans += int(li[i])**p
    return ans
    

a, p = map(int,input().split())
array = [a]
x = func(a,p)
while True:
    if x in array:
        break
    else:
        array.append(x)
        x = func(x,p)
        
#print(array)  
print(array.index(x))

# -


