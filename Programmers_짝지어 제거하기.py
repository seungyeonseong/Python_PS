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

def solution(s):
    q = deque()
    for i in s:
        if len(q)>=2 and i==q[-1]:
            q.pop()
            continue
        else:
            q.append(i)
    if len(q)>=2 and q[-1]==q[-2]:
        q.pop()
        q.pop()
    if q:
        return 0
    else:
        return 1
    
s = 'baabaa'

print(solution(s))
