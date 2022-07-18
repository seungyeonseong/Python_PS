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

def dijkstra():
    q = []
    heapq.heappush(q,(0,x))
    distance[x] = 0
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
        
n,m,k,x = map(int,input().split())

distance = [INF]*(n+1)
graph= [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))

dijkstra()
li=[]
for i in range(1,n+1):
    if distance[i]==k:
        li.append(i)
if li:
    for i in li:
        print(i)
else:
    print(-1)
    


# +
#플로이드워셜 풀이는 메모리초과남 

# +
INF = int(1e9)

n,m,k,x = map(int,input().split())

graph=[[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    
for i in range(1,n+1):
    graph[i][i]=0


for t in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][t]+graph[t][j],graph[i][j])
li=[]
for r in range(1,n+1):
    if graph[x][r]==k:
        li.append(r)
if li:
    for tmp in li:
        print(tmp)
else:
    print(-1)

        
