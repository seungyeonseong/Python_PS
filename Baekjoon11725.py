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
#구글링 =>DFS이용한 풀이

# +
import sys
input =sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())

tree = [[] for _ in range(n+1)]
parent =  [0 for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    
def dfs(start,tree,parent):
    for i in tree[start]:
        if parent[i]  == 0:
            parent[i] = start
            dfs(i,tree,parent)
dfs(1,tree,parent)
for i in range(2,n+1):
    print(parent[i])

# +
### 내풀이 => 순서 못정하면 큐에 넣기 =>답은 맞지만 시간초과남

# +
from collections import deque
        
n = int(input())
li = [False]*(n+1)
li[1] = True
parent = [i for i in range(n+1)]
q = deque()
for _ in range(n-1):
    x,y = map(int,input().split())
    if li[x] is True:
        parent[y] = x
        li[y] = True
    elif li[y] is True:
        parent[x] = y
        li[x] = True
    else:
        q.append((x,y))
while q:
    x,y = q.popleft()
    if li[x] is True:
        parent[y] = x
        li[y] = True
    elif li[y] is True:
        parent[x] = y
        li[x] = True
    else:
        q.append((x,y))
        
            
for i in range(2,n+1):
    print(parent[i])

