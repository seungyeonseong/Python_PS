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

def solution(d, budget):
    answer = 0
    n = 0
    d.sort()
    for i in d:
        n += i
        if n >budget:
            return answer
        else:
            answer += 1
    return answer
