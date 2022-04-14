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
#백준에서 풀었던듯?
# -

def solution(triangle):
    for i in range(len(triangle)-1,-1,-1):
        for j in range(len(triangle[i])-1):
            triangle [i-1][j] = max(triangle[i][j],triangle[i][j+1]) + triangle[i-1][j]
    return triangle[0][0]
