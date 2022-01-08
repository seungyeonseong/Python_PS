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
total = 1
cnt =0
#벌집층
#1/2~7(6)/8~19(12)/20~37(18)/38~61(24)

#i가 300까지 돌아야 n의 최댓값 수용가능
if n == 1:
    cnt +=1
else:
    while n > total:
        total += 6*cnt
        cnt += 1
#print(total)        
print(cnt)  
        
# -

total=1
for i in range(10):
    total += 6*i
    print(total)

# +
for i in range(300):
        total += 6*i
        if total >= 1000000000:
            print(i)
            break
        
print(total)
print(i) 
# -


