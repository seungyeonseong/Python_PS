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
#내풀이->메모리 초과로 틀림
##모든 행성마다 cost 계산해서 배열에 추가했더니 메모리 초과남 ㅠ

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
star = []
parent = [i for i in range(n+1)]

for _ in range(n):
    x,y,z = map(int,input().split())
    star.append((x,y,z))
arr = []
for i in range(n):
    for j in range(i+1,n):
        cost = min(abs(star[i][0]-star[j][0]),abs(star[i][1]-star[j][1]),abs(star[i][2]-star[j][2]))
        arr.append((cost,i+1,j+1))
arr.sort()
total = 0
for i in arr:
    cost,a,b = i
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        total += cost
print(total)


# +
#구글링
#모든 edge를 구하려고하면 안됌,,,행성별로 x,y,z 별 최단 거리를 리스트에 추가

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
star = []
parent = [i for i in range(n+1)]

for i in range(n):
    x,y,z = map(int,input().split())
    star.append((x,y,z,i+1))
arr = []

for i in range(3):
    star.sort(key = lambda x:x[i])
    for j in range(n-1):
        arr.append((abs(star[j][i]-star[j+1][i]),star[j][3],star[j+1][3]))
        
arr.sort()
total = 0

for i in arr:
    cost,a,b = i
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        total += cost
print(total)
