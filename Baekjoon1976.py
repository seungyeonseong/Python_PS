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
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())
graph=[]
parent = [i for i in range(n+1)]

for i in range(n):
    graph.append(list(map(int,input().split())))
    
travel_route=list(map(int,input().split()))

for i in range(n):
    for j in range(i+1,n):
        if graph[i][j] ==1 and find_parent(parent,i+1)!=find_parent(parent,j+1):
            union_parent(parent,i+1,j+1)
res = "YES"           
for x in range(m-1):
    if find_parent(parent,travel_route[x]) != find_parent(parent,travel_route[x+1]):
        res = "NO"
        break
print(res)
            


    
