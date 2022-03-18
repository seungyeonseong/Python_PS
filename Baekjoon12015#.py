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
#dp로 풀었던 문제,,이분탐색으로 아이디어가 도저히 떠오르지 않음
# -

# LIS;가장 긴 증가하는 부분 수열
# -->  일반적인 방법은 DP이용, 시간 복잡도 개선을 위해서는 이분탐색 이용

# +
#1.이분탐색:수열이 들어갈 자리를 이분탐색으로 찾는 방법

#벡터를 생성하고 최솟값 하나를 넣어둠
#입력받은 수 x와 벡터의 끝 값 back을 비교해서 x가 더 크다면 push back하고
#길이 변수 cnt를 1 증가
#back이 x보다 크거나 같다면 lower bound를 찾고 그 위치에 x넣는다

# +
#import sys
#input =sys.stdin.readline

n = int(input())
array = list(map(int,input().split()))
stack = [0]    #LIS 리스트

def binary_search(target,start,end):
    while start <= end:
        mid = (start +end)//2
        
        if stack[mid] < target:
            start = mid +1
        else:
            end = mid-1
    return start

for i in array:
    if stack[-1] < i:
        stack.append(i)
    else:
        stack[binary_search(i,0,len(stack)-1)] = i #교체

print(len(stack)-1)    #실제 LIS는 아니지만 '길이'조건 만족
print(stack)

# +
#2. bisect

# +
from bisect import bisect_left

n = int(input())
array = list(map(int,input().split()))
stack = [0]   

for i in array:
    if stack[-1] <i:
        stack.append(i)
    else:
        stack[bisect_left(stack,i)] = i
        
print(len(stack)-1)
print(stack)


# +
#예제: 1 3 4 2 5 6 7 인 경우 stack불러오면
#실행 결과->1 2 4 5 6 7로 나옴
#실제 답: 1 3 4 5 6 7

#실제 LIS 와 다르지만 길이의 값에는 영향을 주지 않아서 이런 풀이를 사용하는듯,,,

# +
#import sys
#input = sys.stdin.readline

def binary_search(target,start,end):
    while start <= end:
        mid = (start+end)//2
        if target > stack[mid]:
            start = mid+1
        else:
            end = mid -1
    return start

n = int(input())
array = list(map(int,input().split()))
stack = [0]

for i in array:
    if stack[-1] < i:
        stack.append(i)
    else:
        stack[binary_search(i,0,len(stack)-1)]=i
        
print(len(stack)-1)
        

# -

stack


