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
n = int(input())
time = list(map(int,input().split()))
wt = 0

time.sort()
for i in range(len(time)):
    for j in range(0,i+1):
        wt += time[j]
print(wt)
