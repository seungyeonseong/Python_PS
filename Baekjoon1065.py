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
cnt = 0

sub=[]

for i in range(1, n+1):
    if i <= 99:   #99이하의 정수는 모두 한수
        cnt += 1
    else:         #100이상이면 자릿수 구분
        j = i
        li=[]
        while j>=10:
            li.append(j%10)
            j = j//10
        li.append(j)
        li.reverse()
        d= li[1]-li[0]
        #print(li)
        for k in range(1,len(li)-1):#k=1,2
            if (li[k+1]-li[k]) != d:
                break
            else:
                cnt += 1
        
        
       
    
print(cnt)
        
   
# -


