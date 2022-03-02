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
parent = [i for i in range(n+1)]

arr=[]
for  _ in range(m):
    a,b,c = map(int,input().split())
    arr.append((c,a,b))
arr.sort()
total = 0
for i in arr:
    cost,a,b = i
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        total += cost
print(total)
    
    
