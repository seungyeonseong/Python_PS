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
###구글링
#LCS_최장 공통 부분 수열
# -

# LCS(Xi, Yj)를 문자열 X, Y 각각의 i, j번째 글자까지의 최장 공통 부분 문자열의 길이라고 했을 때
#
# X[i] == Y[j]일 때
# LCS(Xi, Yj) = LCS(Xi - 1, Yj - 1) + 1
#
# X[i] != Y[j]일 때
# LCS(Xi, Yj) = LCS(Xi - 1, Yj - 1)
# LCS(Xi, Yj) = max(LCS(Xi - 1, Yj), LCS(Xi, Yj - 1))
#
#
# 1. X[i] == Y[j]
# 먼저 X[i] == Y[j]일 때는 각 문자열에 X[i], Y[j]가 추가되기
# 이전의 LCS의 길이(= LCS(Xi - 1, Yj - 1))에 1만큼 더해주면 된다.
# 이는 직관적으로 이해할 수 있다.
#
# 2. X[i] != Y[j]
# 다음으로 X[i] != Y[j]일 때 마지막 글자가 다르다고 각 문자열에 X[i], Y[j]가 추가되기 이전의 LCS의 길이(= LCS(Xi - 1, Yj - 1))를 그대로 가져오면 LCS의 길이를 손해볼 수 있다.
# 문자열 ACB와 ABA를 예로 들어보자. 문자열 ACB와 ABA의 LCS는 AB이다. 하지만 마지막 글자인 B와 A가 다르다고 LCS(X3 - 1, Y3 - 1)를 그대로 가져오면 LCS는 A가 되어 버리는 것이다.
# 그래서 우리는 마지막 글자가 다를 때에는 각 문자열의 마지막 글자들이 따로 한 글자씩 추가 되었을 때의
# LCS (= LCS(Xi - 1, Yj), LCS(Xi, Yj - 1) ) 중 큰값을 가져와야 한다.

# +
import sys

fst = list(sys.stdin.readline().strip())
sec = list(sys.stdin.readline().strip())

dp = [[0] * (len(sec)+1) for _ in range(len(fst)+1)]
for i in range(1,len(fst)+1):
    for j in range(1,len(sec)+1):
        if fst[i-1] == sec[j-1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])

# -


