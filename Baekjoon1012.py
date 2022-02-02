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
input = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(x,y):#방문 처리
    if x < 0 or x >= n or y <0 or y >=m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False





#입력
t = int(input())
for _ in range(t):
    m, n, k  = map(int,input().split())
    
    graph = [[0]*m for i in range(n)]
    result = 0
    
    for _ in range(k):
        x,y = map(int,input().split())
        graph[y][x] = 1
        
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                result +=1 
    print(result)
# -


