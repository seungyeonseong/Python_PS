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
#자카드 유사도:두 집합의 교집합 크기/합집합 크기
#모두 공집합일 경우 자카드 유사도는 1

# +
str1="FRAN__CE"
str2="french"

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    answer = 0
    s1=[]
    s2=[]
    for i in range(len(str1)-1):
        x = str1[i:i+2]
        for i in x:
            res = True
            if 'z'<i or i<'A'or i=="_":
                res = False
                break
        if res:
            s1.append(x)

    for i in range(len(str2)-1):
        x = str2[i:i+2]
        for i in x:
            res = True
            if 'z'<i or i<'A'or i=="_":
                res = False
                break
        if res:
            s2.append(x)
  
    s = set(s1+s2)
    mmax,mmin = 0,0
    for i in s:
        mmax += max(s1.count(i),s2.count(i))
        mmin += min(s1.count(i),s2.count(i))
    return int(mmin/mmax*65536)
  
print(solution(str1,str2))
# -



