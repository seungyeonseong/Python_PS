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
#문제잘못이해해서2트만에 통과,,

# +
def check(graph,N):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == "#":
                cnt += 1
    n  = int(cnt**0.5)
    for i in range(0,N-n+1):
        for j in range(0,N-n+1):
            if graph[i][j] == ".":
                continue
            else:
                res = 0
                for q in range(j,j+n):
                    for k in range(i,i+n):
                        if graph[k][q] !="#":
                            return False
                        else:
                            res += 1
                if res == cnt:
                    return True
                

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    graph=[]
    for i in range(N):
        graph.append(list(input()))
    if check(graph,N):
        print("#%d yes" %test_case)
    else:
        print("#%d no" %test_case)
