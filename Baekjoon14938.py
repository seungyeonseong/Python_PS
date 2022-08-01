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
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,r = map(int,input().split())
graph=[[] for _ in range(n+1)]
item = [0]
item += list(map(int,input().split()))
for _ in range(r):
    a,b,l = map(int,input().split())
    graph[a].append((b,l))
    graph[b].append((a,l))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
num = 0
for i in range(1,n+1):
    distance = [INF]*(n+1)
    dijkstra(i)
    ans = 0
    for j in range(1,n+1):
        if distance[j] <= m:
            ans += item[j]
    num = max(num,ans)
print(num)
