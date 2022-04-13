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
#네자릿수 비교 하는 법-->** list[:4]*4 
# -

def solution(numbers):
    answer = ''
    num = []

    #순서대로 큰 숫자로 정렬
    for n,i in enumerate(numbers):
        num.append((n,list(str(i)[:4]*4)))
    num.sort(key = lambda x: x[1],reverse=True)
    #4자릿수 비교
    for n,i in num:
        answer += str(numbers[n])
    if answer[0] =="0":
        return "0"
