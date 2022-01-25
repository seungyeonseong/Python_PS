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
import sys

#정수를 받을때
n = int(sys.stdin.readline())
lists =[0]*10001

for i in range(n):
    lists[int(sys.stdin.readline())] += 1

for i in range(10001):
    if lists[i] != 0:
        for j in range(lists[i]): #해당 숫자만큼
            print(i)
