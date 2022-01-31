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
#dfs

def dfs(x,y):
    if x <0 or x>= h or y <0 or y>=w:
        return False
    if li[x][y] == 1:
        li[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x-1,y+1)
        dfs(x+1,y+1)
        dfs(x-1,y-1)
        dfs(x+1,y-1)
        return True
    return False

#입력

while True:

    w,h  = map(int,input().split())
    if w == 0 and h == 0:
        break
    li=[]
    for i in range(h):
        li.append(list(map(int,input().split())))

    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i,j) == True:
                result += 1
    print(result)

# -


