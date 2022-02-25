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
#접근법: 1,0으로 이루어져있는 미로를 최댓값으로 가되 0으로 지나가는 개수 구하기
#1,0의 자리를 반대로 바꿔서 최단경로 구하기로 풀었따,,,
#최대힙 구현하려다가 실패함 ㅠ,,,나중에 해보기

# +
import heapq

INF = int(1e9)

dx = [1,0,-1,0]
dy = [0,1,0,-1]
 

n = int(input())
graph = []
distance = [[INF]*n for _ in range(n)]
for i in range(n):
    graph.append(list(input()))
    
for i in range(n):
    for j in range(n):
        if graph[i][j] =='1':
            graph[i][j] = 0
        else:
            graph[i][j] = 1
x,y = 0,0    
q= []
heapq.heappush(q,(0,x,y))
distance[x][y] = 0
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

