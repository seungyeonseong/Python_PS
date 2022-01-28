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
n = int(input())
li=[]

#리스트에 스케줄 받기
for i in range(n):
    a,b = map(int,input().split())
    li.append([a,b])
    
#정렬
li = sorted(li,key=lambda x:(x[1],x[0]))
#sorted(li,key=lambda x:x[0])

#print(li)
end = li[0][1]
cnt = 1

for i in range(1,n):
    #다음 회의의 시작 시간이 기존 회의 종료시간보다 늦어야함
    if li[i][0] >= end:
        cnt += 1
        end = li[i][1] #종료시간 갱신
print(cnt)
    
#print(li)
