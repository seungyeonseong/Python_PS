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
a,b,v = map(int,input().split())
import math

day = math.ceil((v-a)/(a-b)+1)

print(day)


# +
#입력
t = int(input())

for _ in range(t):
    h, w, n = map(int,input().split())
    #호텔 층 수:6, 각 층의 방 수:12, 몇번째손님인지:10->402호
    #1~6/7~12/...
    if n//h +1 >= 10:
        n//6
        print(str(n%h)+str(n//h+1))
    else:
        print(str(n%h)+str(0)+str(n//h+1))

# +
#입력
t = int(input())

for _ in range(t):
    h, w, n = map(int,input().split())
    if n%h == 0:
        print(str(h),end="")
    else:
        print(str(n%h),end="")
    if n//h +1 >= 10:
        print(str(n//h+1))
    else:
        print(str(0)+str(n//h+1))
    
# -

8%6

# +
#입력
t = int(input())

for _ in range(t):
    h, w, n = map(int,input().split())
    if n%h == 0:
        print(str(h),end="")
    else:
        print(str(n%h),end="")
        
    if n//h +1 >= 10:
        if n%h == 0:
            print(str(h)+str(n//h))
        else:
            print(str(h)+str(n//h+1))
    else:
        if n%h ==0:
            print(str(h)+str(0)+str(n//h))
        else:
            print(str(h)+str(0)+str(n//h+1))

# +
#1~6/7~12/13~18...

#입력
t = int(input())

for _ in range(t):
    h, w, n = map(int,input().split())
    li=[]
    for i in range(1,w+1):
        for j in range(1,h+1):
            if i<10:
                li.append(str(j)+str(0)+str(i))
            else:
                li.append(str(j)+str(i))
    print(li[n-1])

# -


