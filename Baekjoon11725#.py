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

###구글링


# +
import sys
input =sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n+1)]
parent=[0]*(n+1)

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    
def dfs(start,tree,parent): #연결된 노드들로부터 parent[i]의 부모가 없으면 부모 설정 후 dfs
    for i in tree[start]:
        if parent[i] == 0:
            parent[i] = start
            dfs(i,tree,parent)
            
dfs(1,tree,parent)
for i in range(2,n+1):
    print(parent[i])

# +
#아래 엉터리긴한데 사실 왜틀렸는지모름

# +
n = int(input())
for _ in range(n-1):
    #graph=[[] for i in range(n+1)]
    parent=[i for i in range(n+1)]
    a,b = map(int,input().split())
    if a==1:
        parent[b] = 1
    elif b==1:
        parent[a] = 1
    else:
        if parent[a] != a:
            parent[b] =a
        elif parent[b] !=b:
            parent[a] = b
                
for i in range(2,n+1):
    print(parent[i])
