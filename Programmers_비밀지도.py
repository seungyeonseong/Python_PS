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
#1. 10진법 ->2진법 변환
#2. 배열 두 개 합친 후 배열로 출력

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        x1 = bin(arr1[i])[2:]
        x2 = bin(arr2[i])[2:]
        total=""
        if len(x1)!= n:
            x1 = "0"*(n-len(x1))+x1
        if len(x2) != n:
            x2 = "0"*(n-len(x2))+x2

        for k in range(len(x1)):
            if x1[k]=="1"or x2[k]=="1":
                total +="#"
            else:
                total +=" "
        answer.append(total)

    return answer
