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
def dfs(start):
    for i in li[start]:
        if visited[i] ==0:
            visited[i] = visited[start]+1
            dfs(i)
    
n = int(input())
a,b = map(int,input().split())
m =int(input())
li = [[] for _ in range(n+1)]
visited=[0]*(n+1)
for _ in range(m):
    x,y = map(int,input().split()) #x부모 y자식
    li[y].append(x)
    li[x].append(y)
    
dfs(a)
print(visited[b] if visited[b]>0 else -1)

    
    
    
# -


