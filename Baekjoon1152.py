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

text = list(input())
cnt = 0
#print(text)
#print(len(text))
for i in range(0,len(text)):
    if i!=0 and (i!= len(text)-1) and text[i] == " ":
        cnt += 1
if len(text)==1 and text[0] == " ":#공백입력된 경우
    print(0)
else:
    print(cnt+1)



