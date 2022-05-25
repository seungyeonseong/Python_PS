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
#변수 중복돼서 한참한참 삽질함,,

# +
from collections import deque
import sys
input =sys.stdin.readline
 
n = int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(graph, x, y, visited, h):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False and h < graph[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True

l=[]
hh = -1
for li in graph:
    for x in li:
        hh = max(hh, x)

for h in range(0,hh+1):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if visited[x][y] == False and graph[x][y]>h:
                bfs(graph, x, y, visited, h)
                cnt += 1
    l.append(cnt)
    
print(max(l))

