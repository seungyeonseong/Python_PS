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
#import sys
#input = sys.stdin.readline

def dfs(x, y):
    # 방문 확인
    global cnt
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if li[x][y] == 1:

        cnt += 1
        li[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


# 입력
n = int(input())
li = []
# 인접 행렬
for i in range(n):
    li.append(list(map(int, input())))


cnt = 0
array = []
result = 0
for i in range(n):
    for j in range(n):  # 주변에 1들을 하나로 묶기, cnt로 바꾸기
        if dfs(i, j) == True:
            array.append(cnt)
            result += 1
            cnt = 0

print(result)
array.sort()
if len(array) == 0:
    print(0)
else:
    for i in array:
        print(i)

