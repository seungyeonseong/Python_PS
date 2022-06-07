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
#Knapsack 배낭 채우기 
# -

# 풀이: 가방 무게의 최대 값k부터 역순으로 들어갈 물건의 무게w까지 순회하면서 해당 위치의 최대 가치와 들어갈 물건의 무게 w만큰 이전의 최대 가치에 물건의 가치 v를 더한 값 중 최댓값을 구한다.

# [아이디어]
# 1.dp문제임을 파악했다면, subproblem을 잘 정의해야함
# 2.이전의 경우로부터 물건을 추가하거나/추가하지 않는 것 중 하나 선택
# 3.해당 문제는 <i:물건의 개수, j:배낭의 무게 제한>이므로 2차원 배열 필요
# 4.각 물건들을 가지고 k이하의 모든 배낭들을 채우거나 채우지 않으면서 각 순간 최대 가치(v)를 업데이트 해나감
# 5.knapsack problem 중 각 물건이 1개씩 존재하거나 쪼갤 수 없는 0-1problem에 해당

# +
#구글링
#냅색알고리즘: 담을 수 있는 물건이 나눌 수 있냐 없냐에 따라 나눈다
#1)담을 수 있는 물건이 나누어 질때 => 분할 가능 배낭 문제
#2)담을 수 있는 물건이 나누어 질 수 없을 때 => 0-1배낭 문제

#해당 문제는 2)으로 물건을 담을때 허용무게보다 넣을 물건의 무게가 
#더 크다면 넣지 않는다. 그렇지않는다면, 현재넣을 물건의 무게만큼 빼고
#현재물건을 넣거나 이전그대로 가지고 간다.

# +
n,k = map(int,input().split())
thing=[[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    thing.append(list(map(int,input().split())))
for i in range(1,n+1):
    for j in range(1,k+1):
        w = thing[i][0]
        v = thing[i][1]
        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j],d[i-1][j-w]+v)
print(d[n][k])
# -


