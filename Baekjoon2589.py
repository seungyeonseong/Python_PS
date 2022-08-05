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

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    visited = [[0]*m for _ in range(n)] 
    q = deque()
    q.append((x,y))
    visited[x][y]= 1
    num = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]=="L"and visited[nx][ny]==0:
                visited[nx][ny] = visited[x][y]+1
                q.append((nx,ny))
                num = max(num,visited[nx][ny])
    return num-1
     
n,m = map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(input()))
cnt = 0    
for i in range(n):
    for j in range(m):
        if graph[i][j] =="L":
            cnt = max(cnt,bfs(i,j))
    
print(cnt)
