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
a, b = map(int,input().split())

#최대공약수
n = min(a,b)
while (n > 1):
    if a%n ==0 and b%n == 0:
        break
    else:
        n -= 1
print(n)

#최대공배수
print(n*(a//n)*(b//n))
# -


