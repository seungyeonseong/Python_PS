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
from collections import deque


#입력

n = int(input())
m = int(input())

visited = [False]*(n+1)

graph = [[i] for i in range(n+1)]
for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

queue = deque()
queue.append(1) #1,2
visited[1] = True
cnt =0


while queue:
    x = queue.popleft()
    for i in graph[x]:
        if visited[i] == False:
            queue.append(i)
            visited[i] = True
            cnt += 1
            
        
print(cnt)
        
