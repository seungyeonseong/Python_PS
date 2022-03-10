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

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    q = deque()
    graph[x][y] = 1
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx>=n or ny < 0 or ny >=m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1 
                q.append((nx,ny))
            if graph[nx][ny] == 1:
                continue
        return graph[n-1][m-1]

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,list(input()))))

total = 987654321
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] == 0
            total = min(bfs(0,0),total)
        graph[i][j] == 1
            
print(total)
    
    
# -

graph

d =[]
d.append(list(map(int,list(input()))))

bfs(0,0)


