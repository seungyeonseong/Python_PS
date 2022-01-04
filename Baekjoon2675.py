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
word = list(input())
st = ord('a')
fn = ord('z')
li=[]
#알파벳별로 처음 등장하는 위치 저장
for i in range(st,fn+1): #a
    for j in range(len(word)):#baekjoon
        if chr(i) == word[j]:
            li.insert(i-97,j)
            break
        elif chr(i) != word[j] and j == len(word)-1:
            li.insert(i-97,-1)
for k in li:
    print(k,end=" ")


        
# -

n = int(input())#테스트 개수
for i in range(n):
    m = list(input().split())
    rep = int(m[0])
    li = list(m[1])
    for j in range(len(li)):
        for k in range(rep):
            print(li[j],end="")
    print(" ")
#print(li) 



