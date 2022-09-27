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

def solution(s):
    answer = [0,0]

    while True:
        if s == "1":
            return answer
        answer[0] +=1
        cnt = 0
        for l in list(s):
            if l=="1":
                cnt +=1    #1.x의 모든 0 제거
        answer[1] += len(list(s))-cnt
        s = bin(cnt)[2:]    #2. 이진변환
