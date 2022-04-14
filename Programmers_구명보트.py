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
#pop으로 풀었다가 시간복잡도때문에 효율이랑 시간초과 난리남
# -

def solution(people, limit):
    answer = 0
    people = sorted(people)
    idx =0
    back_idx = len(people)-1
    num = 0

    while idx <= back_idx:
        if idx == back_idx:
            return answer + 1

        if (limit - people[back_idx]) >= people[idx]:
            num += 2
            answer += 1
            idx += 1
            back_idx -= 1

        else:
            num += 1
            answer += 1
            back_idx -= 1

        if num == len(people):
            return answer
