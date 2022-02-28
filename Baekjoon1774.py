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
        
n,m = map(int,input().split())
graph =[]
parent= [i for i in range(n+1)]
total= 0
for _ in range(n):
    x,y = map(int,input().split())
    graph.append((x,y))
    
for _ in range(m):
    a,b = map(int,input().split())
    union_parent(parent,a,b)
   
    
array = []

for i in range(n):
    for j in range(i+1,n):
        cost = ((graph[i][0]-graph[j][0])**2+(graph[i][1]-graph[j][1])**2)**0.5
        array.append((cost,i+1,j+1))
        
array.sort()
for i in array:
    cost,a,b = i
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        total += cost
print(format(round(total,2),".2f"))
        
