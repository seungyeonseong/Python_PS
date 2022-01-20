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
n, m = map(int,input().split())

card = list(map(int,input().split()))
li=[]
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            li.append(card[i]+card[j]+card[k])
li.sort()
li.reverse()
if m in li:
    print(m)
else:
    for i in li:
        if i <m:
            print(i)
            break
# -


198+1+9+8

# +
n = int(input())
li=[0 for _ in range(1,n+1)]
#각 자리의 합 구하기
for i in range(1,1000001):
    t = i
    s=0
    s += i
    while i > 9 :
        s += i%10
        i = i//10
    s += i
    li[t] = s
#print(li)    
    
if n in li:
    print(li.index(n))
else:
    print(0)

# +
#216 -> 198
n = int(input())

for i in range(1,n+1):
    n_sum = i + sum(map(int,str(i)))
    if n == n_sum:
        print(i)
        break
    elif i == n:
        print()
