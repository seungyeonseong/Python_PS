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
import sys

input = sys.stdin.readline

n,l,r = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
    
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def check(x,y):
    global summ
    union = [(x,y)]
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx >=n or ny<0 or ny >=n:
                continue
            if visited[nx][ny] is True:
                continue
            if l <= abs(graph[x][y]-graph[nx][ny]) <= r:
                q.append((nx,ny))
                summ += graph[nx][ny]
                union.append([nx,ny])
                visited[nx][ny] = True
    
        
    return union

result = 0
while True:
    flag = 0
    visited=[[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] is False:
                summ = graph[i][j]
                union = check(i,j)
                if len(union) > 1:
                    for x,y in union:
                        graph[x][y] = summ//len(union)
                    flag  = 1
        
    if flag == 0:
        break
    result += 1        
            
print(result)
