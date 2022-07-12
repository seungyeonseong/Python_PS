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
def bfs():
    q = deque()
    q.append((home[0],home[1]))
    while q:
        x,y = q.popleft()
        if abs(fest[0]-x)+abs(fest[1]-y) <= 1000:
            print("happy")
            return
        for i in range(n):
            if visited[i] is False:
                nx,ny = li[i]
                if abs(nx-x)+abs(ny-y) <= 1000:
                    visited[i] = True
                    q.append((nx,ny))
    print("sad")
    return
            
        
        
t= int(input())
for _ in range(t):
    n = int(input())
    visited=[False]*n
    li=[]
    home = list(map(int,input().split()))
    for _ in range(n):
        x,y = map(int,input().split())
        li.append([x,y])
    fest = list(map(int,input().split()))
    bfs()
    
