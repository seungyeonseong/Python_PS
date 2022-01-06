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
word = list(input())
dial = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

total =0

for i in range(len(word)):
    for j in dial:
        if word[i] in j:
            total += dial.index(j)+3

print(total)















# -


