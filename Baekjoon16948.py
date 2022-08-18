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
# +
from collections import deque

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

def bfs(x,y):
    q = deque()
    graph[x][y] = 1
    q.append((x,y))
    while q:
        x,y  = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <n and 0 <= ny <n and graph[nx][ny]==0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

n = int(input())
r1,c1,r2,c2 = map(int,input().split())

graph = [[0]*n for _ in range(n)]
bfs(r1,c1)
if graph[r2][c2]==0:
    print(-1)
else:
    print(graph[r2][c2]-1)

# -


def dfs(x,y):
    if 0 >x or x>=n or 0>y or y>=n:
        return
    graph[x][y]= True
    if 0<= x <n and 0<= y <n and graph[]:
        dfs(x-2,y-1)
        dfs(x-2,y+1)
        dfs(x,y-2)
        dfs(x,y+2)
        dfs(x+2,y-1)
        dfs(x+2,y+1)
        return

