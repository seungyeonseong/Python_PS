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
#못품 ㅠ 구글링
#접근법: 각 목적지까지 최단경로로 이동할 때 
#g와 h을 잇는 최단거리를 지나가는지 확인하도록->지나가면 목적지출력

#문제점:다익스트라 알고리즘에서 지나온 경로의 노드를 출력하는 방법을 구현x

#-->다익스트라 알고리즘을 활용해서 최단경로로 비교!꼭 노드 출력할 필요X 

# +
import heapq

INF= int(1e9)

def dijkstra(start):
    q = []
    distance=[INF]*(n+1)
    
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            continue
    #g->h로 간 경로 확인할 수 있도록
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance
                
for tc in range(int(input())):
    n,m,t = map(int,input().split())
 
    s,g,h = map(int,input().split())
    
    
    graph=[[]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    
        
    destination=[]
    for _ in range(t):
        destination.append(int(input()))
        
    s_dijk = dijkstra(s)
    g_dijk = dijkstra(g)
    h_dijk = dijkstra(h)
    res=[]
    for des in destination:
        if s_dijk[g]+g_dijk[h]+h_dijk[des] == s_dijk[des] or s_dijk[h] +h_dijk[g]+g_dijk[des] == s_dijk[des]:
            res.append(des)
    res.sort()
    for i in res:
        print(i,end=" ")
        
# -


