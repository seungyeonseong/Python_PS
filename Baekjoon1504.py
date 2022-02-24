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
##다익스트라
#삽질1: 양방향인거 확인 안함
#삽질2: v1->v2로 갈 필요x, v2->v1도 가능

# +
import heapq
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


n,e = map(int,input().split())
graph=[[]*(n+1) for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
v1,v2 = map(int,input().split())

#1->v1->v2->n번
arr=[1,v1,v2,n]
arr2=[1,v2,v1,n]
total = 0
total2=0
for i in range(0,len(arr)-1):
    dijkstra(arr[i])
    if distance[arr[i+1]] != INF:
        total += distance[arr[i+1]]
    else:
        total = -1
        break
    distance = [INF]*(n+1)
    
for i in range(0,len(arr2)-1):
    dijkstra(arr2[i])
    if distance[arr2[i+1]] != INF:
        total2 += distance[arr2[i+1]]
    else:
        total2 = -1
        break
    distance = [INF]*(n+1)
total=min(total,total2)
print(total)

# -

4 5
1 2 3
1 3 1
1 4 1
2 3 3
3 4 4
2 3
10

distance

distance = [INF]*(n+1)
dijkstra(1)
distance

# +
##시간초과

# +
INF = int(1e9)

n,e = map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    if graph[a][b] > c:
        graph[a][b] = c
    if graph[b][a] > c:
        graph[b][a] = c
    
v1,v2 = map(int,input().split())

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
            
    
#1->v1->v2->n번
arr=[1,v1,v2,n]
total = 0
for i in range(len(arr)-1):
    if graph[arr[i]][arr[i+1]] != INF:
        total += graph[arr[i]][arr[i+1]]
    else:
        total = -1
        break

print(total)
# -


