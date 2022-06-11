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
from collections import deque
import sys

input = sys.stdin.readline
q = deque()
for _ in range(int(input())):
    x = input().split()
    if x[0] == "push":
        q.append(int(x[1]))
    elif x[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif x[0] == "size":
        print(len(q))
    elif x[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif x[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)


