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
#visited만들었을때는 평생 돌아감,,,
#자꾸 빠트려서 런타임에러 삽질함,,

# +
import sys
from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
m,n,k = map(int,input().split())
li = []
graph = [[0] * n for _ in range(m)]

for _ in range(k):
    li.append(list(map(int,input().split())))
for tmp in li:
    x1, y1, x2, y2 = tmp
    for x in range(m-y2,m-y1):
        for y in range(x1, x2):
            if graph[x][y] == 0:
                graph[x][y] = 1
cnt = 0
res = []
for a in range(m):
    for b in range(n):
        if graph[a][b] == 0:
            cnt = 0
            q = deque()
            q.append((a, b))
            graph[a][b] =1
            while q:
                x, y= q.popleft()
                cnt += 1
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx < m and 0<=ny < n and graph[nx][ny] == 0:
                        q.append((nx, ny))
                        graph[nx][ny] = 1
            res.append(cnt)
print(len(res))
for i in sorted(res):
    print(i,end=" ")


# -


