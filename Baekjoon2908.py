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
a,b=map(str,input().split())

#거꾸로읽기
a = list(a)
a.reverse()
a = int(a[0])*100+int(a[1])*10 +int(a[2])
b = list(b)
b.reverse()
b = int(b[0])*100+int(b[1])*10 +int(b[2])
if a >b:
    print(a)
else:
    print(b)
# -


