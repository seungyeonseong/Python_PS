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
#"(",")"삽입 위치

# +
import sys

input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))
res = ""


def sol(x, y, n):
    global res

    tmp = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != tmp:
                res += "("
                sol(x, y, n // 2)
                sol(x, y + n // 2, n // 2)
                sol(x + n // 2, y, n // 2)
                sol(x + n // 2, y + n // 2, n // 2)
                res += ")"
                return
    if tmp == "0":
        res += "0"
    else:
        res += "1"


sol(0, 0, n)

print(res)
