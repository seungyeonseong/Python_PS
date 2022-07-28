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
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
for _ in range(m):
    graph.append(list(input()))
    
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    num = 1
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <m and 0<=ny <n and visited[nx][ny]==False and graph[nx][ny] == graph[x][y]:
                q.append((nx,ny))
                visited[nx][ny] = True
                num += 1
    return num
    


visited = [[False]*n for _ in range(m)]
nw,nb = 0,0
for i in range(m):
    for j in range(n):
        if visited[i][j] is False:
            if graph[i][j] =="W":
                num = bfs(i,j)
                nw += num**2
            else:
                num = bfs(i,j)
                nb += num **2
print(nw,nb)
