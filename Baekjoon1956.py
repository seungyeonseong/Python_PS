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
INF = int(1e9)

v,e = map(int,input().split())
graph = [[INF]*(v+1) for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    
    
for k in range(1,v+1):
    for a in range(1,v+1):
        for b in range(1,v+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
            
#사이클이 될수 있는 것 찾기
result = INF
for i in range(1,v+1):
    result = min(result,graph[i][i]) #다시 시작점으로 돌아온 값 중 가장 작은 값으로 갱신
    
if result == INF:
    print(-1)
else:
    print(result)
    
    
     

            

