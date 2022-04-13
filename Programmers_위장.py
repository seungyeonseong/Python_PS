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

#3*2-1

def solution(clothes):
    answer = 1
    d =dict()
    for i in clothes:
        if i[1] not in d:
            d[i[1]] = 1
        else:
            d[i[1]] += 1
    for i in d:
        answer *= (d[i]+1)
    answer -= 1


    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))
