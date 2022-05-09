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

def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    graph=[[] for _ in range(N+1)]
    distance  = [INF]*(N+1)
    for i in road:
        a,b,c = i
        graph[a].append((b,c))
        graph[b].append((a,c))
    q = []
    heapq.heappush(q,(0,1))
    distance[1] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]]= cost
                heapq.heappush(q,(cost,i[0]))
    for i in range(1,N+1):
        if distance[i] <=K:
            answer +=1

    return answer
