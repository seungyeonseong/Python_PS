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
##구글링
#수학문제,,,아이디어못떠올려서 큰일,,이해될듯말듯
#전체사각형 수 -(너비+높이-최대공약수)

# +
def check(w,h):#최대공약수
    x = 1
    answer = 0
    while x<=w:
        if w%x==0 and h%x==0:
            answer = x
        x+=1
    return answer

def solution(w,h):
    answer = w*h
    if w>h:
        w,h = h,w

    answer -= (w+h-check(w,h))
    return answer
