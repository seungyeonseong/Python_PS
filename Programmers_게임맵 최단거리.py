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
#전형적인 BFS문제

# +
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(maps):
    q = deque()
    q.append((0,0))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if nx <0 or nx >=len(maps) or ny <0 or ny>=len(maps[0]):
                continue
            if maps[nx][ny]==0:
                continue
            if maps[nx][ny] ==1:
                maps[nx][ny] = maps[x][y] +1
                q.append((nx,ny))
    return maps




def solution(maps):
    bfs(maps)
    answer =maps[len(maps)-1][len(maps[0])-1]
    if answer==1:
        return -1
    else:
        return answer
