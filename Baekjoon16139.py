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
##sys로 문자열 input할때 rstrip()안해줘서 인덱스에러 삽질함
# -

import sys
input = sys.stdin.readline
s = input().rstrip()
q = int(input())
alp_li = set(s)
li = [[0]*len(s) for i in range(ord('a'),ord('z')+1)]
for i in alp_li:
    cnt = 0
    for n,j in enumerate(s):
        if i == j:
            cnt+=1
        li[ord(i)-97][n] = cnt
for _ in range(q):
    alp,l,r = input().split()
    if int(l)>0:
        res = li[ord(alp)-97][int(r)]-li[ord(alp)-97][int(l)-1] 
    else:
        res = li[ord(alp)-97][int(r)]
    sys.stdout.write(str(res)+'\n')

