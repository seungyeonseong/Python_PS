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

def solution(brown, yellow):
    answer = []
    for i in range(1,int(yellow**0.5)+1):
        if yellow %i == 0:
            x= yellow//i
            y= i
            if brown ==2*x+2*y+4:
                answer = [x+2,y+2]
    return answer
