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
###구글링
#내풀이는 연속으로 같은 연산자가 나올 경우 처리를 못함
#N시간 쏟고도 못풀었따 ㅂㄷㅂㄷ

# +
from itertools import permutations

def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))
    
def calculate(exp,op):
    array=[]
    tmp=""
    for i in exp:
        if i.isdigit()==True:
            tmp+=i
        else:
            array.append(tmp)
            array.append(i)
            tmp=""
    array.append(tmp)
    
    for o in op:
        stack=[]
        while len(array)!=0:
            tmp=array.pop(0)
            if tmp==o:
                stack.append(operation(stack.pop(), array.pop(0), o))
            else:
                stack.append(tmp)
        array=stack
            
    return abs(int(array[0]))

def solution(expression):
    op = ['+', '-', '*']
    op = list(permutations(op, 3))
    result=[]
    for i in op:
        result.append(calculate(expression, i))
    return max(result)


expression = "100-200*300-500+20"
print(solution(expression))

# +
#그지같은 내풀이ㅠ

# +
from itertools import permutations
    
def solution(expression):
    total=[]
    op = ["*","+","-"]
    op = list(permutations(op,3))
    arr = []
    tmp=""
    for i in expression:
        if i.isdigit()==True:
            tmp +=i
        else:
            arr.append(tmp)
            arr.append(i)
            tmp = ""
    arr.append(tmp)
    
    for i in op:
        result = []
        stack=[]
        for n,k in enumerate(arr):
            if k==i[0]:
                stack.append(result.pop())
                stack.append(k)
                
               # result.append(str(eval(arr[n-1]+k+arr[n+1])))
            else:
                result.append(k)
            if arr[n-1] ==i[0]:
                result.pop()
                
       # return result
        result2=[]
        for n,k in enumerate(result):
            if k==i[1]:
                result2.pop()
                result2.append(str(eval(result[n-1]+k+result[n+1])))
            else:
                result2.append(k)
            if result[n-1] ==i[1]:
                result2.pop()
       # return result2
        total.append(abs(eval("".join(result2))))
    answer =max(total)
    return answer

expression = "100-200*300-500+20"
print(solution("5+5+5+5"))
