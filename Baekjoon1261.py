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
###내풀이
#접근법: 이코테 기출 중 화성 어쩌고랑 유사함.최단경로 찾기 위해 배열을 노드로 본다!
#입력받을때 실수해서 value error와장창 뜨고 삽질함 ㅠ

# +
import heapq
import sys
input  = sys.stdin.readline
INF = int(1e9)

m, n = map(int, input().split())
graph = []
distance = [[INF] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(input()))


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y = 0, 0
q = []
heapq.heappush(q, (int(graph[x][y]), x, y))
distance[x][y] = int(graph[x][y])

while q:
    dist, x, y = heapq.heappop(q)
    if dist > distance[x][y]:
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        cost = dist + int(graph[nx][ny])
        if cost < distance[nx][ny]:
            distance[nx][ny] = cost
            heapq.heappush(q, (cost, nx, ny))

print(distance[n - 1][m - 1])

