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

def solution(nums):
    answer = 0
    n = len(nums)/2
    nums = set(nums)
    if len(nums) >= n:
        answer = n
    else:
        answer = len(nums)
    
    return answer
