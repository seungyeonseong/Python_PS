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
###구글링
#접근법: 틀림 ㅠ,1->3->5 경로 갱신될 때 추가해주는 방법을 구현x

#여러가지 풀이가 있었지만 노드 간의 최단거리가 갱신될 때 부모노드를 갱신해줘서
# 도착점과 시작점 사이의 길을 알 수 있게 만드는 풀이가 이해가 쉬웠다,,

# +
import heapq
INF = int(1e9)
def dijkstra(start):
    q = []

    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        #arr.append(now)
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                parent[i[0]] = now

n = int(input())
m = int(input())

graph= [[]*(n+1) for _ in range(n+1)]
distance = [INF]*(n+1)
parent=[i for i in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    
start,end = map(int,input().split())
arr=[]
dijkstra(start)

print(distance[end])
#print(distance)
arr.append(end)
i = end
while i != start:
    i = parent[i]
    arr.append(i)

print(len(arr))
arr.reverse()
for i in arr:
    print(i,end=" ")
