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

def dijkstra(start):
    q= []
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
                
for tc in range(int(input())):
    n,d,c = map(int,input().split())
    graph  = [[]*(n+1) for _ in range(n+1)]
    distance = [INF]*(n+1)
    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((a,s))
    total =1
    dijkstra(c)
    total = 0
    min_distance=0
    for i in distance:
        if i != INF:
            total += 1
            if min_distance <i:
                min_distance = i
    print(total, min_distance)
        
        
