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

t = int(input())
for i in range(t):
    li = list(input())
    cnt = 0
    for i in li:
        if i =="o":
            cnt += 1
    if 15-len(li)+cnt >= 8:
        answer = "YES"
    else:
        answer = "NO"
    print(answer)
    
