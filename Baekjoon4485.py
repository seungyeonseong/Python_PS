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

tc =1
while 1:
    
    n = int(input())
    if n==0:
        break
        
    graph=[[]*n for _ in range(n)]
    distance = [[INF]*n for _ in range(n)]
    for i in range(n):
        graph[i]=list(map(int,input().split()))
    x,y = 0,0
    q=[]
    heapq.heappush(q,(graph[x][y],x,y))
    distance[x][y] = graph[x][y]
    while q:
        dist,x,y = heapq.heappop(q)
        if dist > distance[x][y]:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or nx>=n or ny <0 or ny>=n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q,(cost,nx,ny))
    print("Problem %d:" %tc,distance[n-1][n-1])
    tc += 1
    

# +
### distance
# -

graph

 graph=[[]*(n+1) for _ in range(n+1)]

graph

a=123
b =1
print("sol %d" %b,a)


