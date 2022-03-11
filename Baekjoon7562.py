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
##내풀이->dfs 재귀로 풀려했는데 오류파티

# +


dx = [2,1,2,1,-2,-1,-2,-1]
dy = [-1,2,1,-2,1,2,-1,-2]

def func(a,b,num):
    if a == x and b==y:
        return num
    for k in range(8):
        nx = a +dx[k]
        ny = b +dy[k]
        if nx<0 or nx>=i or ny<0 or ny>=i:
            continue
        func(nx,ny,num+1)

tc = int(input())

for _ in range(tc):
    i = int(input())
    a,b = map(int,input().split())
    x,y = map(int,input().split())
    print(func(a,b,0))


# +
###구글링-->bfs로 풀이

# +
from collections import deque

dx = [2,1,2,1,-2,-1,-2,-1]
dy = [-1,2,1,-2,1,2,-1,-2]

def func(a,b):
    q = deque()
    q.append((a,b))
    graph[a][b] = 0
    while q:
        a,b = q.popleft()
        if a == x and b==y:
            return graph[x][y]
        for k in range(8):
            nx = a +dx[k]
            ny = b +dy[k]
            if nx<0 or nx>=i or ny<0 or ny>=i:
                continue
            if graph[nx][ny] ==0:
                graph[nx][ny] = graph[a][b] +1 
                q.append((nx,ny))

tc = int(input())

for _ in range(tc):
    i = int(input())
    a,b = map(int,input().split())
    x,y = map(int,input().split())
    graph=[[0]*(i+1) for _ in range(i+1)]
    print(func(a,b))
    

