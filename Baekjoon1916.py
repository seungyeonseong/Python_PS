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

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance =[INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    
start,end = map(int,input().split())

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
dijkstra(start)
print(distance[end])
# -


