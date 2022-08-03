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

dxr = [1,-1]
dyr = [0,0]
dxc = [0,0]
dyc = [1,-1]

def dfsr(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        for i in range(2):
            nx = x + dxr[i]
            ny = y + dyr[i]
            if 0 <= nx <n and 0 <= ny < m and visited[nx][ny] is False and graph[nx][ny]==graph[x][y]:
                q.append((nx,ny))
                visited[nx][ny] = True                
        
def dfsc(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        for i in range(2):
            nx = x + dxc[i]
            ny = y + dyc[i]
            if 0 <= nx <n and 0 <= ny < m and visited[nx][ny] is False and graph[nx][ny]==graph[x][y]:
                q.append((nx,ny))
                visited[nx][ny] = True     
                
n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
        
visited= [[False]*m for _ in range(n)]       
ans = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] is False and graph[i][j]=="-":
            dfsc(i,j)
            ans += 1
        elif visited[i][j] is False and graph[i][j]=="|":
            dfsr(i,j)
            ans +=1
print(ans)
         
