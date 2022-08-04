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
input =sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
visited = [["-"]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x,y,c = map(int,input().split())
    graph[x][y] = c
    graph[y][x] = c
    visited[x][y] = y
    visited[y][x] = x

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j] = 0

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if graph[a][b] > graph[a][k]+graph[k][b]:
                graph[a][b] = graph[a][k]+graph[k][b]
                visited[a][b] = visited[a][k]                
for i in range(1,n+1):
    for j in range(1,n+1):
        print(visited[i][j],end=" ")
    print()
