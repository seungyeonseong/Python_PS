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
input = sys.stdin.readline
from collections import deque 

dx = [1,0,-1,0]
dy = [0,1,0,-1]
            
def bfs(x,y):
    global numv
    global numo
    q = deque()
    q.append((x,y))
    if graph[x][y] == "v":
        numv += 1
    elif graph[x][y] =="o":
        numo += 1
    graph[x][y] = "x"
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or nx >= r or ny <0 or ny >=c:
                continue
            if graph[nx][ny]=="#" or graph[nx][ny] =="x":
                continue
            #if graph[nx][ny] =="#":
             #   break
            if graph[nx][ny] =="v":
                numv += 1
                graph[nx][ny] ="x"
                q.append((nx,ny))
            elif graph[nx][ny] =="o":
                numo += 1
                graph[nx][ny] ="x"
                q.append((nx,ny))
            else:
                graph[nx][ny] ="x"
                q.append((nx,ny))

    if numv == 0 and numo ==0:
        return
    if numv >= numo:
        numo = 0
        return
    else:
        numv = 0
        return

r,c = map(int,input().split())
graph=[]
for _ in range(r):
    graph.append(list(input()))

ans = [0,0]
for i in range(r):
    for j in range(c):
        if graph[i][j] != "#" and graph[i][j]!="x" :
            numv, numo = 0,0
            bfs(i,j)
           # print(numv,numo)
            ans[0] += numv
            ans[1] += numo
  
        
            
print(ans[1],ans[0])
            
  
