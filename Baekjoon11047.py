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
n,k = map(int,input().split())
coin=[]
for i in range(n):
    coin.append(int(input()))

cnt = 0
coin.sort(reverse=True)
for i in coin:
    if i <= k:
        num = k//i
        k = k%i
        cnt += num
print(cnt)
