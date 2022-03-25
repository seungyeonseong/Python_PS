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
###벨만-포드 알고리즘(Python_algorithm 깃허브에 정리해둠)

# +
import sys
input = sys.stdin.readline

INF =  int(1e9)

n,m = map(int,input().split())
distance=[INF] *(n+1)
edges=[]
for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

def bf(start):
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            nxt = edges[j][1]
            cost = edges[j][2]
            if distance[cur] != INF and distance[nxt] > distance[cur] + cost:
                distance[nxt]  = distance[cur] +cost
                if i ==n-1:
                    return True
    return False

negative_cycle = bf(1)
if negative_cycle:
    print("-1")
else:
    for i in range(2, n+1):
        if distance[i] == INF:
            print("-1")
        else:
            print(distance[i])

# +
#플로이드 워셜,다익스트라->음수사이클 해결 x

# +
INF = int(1e9)

n,m = map(int,input().split())
city =[[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    city[a][b] =c
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            city[i][j] = 0
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            city[i][j] = min(city[i][j],city[i][k]+city[k][j])
            
temp = True
for i in range(1,n+1):
    if city[i][i] !=0:
        temp = False
        break
    
if temp:
    for i in range(2,n+1):
        if city[1][i] == 1000000000:
            print(-1)
        else:
            print(city[1][i])
else:
    print(-1)




 
    
