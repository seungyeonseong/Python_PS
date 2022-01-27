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
n,m = map(int,input().split())

if n==1:
    print(1)
elif n ==2:
    if m>=7:
        print(4)
    else:
        print((m+1)//2)
else:
    if m <=4:
        print(m)
    elif m == 5:
        print(4)
    else:
        print(m-2)
