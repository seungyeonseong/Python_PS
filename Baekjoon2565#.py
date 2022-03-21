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
#우선순위 큐로 A 기준q,B기준 qq로 각각 개수구하고, 그 중 최솟값

# +
from collections import deque
import heapq

n = int(input()) 
q=[]
qq=[]
graph=[[]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    a,b = map(int,input().split())
    heapq.heappush(q,(a,b))
    heapq.heappush(qq,(b,a))

    
#dp=[[0,0] for _ in range(n+1)]
dp=[0,0]
i,val = heapq.heappop(q)
while q:
    i,new = heapq.heappop(q)
    if new<val:
        dp[0] += 1
    else:
        val = new
        
i,val = heapq.heappop(qq)
while qq:
    i,new = heapq.heappop(qq)
    if new <val:
        dp[1] +=1
    else:
        val = new
print(min(dp))
    

# +
#구글링
##도착지점기준:{8,2,9,1,4,6,7,10} 서로 전기줄이 교차하지 않으려면, 
#연속적으로 증가하는 숫자가 필요=LIS

# +
#import sys
#input = sys.stdin.readline

n = int(input())
a=[]
dp=[1]*n

for _ in range(n):
    a.append(list(map(int,input().split())))
    
a.sort(key = lambda x:x[0])

for i in range(n):
    for j in range(i):
        if a[i][1] > a[j][1]:
            dp[i] = max(dp[i],dp[j]+1)
print(n-max(dp))

# +
n = int(input())
li=[0]+list(map(int,input().split()))

#20 10 30 20 30 50 --> 4개
d = [1]*(n+1)

if n>= 2:
    for i in range(2,n+1):
        for j in range(1,i):
            if li[i] > li[j]:
                d[i] = max(d[j]+1,d[i])
        
print(max(d))
# -

d


