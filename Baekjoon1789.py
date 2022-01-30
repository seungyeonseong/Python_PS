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
#수정제출한 코드

# +
n = int(input())
cnt = 0

for num in range(1,n+1):
    n -= num
    cnt += 1
    if n <= 0:
        break
if n == 0:
    print(cnt)
else:
    print(cnt-1)

# +
#n = 1,2,3,4,,,
#i = 1,1,2,2,2,3,3,3,3...
#이런 형태로 증가하길래 구현한 풀이 ㅎ
#답은 나오지만, 시간초과됨

s = int(input())

cnt = 0 
for i in range(1,s):
    for j in range(i+1):
        ans = i
        cnt +=1
        if cnt == s:
            break
    if cnt ==s:
        break
print(ans)
