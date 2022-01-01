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

n = int(input())
#n번 반복
for _ in range(n):
    score = []
    cnt= 0
    score = list(map(int,input().split()))
    #print("score_b")
    #print(score)
    scorenum = score[0]
    for j in range(1,len(score)):
        score[j-1] = score[j]
    score[-1]=0      #마지막 값 안없애면 중복됨
    #print("score_a")
    #print(score)
    m = sum(score)/scorenum
    #print(m)
    for k in score:
        if k > m:
            cnt += 1
    pro = '{:.3f}'.format(round(cnt/scorenum*100,3))
    print(pro+"%")   #공백없이 출력


