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
import sys
#######파이썬은 재귀 횟수 1000회 이상일 때 오류 발생#########
#####sys.setrecursionlimit(10000) 입력해서 제한 풀어줘야함###

sys.setrecursionlimit(10000)

#dfs
def dfs(graph,v,visited):
    visited[v] = True #방문처리
    for i in graph[v]:
        if visited[i] is False:
            dfs(graph,i,visited)
    
n,m = map(int,sys.stdin.readline().split())
#인접 리스트 생성
graph = [[] for i in range(n+1)]
for i in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
    
#인접 리스트 정렬
for i in range(n+1):
    graph[i].sort()
    
visited = [False]*(n+1)    

#그래프
cnt = 0
for i in range(1, n+1):
    if visited[i] is False:
        dfs(graph,i,visited)
        cnt +=1
print(cnt)
# -


