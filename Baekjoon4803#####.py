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
    if a <b:
        parent[b] = a
    else:
        parent[a] = b
        
case =0        
while True:
    result = True
    case +=1
    n,m = map(int,input().split())
    if n ==0 and m ==0:
        break
    parent=[i for i in range(n+1)]
    li=[]
    for _ in range(m):
        li.append(list(map(int,input().split())))
    for x,y in li:
        if x ==y:
            result = False
            continue
        if find_parent(parent,x) == find_parent(parent,y):
            result = False
        union_parent(parent,x,y)
    res = 0
    for i in range(1,n+1):
        if parent[i]==i:
            res +=1
            
            
    if result:
        if res==1:
            print("Case %d: There is one tree." %case)
        else:
            print("Case %d: A forest of %d trees." %(case,res))

    elif result is False:
        if res ==2:
            print("Case %d: There is one tree." %case)
        elif res >2:
            print("Case %d: A forest of %d trees." %(case,res-1))
        else:
            print("Case %d: No trees." %case)

# -

Case 1: No trees.
Case 3: No trees.
