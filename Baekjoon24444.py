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
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited[start]= 1
    n = 2
    while q:
        x = q.popleft()
        for i in sorted(graph[x]):
            if visited[i] == 0:
                q.append(i)
                visited[i] = n
                n += 1
        



n,m,r = map(int,input().split())
visited=[0]*(n+1)
graph =[[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(r)
for i in range(1,n+1):
    print(visited[i])
