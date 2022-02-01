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
####최단거리문제는 BFS로 풀 것#######

# +
#import sys
#input = sys.stdin.readline
from collections import deque



#동->남->서->북
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
     #방문 처리
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a +dx[i]
            ny = b + dy[i]
            if nx <0 or nx >= n or ny <0 or ny >=m:
                continue
            if li[nx][ny] == 0:
                continue
            if li[nx][ny] ==1:
                li[nx][ny] = li[a][b] +1
                queue.append((nx,ny))
        
    return li[n-1][m-1]
    
    
    
#visited = [[0]*m for i in range(n)] 
    
#입력
n, m  = map(int,input().split())
li =[]
for i in range(n):
    li.append(list(map(int,input())))
    
print(bfs(0,0))

