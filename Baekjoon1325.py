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
#BFS풀이

# +
from collections import deque 

def bfs(start):
    q = deque([start])
    visited = [False]*(n+1)
    visited[start] = True
    cnt = 1
    while q:
        x = q.popleft()
        for node in graph[x]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
                cnt += 1
    return cnt
    
n,m = map(int,input().split())
graph= [[] for _ in range(n+1)]
li =[]
for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)
mmax=-1   
for i in range(1,n+1):
    num = bfs(i)
    if mmax<num:
        mmax =num
    li.append(num)

for n,i in enumerate(li):
    if i==mmax:
        print(n+1,end=" ")
    

# +
#맞왜틀한 DFS풀이,,답은나오는데 메모리초과남(구글링에서 해결법못찾음)

# +
def dfs(start):
    global num
    visited.add(start)
    for i in graph[start]:
        if i not in visited:
            num += 1
            dfs(i)
    
n,m = map(int,input().split())
graph= [[] for _ in range(n+1)]
li =[]
for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)
    
for i in range(1,n+1):
    if len(graph[i])==0:
        continue
    num = 0
    visited =set()
    dfs(i)
    li.append(num)

mmax=max(li)
for n,i in enumerate(li):
    if i==mmax:
        print(n+1,end=" ")
    
# -


