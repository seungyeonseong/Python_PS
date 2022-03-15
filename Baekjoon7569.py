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
##내풀이
#접근법: 3차원 리스트 + bfs
#3차원이라 그런가 겁나겁나 헷갈림,,,

# +
from collections import deque
import sys
input = sys.stdin.readline

dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dz = [0, 0, 1, 0, 0, -1]


def bfs():
    while q:
        i, j, k = q.popleft()
        for x in range(6):
            nx = i + dx[x]
            ny = j + dy[x]
            nz = k + dz[x]
            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue
            if graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = graph[i][j][k] + 1
                q.append((nx, ny, nz))
            if graph[nx][ny][nz] == -1:
                continue


m, n, h = map(int, input().split())
# graph = [[[] for row in range(n)] for depth in range(h)]
graph = [[[] for _ in range(n)] for _ in range(h)]
for i in range(h):
    for j in range(n):
        graph[i][j] = list(map(int, input().split()))

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i, j, k))

bfs()
Tomato = True
day = 1
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                Tomato = False
                break
            day = max(day,graph[i][j][k])

if Tomato is True:
    print(day-1)
else:
    print(-1)

#print(graph)

# +
#3차원 리스트 구현하는 법
# -

li = [[[0 for col in range(5)]for row in range(3)]for depth in range(1)]
li
