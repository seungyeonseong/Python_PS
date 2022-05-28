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
#처음엔 벽3개를 한번에 설치하는 방법을 생각했다->실패

#가져가야할 부분
#모든 벽을 세우는 백트래킹부분+bfs탐색마다 copy로 임시 2차원 생성하는 부분

# +

#n,m = 7,7
#graph=[[2,0,0,0,1,1,0],[0,0,1,0,1,2,0],[0,1,1,0,1,0,0],[0,1,0,0,0,0,0],[0,0,0,0,0,1,1],[0,1,0,0,0,0,0],[0,1,0,0,0,0,0]]

from collections import deque
import copy
import sys
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

res = 0
def bfs():
    global res
    graph2 = copy.deepcopy(graph)
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph2[i][j]==2:
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph2[nx][ny] == 0:
                graph2[nx][ny] = 2
                q.append((nx,ny))
    ans = 0
    for i in range(n):
        for j in range(m):
            if graph2[i][j] ==0:
                ans += 1
    res = max(ans,res)
                
def wall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j] = 1
                wall(cnt+1)
                graph[i][j] = 0
n,m = map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
    
                
wall(0)
print(res)
