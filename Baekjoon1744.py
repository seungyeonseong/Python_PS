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
for i in range(n):
    li.append(int(input()))
    
def func(li):
    #양수/음수로 나누기
    minus=[]
    plus=[]
    total = 0
    li.sort()
    for i in li:
        if i <0:
            minus.append(i)
        elif i>0:
            plus.append(i)
    #음수개수가 짝수면        
    if len(minus)%2 ==0 and len(minus)>0:
        for i in range(0,len(minus)-1,2):
            total += minus[i]*minus[i+1]  
    elif len(minus)%2==1:#음수개수가 홀수이면
        if 0 in li: #0이 있으면
            minus.remove(minus[-1])
            for i in range(0,len(minus)-1,2):
                total += minus[i]*minus[i+1]
        else:    #0이 없으면
            for i in range(0,len(minus)-2,2):
                 total += minus[i]*minus[i+1]
            total += minus[-1]
            
    plus.reverse()
    #양수처리
    while plus.count(1) >0:
        total +=1
        plus.remove(1)
    if len(plus)%2==0 and len(plus)>0:
        for i in range(0,len(plus)-1,2):
            total += plus[i]*plus[i+1] 
    elif len(plus)%2 ==1:
        for i in range(0,len(plus)-2,2):
            total += plus[i]*plus[i+1] 
        total += plus[-1]
    
    return total

print(func(li))
        
