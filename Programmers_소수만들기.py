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
def checkPrime(x): #소수를 확인하는 함수
    if x==2:
        return True
    if x==1 or x%2==0:
        return False
    for i in range(3,int(x**0.5)+1,2):
        if x%i==0:
            return False
    return True

def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                if checkPrime(nums[i]+nums[j]+nums[k]):
                    answer += 1


    return answer

