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

import heapq
n = int(input())
q = []
for _ in range(n):
    x = int(input())
    if x >0:
        heapq.heappush(q,-x)
    else:
        if q:
            res = heapq.heappop(q)
            print(-1*res)
        else:
            print(0)
        


