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
#내풀이

# +

def solution(lottos, win_nums):
    answer = []
    inter = 0
    unknown=0
    for i in lottos:
        for j in win_nums:
            if i==j:
                inter +=1
        if i==0:
            unknown +=1
    maxx = unknown + inter
    if maxx >6:
        maxx= 6
    elif maxx <1:
        maxx = 1
    answer.append(7-maxx)
    minn = inter
    if minn <=1:
        minn = 1
    answer.append(7-minn)
    return answer


# +
###고수의 풀이
# -

def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    
    cnt_0 = lottos.count(0)
    ans =0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0+ans],rank[ans]
