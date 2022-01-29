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
#입력

e, s, m = map(int,input().split())

#1 2 3
#28 28 28
# 1 28 

year = 1

while True:
    fst = year % 15
    if fst ==0:
        fst = 15
    sec = year % 28
    if sec ==0:
        sec = 28
    thd = year % 19
    if thd == 0:
        thd = 19
    if fst != e or sec != s or thd != m:
        year += 1
    else:
        break
    

print(year)

# -


