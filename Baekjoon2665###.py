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
import heapq

INF = int(1e9)

dx = [1,0,-1,0]
dy = [0,1,0,-1]
 

n = int(input())
graph = [[0]*n for _ in range(n)]
distance = [[0]*n for _ in range(n)]
for i in range(n):
    graph[i] = list(input())
for i in range(n):
    for j in range(n):
        if int(graph[i][j]) ==1:
            graph[i][j] = -1
    
x,y = 0,0    
q= []
heapq.heappush(q,(-1,x,y))
distance[x][y] = -1
while q:
    dist,x,y = heapq.heappop(q)
    if dist > distance[x][y]:
        continue
    for i in range(4):
        nx = x +dx[i]
        ny = y +dy[i]
        if nx <0 or nx >=n or ny<0 or ny >=n:
            continue
        cost = dist +graph[nx][ny]
        if cost < distance[nx][ny]:
            distance[nx][ny] = cost
            heapq.heappush(q,(cost,nx,ny))
print(distance[n-1][n-1])



# +
import heapq

INF = int(1e9)

dx = [1,0,-1,0]
dy = [0,1,0,-1]
 

n = int(input())
graph = [[0]*n for _ in range(n)]
distance = [[0]*n for _ in range(n)]
for i in range(n):
    graph[i] = list(input())
    
x,y = 0,0    
#distance = [[0]*n for _ in range(n)]
q= []
heapq.heappush(q,(-1,1,x,y))
distance[x][y] = 1
while q:
    num,dist,x,y = heapq.heappop(q)
    if dist < distance[x][y]:
        continue
    for i in range(4):
        nx = x +dx[i]
        ny = y +dy[i]
        if nx <0 or nx >=n or ny<0 or ny >=n:
            continue
        cost = dist +int(graph[nx][ny])
        if cost > distance[nx][ny]:
            distance[nx][ny] = cost
            heapq.heappush(q,(-cost,cost,nx,ny))
print(distance[n-1][n-1])

# -

graph


