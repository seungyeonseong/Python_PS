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
word = input()
word = list(word.upper())
cnt=[]
for i in range(26):
    cnt.append(0)
#print(word)

#빈도수 세기
for i in range(65,91):
    for j in word:
        if chr(i) == j:
            cnt[i-65] += 1 
#print("cnt")
#print(cnt)

#최댓값 가지는 값 
m=[]
for k in range(26):
    if cnt[k] == max(cnt):
        #print(k)
        m.append(chr(k+65))
#print(m)

#출력
if len(m) >= 2:
    print("?")
else:
    print(m[0])
        
        
        
#print(max(word))
#print(word)
# -




