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
p = "(()())()"

def check(p):#"올바른 괄호 문자열"확인 함수
    left,right = 0,0
    for i in p:
        if i =="(":
            left += 1
        else:
            right +=1
        if right>left:
            return False
    return True
def index(p):
    left,right =0,0
    for n,i in enumerate(p):
        if i =="(":
            left += 1
        else:
            right += 1
        if left ==right:
            return n
            
        
def sol(p):
    answer = ""
    if len(p) ==0:
        return answer
    #u와 v로 분리
    idx = index(p)
    u = p[:idx+1]
    v = p[idx+1:]
    if check(u):
        answer = u +sol(v)
    else:
        answer = "("
        answer += sol(v)
        answer += ")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] =="(":
                u[i] = ")"
            else:
                u[i] = "("
        answer += "".join(u)
    return answer
    
print(sol(p))
# -



