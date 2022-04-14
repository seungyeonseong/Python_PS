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
##가지고 있는 숫자로 새로운 숫자만드는 방법->순열로 구현,,

# +
#조합하기
from itertools import permutations

#소수인지 확인하는 함수
def check_prime(x):
    if x==2:
        return True
    elif x%2==0 or x==1:
        return False
    num  = 3
    while num<x:   
        if x%num==0:
            return False
        num +=2
    return True

def solution(numbers):
    answer = 0
    li = []
    numbers = list(numbers)
    for i in range(1,len(numbers)+1):
        x = list(permutations(numbers,i))
        print(x)
        for j in x:
            t=""
            for k in j:
                t +=k
            li.append(int(t))
    li =set(li)
                
    
    for i in li:
        if check_prime(i):
            answer += 1    
    return answer

numbers ="17"
print(solution(numbers))

# +
#고수의 풓이_소수판별:에라토스테네스의 체
# -

from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)


# +
#고수의 풓이_조합만들기

# +
primeSet = set()


def isPrime(number):
    if number in (0, 1):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def makeCombinations(str1, str2):
    if str1 != "":
        if isPrime(int(str1)):
            primeSet.add(int(str1))

    for i in range(len(str2)):
        makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])


def solution(numbers):
    makeCombinations("", numbers)

    answer = len(primeSet)

    return answer


# +
#참고_에라토스테네스의 체
#1)2부터 N까지의 모든 자연수를 나열한다.
#2)남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
#3)남은 수 중에서 i의 배수를 모두 제거한다.i는 제거하지 않는다
#4)더 이상 반복할 수 없을 때까지 2),3)번 반복

# +
import math

n = 1000  #2부터 1000까지의 모든 수에 대하여 소수 판별
#처음엔 모든 수가 소수(True)인 것으로 초기화(0과1 제외)
array = [True for i in range(n+1)]

for i in range(2,int(math.sqrt(n))+1):  #2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True:  #i가 소수인 경우(남은 수인 경우)
        #i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i*j <= n:
            array[i*j] = False
            j += 1
#모든 소수 출력
for i in range(2,n+1):
    if array[i]:
        print(i,end=" ")
