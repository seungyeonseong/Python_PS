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

li = list(map(int,input().split()))

#소수찾기
def func(m):#m이 소수인지 아닌지 판별하는 함수 작성
    if m == 1:
        return False
    if m == 2:
        return True
    for i in range(2,int(m**0.5)+1):
        if m % i == 0:
            return False
    return True
 
          
count = 0        
for i in range(n):
    if func(li[i]) == True:
        count += 1
print(count)
# -


