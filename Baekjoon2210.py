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
sys.setrecursionlimit(10**9)

graph=[]
for _ in range(5):
    graph.append(list(map(int,input().split())))
    

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(x,y,number):
    number += str(graph[x][y])
    
    if len(number)==6:
        if number not in d:
            d.add(number)
        return

    for i in range(4):
        nx = x +dx[i]
        ny = y +dy[i]
        if 0 <= nx <5 and 0 <=ny<5:
            dfs(nx,ny,number)
    
    
d = set()
for i in range(5):
    for j in range(5):
        dfs(i,j,"")

print(len(d))
