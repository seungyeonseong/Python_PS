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
#맞았지만 시간이 아주아주 느림,,,
#반복문마다 리스트 초기화해서 그런걸로 추정ㅎ

# +
n = int(input())
d= [0]*(n+1)
#li =[i*i for i in range(1,int(n**0.5)+1)]

for i in range(1,n+1):
    s =[]
    li =[k*k for k in range(1,int(i**0.5)+1)]
    for j in li:
        s.append(d[i-j])
    d[i] = min(s)+1
print(d[n])
        
        
        

# +
#아래는 틀린 풀이 2개
#반례)41=25+16=36+4+1
#가장 큰 제곱수로 빼는 거 아님 ㅠ

# +
import sys
input = sys.stdin.readline

n = int(input())
d= [0]*(n+1)
li =[i*i for i in range(1,int(n**0.5)+1)]
d[1] =1
if n>=2:
    d[2] = 2
if n>=3:
    d[3]=3
if n>=4:
    for i in range(4,n+1):
        if i in li:
            d[i] = 1
            target = i
        else:
            d[i] = d[target]+d[i-target]
print(d[n])
# -

n = int(input())
total=0
for i in range(int(n**0.5),0,-1):
    total += n//(i**2)
    n = n%(i**2)
print(total)

# +
###구글링 풀이
# -

n = int(input())
dp = [x for x in range (n+1)]
for i in range(1,n+1):
    for j in range(1,i):
        if j*j > i :
            break
        if dp[i] > dp[i-j*j] + 1 :
            dp[i] = dp[i-j*j] + 1
print(dp[n])
