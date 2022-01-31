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

input = sys.stdin.readline
sy


#순열 사이클 개수 구하기

def dfs(graph,v,visited):
    visited[v] = True
    for i in graph[v]:
        if visited[i] is False:
            dfs(graph,i,visited)





#입력
t = int(input())
for i in range(t):
    n = int(input())
    graph = [[i] for i in range(n+1)]
    array = list(map(int,input().split()))
    for j in range(len(array)):
        graph[j+1].append(array[j])
    
    visited = [False] *(n+1)
    cnt = 0
    for j in range(1,n+1):
        if visited[j] is False:
            dfs(graph,j,visited)
            cnt += 1
            
    print(cnt)
   

# -


