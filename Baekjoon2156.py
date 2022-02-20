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
##구글링
#현재시점 기준 경우의 수 나누면
#-->1.안마시는 경우_2.2번연속 마시는경우 3.처음으로 마시는 경우
# -

n = int(input())
li = [0]
for _ in range(n):
    li.append(int(input()))
d = [0]*(n+1)
d[1] = li[1]
if n >=2:
    d[2] = d[1] + li[2]
if n>=3:
    for i in range(3,n+1):
        d[i] = max(d[i-3]+li[i-1]+li[i],d[i-2]+li[i],d[i-1])
print(d[n])

# +
#개틀린 내풀이
#점화식으로 풀려고했는데 원리 파악x

# +
n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))
    
if n ==1:
    total=[li[0]]
elif n ==2:
    total = [li[0]+li[1]]
elif n==3:
    total = [li[0]+li[1],li[1]+li[2]]
        
elif n >=4:
    total = [li[0]+li[1]+li[3],li[1]+li[2],li[0]+li[2]+li[3]]
if n>=5:
    for i in range(5,n):
        if i%3==1:
            total[0] += li[i]
            total[1] += li[i]
        elif i%3==2:
            total[1] += li[i]
            total[2] += li[i]
        else:
            total[0] += li[i]
            total[2] += li[i]
print(max(total))        
        

