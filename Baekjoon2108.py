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
# 최빈값 구하는 과정에서 li.count() 쓰니까 시간초과 뜸,,,

# +
import sys
input = sys.stdin.readline

n = int(input())
li=[]
for i in range(n):
    li.append(int(input()))

#산술평균
print(round(sum(li)/n))
    
#중앙값
li.sort()
print(li[n//2])

#최빈값
num=[]
for i in set(li):
    ans = 0
    for j in li:
        if i == j:
            ans += 1
    num.append((i,ans))
               
num.sort(key=lambda x:(-x[1],x[0]))

if len(num)==1:
    print(num[0][0])
else:
    if num[0][1] ==num[1][1]:
        print(num[1][0])
    else:
        print(num[0][0])


        
#범위
print(li[-1]-li[0])
