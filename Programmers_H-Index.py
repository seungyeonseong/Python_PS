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
##처음에 이분탐색으로 열심히 구현했지만,,똥효율이라 런타임에러폭탄
# -

def solution(citations):
    citations.sort()
    answer = 0
    for i in range(0,len(citations)):
        if len(citations)-i <= citations[i]:
            answer = max(answer,len(citations)-i)
    return answer


def solution(citations):
    answer = 0
    start = 0
    end = max(citations)
    while start <= end:
        m = (start+end)//2
        if start == end:
            return m
        left = m
        right = len(citations)-m+1
        if m == citations[m]: left +=1
        if left <= m and right >= m:
            start = m
        else:
            end = m -1
                
            
        return start
