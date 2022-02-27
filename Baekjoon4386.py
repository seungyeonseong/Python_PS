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
#크루스칼 알고리즘

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
        
    

v,e = map(int,input().split())
graph = []
parent = [i for i in range(v+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    graph.append((c,a,b))

graph.sort()
total = 0
for edges in graph:
    cost,a,b = edges[0],edges[1],edges[2]
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        total += cost
        
print(total)
        
    
    

    


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
star=[0]
for _ in range(n):
    x,y = map(float,input().split())
    star.append((x,y))    
parent = [i for i in range(n+1)]
graph=[]
for i in range(1,n+1):
    for j in range(i+1,n+1):
        cost = ((star[i][0]-star[j][0])**2+(star[i][1]-star[j][1])**2)**0.5
        graph.append((round(cost,2),i,j))
        
graph.sort()
total = 0
for edge in graph:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        total += cost
        
print(total)
        
        
        
        
    
    
    
# -


