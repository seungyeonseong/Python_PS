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
def solution(survey, choices):
    answer = ''

    li = ["R","T","C","F","J","M","A","N"]
    d = {}
    for type in li:
        d[type] = 0

    #점수 매기기
    for idx,score in enumerate(choices):
        if score >=5:
            d[survey[idx][1]] += score-4
        elif score <=3:
            d[survey[idx][0]] += 4-score

    return check(d)


def check(d):    #최종 성격 유형
    ans = ""
    if d['R'] >= d['T']:
        ans += "R"
    else:
        ans += "T"
    if d['C'] >= d['F']:
        ans += "C"
    else:
        ans += "F"
    if d['J'] >= d['M']:
        ans += "J"
    else:
        ans += "M"
    if d['A'] >= d['N']:
        ans += "A"
    else:
        ans += "N"

    return ans
