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
#내풀이
#접근법: 다익스트라, (i번->x번)+(x번->i번)의 최댓값
######distance리스트 다익스트라 수행할 때마다 초기화해줘야하는거 까먹고 삽질함

# +
import heapq

INF = int(1e9)
n,m,x =  map(int,input().split())

graph = [[] for _ in range(n+1)]
distance= [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(x)
res=[0]
for i in range(1,n+1):
    res.append(distance[i])
    

for start in range(1,n+1):
    distance= [INF]*(n+1)    
    dijkstra(start)
    res[start] += distance[x]
print(max(res))
    
