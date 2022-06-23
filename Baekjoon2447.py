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

n = int(input())
def func(n):
    if n ==1:
        return ["*"]
    x = func(n//3)
    li = []
    for star in x:
        li.append(star*3)
    for star in x:
        li.append(star+" "*(n//3)+star)
    for star in x:
        li.append(star*3)
    return li
func(n)
for i in func(n):
    print(i)


