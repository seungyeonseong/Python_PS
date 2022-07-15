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
    global total
    q= deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or nx >=n or ny <0 or ny>=m:
                continue
            if graph[nx][ny] != 0 and visited[nx][ny] is False:
                q.append((nx,ny))
                total += 1
                visited[nx][ny] = True
    return total
        

n,m = map(int,input().split())
graph=[]
visited=[[False]*m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,input().split())))

li=[]
for i in range(n):
    for j in range(m):
        total = 1
        if graph[i][j]==1 and visited[i][j]is False:
            bfs(i,j)
            li.append(total)
print(len(li))
if len(li)==0:
    print(0)
else:
    print(max(li))
