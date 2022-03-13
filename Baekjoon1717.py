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
#recursion 런타임에러나서 limit을 10**5로 설정하니 통과
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] =  find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    x,a,b = map(int,input().split())
    if x == 0:
        union_parent(parent,a,b)
    else:
        if find_parent(parent,a) != find_parent(parent,b):
            #print("NO")
            sys.stdout.write("NO\n")
        else:
            #print("YES")
            sys.stdout.write("YES\n")
