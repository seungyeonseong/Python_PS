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

# ####구글링 --> 삽질삽질개삽질
# #힌트)스택으로 해결

def solution(number, k):
    answer = ''
    stack=[]
    for i,num in enumerate(number):
        while stack and stack[-1] <num and k>0:
            stack.pop()
            k -= 1   
        if k == 0:
            stack += number[i:]
            break
        stack.append(num)     
    if k >0:
        stack = stack[:-k] ##제거 횟수 k를 다 사용하지 않았을 경우 뒤에서부터 자르기
    answer = ''.join(stack)
    return answer
