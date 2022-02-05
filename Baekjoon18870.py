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
##내풀이_시간초과 --> 아마 중복값때문인듯
# -

n = int(input())
li = list(map(int,input().split()))
for i in li:
    ans = 0
    arr = []
    for j in li:
        if i > j and j not in arr:
            arr.append(j)
            ans += 1
        
        
    print(ans,end=" ")
        


# +
n = int(input())
li = list(map(int,input().split()))


s = set(li)
res=[]

for i in s:
    ans = 0
    for j in s:
        if i > j:
            ans += 1     
    res.append((i,ans))

for i in li:
    for j in res:
        if i == j[0]:
            print(j[1],end =" ")

# +
###구글링__딕셔너리 활용
#1_리스트 안에서 자기보다 작은 숫자의 개수를 세는 것이므로 자신이 리스트 안에서의 크기 순서를 출력
#2_딕셔너리는 key 중복 허용 x, key가 중복될 경우 마지막에 입력된 key의 value를 출력

# +
n = int(input())
li = list(map(int,input().split()))

arr = sorted(list(set(li)))
dic ={arr[i]:i for i in range(len(arr))}
for i in li:
    print(dic[i],end=" ")


# -


