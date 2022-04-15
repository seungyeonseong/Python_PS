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
#내풀이
#플루이드워셜-> BFS -->크루스칼,,,삽질 ㅠ

# +
import heapq

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

def solution(n,costs):
    answer = 0
    visited= [1]*n
    parent = [i for i in range(n)]
    q = []
    for i in costs:
        heapq.heappush(q,(i[2],i[0],i[1]))

    while q:
        c,x,y = heapq.heappop(q)
        #만약 연결되있으면 패스함
        if find_parent(parent,x) == find_parent(parent,y):
            continue
        answer += c
        union_parent(parent,x,y)

    return answer
