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
#내풀이_그래프 다익스트라 알고리즘 사용

# +
import heapq

def dijkstra(start,distance,graph):
    q =[]

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
    return distance
    

def solution(n, edge):
    answer = 0
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    distance = [INF]*(n+1)
    for i in edge:
        x,y  = i
        graph[x].append((y,1))
        graph[y].append((x,1))
        
        
    d = dijkstra(1,distance,graph)
    answer = d.count(max(d[1:]))
    print(distance)
    return answer

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n,vertex))

