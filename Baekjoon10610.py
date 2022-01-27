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
n = list(input())
n = list(map(int,n))


if 0 not in n or sum(n)%3 != 0:
    print(-1)
else:
    n.sort(reverse=True)
    for i in n:
        print(i,end='')
    

# -


