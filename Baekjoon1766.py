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
import heapq

input= sys.stdin.readline
    
def topology_sort():
    q =[]
    res = []
    
    for i in range(1,n+1):
        if indegree[i] == 0:
            heapq.heappush(q,i)
    while q:        
        num = heapq.heappop(q)
        res.append(num)
        for i in graph[num]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q,i)
    return res

n,m = map(int,input().split())
graph=[[] for _ in range(n+1)]
indegree=[0]*(n+1)


for _ in range(m):
    a,b = map(int,input().split())    #a번문제는 b번보다 먼저 풀 것
    
    graph[a].append(b)
    indegree[b] += 1


for i in topology_sort():
    print(i,end=" ")

                
