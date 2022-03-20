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
#내풀이: 맨 아랫줄부터 j,j+1보다 큰 값으로 누적해서 갱신,,첫줄에 최댓값나오도록

# +
n = int(input())
li= [0]

for _ in range(n):
    li.append(list(map(int,input().split())))
    
for i in range(n,1,-1):
    for j in range(i-1):
        li[i-1][j] += max(li[i][j],li[i][j+1])
print(li[1][0])
