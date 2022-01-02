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

#33이 39의 생성자
li = list(range(1,10000,1))
for i in range(10000):
    val = 0
    val += i #887
    j = i
    while (j >= 10): #일의 자리가 될때까지
        val += j % 10   #일의자리 7
        j = j//10  #i = 88
    val += j 
    if val in li:
        li.remove(val)
for k in li:
    print(k)


