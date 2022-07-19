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
#DP풀이

# +
import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int,input().split()))

dp=[n+1]*n
dp[0] = 0
for i in range(n):
    for j in range(1,li[i]+1):
        if i+j >= n:
            break
            
        dp[i+j] = min(dp[i+j],dp[i]+1)
print(dp[n-1] if dp[n-1]!= n+1 else -1)

# +
#BFS풀이

# +
from collections import deque

n = int(input())
li = list(map(int,input().split()))
visited = [0]*n

q = deque([(0,li[0])])   #현재위치, 점프가능거리

while q:
    pos,jump = q.popleft()
    for i in range(1,jump+1):
        if pos+i >= n or visited[pos+i]:
            continue
        visited[pos+i] = visited[pos] +1
        q.append((pos+i,li[pos+i]))
print(visited[-1] if visited[-1] else -1)
