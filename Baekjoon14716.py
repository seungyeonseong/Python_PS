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

m,n = map(int,input().split())
graph=[]
for _ in range(m):
    graph.append(list(map(int,input().split())))

dx = [1,0,-1,0,1,1,-1,-1]
dy = [0,1,0,-1,1,-1,1,-1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <m and 0 <= ny <n and graph[nx][ny]==1:
                q.append((nx,ny))
                graph[nx][ny] = 0
                
num = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] ==1:
            bfs(i,j)
            num += 1
            
print(num)       
    
