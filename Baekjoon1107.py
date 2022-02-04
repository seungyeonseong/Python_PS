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
#누를 수 있는 범위의 모든 경우의 수일 때 최솟값을 갱신함

# +
n = int(input())
m = int(input())
broken_num = list(input().split())

def possible_num(x):
    x = list(str(x))
    for i in x:
        if i in broken_num:
            return False
    return True

answer = abs(n-100)
for temp in range(1000001):
    if possible_num(temp) is True:
        answer  = min(answer, len(str(temp))+abs(n-temp))
print(answer)
        

# -

###아래가 내풀이###
#접근법: target번호에 근접한 값을 최소, 최대로 각 각 구하려고함..
#엄청 긴 풀이랑 예외처리,,,


# +
n = list(input())
m = int(input())
broken_num = list(map(int,input().split()))

min_result =[]
max_result = []


#고장난 리모콘 버튼 제거
remote_num = [i for i in range(10) if i not in broken_num]

idx=0

    
for i in range(len(n)):
    if int(n[i]) not in remote_num:
        idx = i
        break
    if i == len(n)-1 and int(n[i]) in remote_num:
        idx = -1
        
if len(broken_num) == 10:
    min_result=[0 for i in range(len(n))]
    max_result=[0 for i in range(len(n))]
    idx = -2

if idx == 0:
    for i in range(len(remote_num)-1,-1,-1):
        if remote_num[i] < int(n[idx]):
            min_result.append(remote_num[i])
            break
    
    for i in range(len(remote_num)):
        if remote_num[i]> int(n[idx]):
            max_result.append(remote_num[i])
            break
            
    if len(min_result) ==0:
        min_result.append(0)
    if len(max_result) ==0:
        max_result.append(0)

if idx >0:
    for i in range(idx):
        min_result.append(int(n[i]))
        max_result.append(int(n[i]))
    for j in range(len(remote_num)-1,-1,-1):
        if remote_num[j] < int(n[idx]):
            min_result.append(remote_num[j])
            break
    for j in range(len(remote_num)):
        if remote_num[j] > int(n[idx]):
            max_result.append(remote_num[j])
            break
if idx == -1:
    min_result = n
    max_result = n
        
           
#나머지 못채운 숫자 채우기
if len(n) != len(min_result):
    for i in range(len(n)-len(min_result)):
        min_result.append(max(remote_num))
if len(n) != len(max_result):
    for i in range(len(n)-len(max_result)):
        max_result.append(min(remote_num))
        
#cnt += len(n) 
#print(min_result)
#print(max_result)
#print(len(max_result))


real = ""
for i in n:
    real += i
real = int(real)

a, b ="",""
for i in min_result:
    a += str(i)
a = int(a)
for j in max_result:
    b += str(j)
b = int(b)

if a<=real and b>=real:
    print(min(abs(real-100),len(list(str(a)))+real-a,len(list(str(b)))+b-real))
elif a<real and b<real:#b가 없다
    print(min(abs(real-100),len(list(str(a)))+real-a))
elif a> real and b>real:
    print(min(abs(real-100),len(list(str(b)))+b-real))
else:
    print(abs(real-100))





