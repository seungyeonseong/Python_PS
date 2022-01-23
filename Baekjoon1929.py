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
#소수의 판별_동빈책466pg

# +
#백준 1929번 풀이
import math 

m,n= map(int,input().split())

def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num%i ==0:
                return False
        return True
        
for i in range(m, n+1):
    if isPrime(i):
        print(i)


# +
#최초 코드

#소수 판별 함수
def is_prime_number(x):
    #2부터 (x-1)까지의 모든 수를 확인하며
    for i in range(2,x):
        #x가 해당 수로 나누어 떨어진다면
        if x%i==0:
            return False #소수가 아님
    return True #소수임

print(is_prime_number(4))
print(is_prime_number(7))

# +
#개선된 소수 판별 알고리즘
#제곱근까지만 확인하면 됨
import math

#소수 판별 함수
def is_prime_number(x):
    #2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2,int(math.sqrt(x))+1):
        #x가 해당 수로 나누어 떨어진다면
        if x%i==0:
            return False #소수가 아님
    return True #소수임

print(is_prime_number(4))
print(is_prime_number(7))

# +
#에라토스테네스의 체
#여러 개의 수가 소수인지 아닌지를 판별할 때 사용하는 대표적인 알고리즘

import math

n = 1000 #2부터 1000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n+1)] #처음 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

#에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n))+1):#2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: #i가 소수인 경우(남은 수인 경우)
        #i를 제외한 i의 모든 배수를 지우기
        j =2
        while i*j <= n:
            array[i*j] = False
            j += 1
            
#모든 소수 출력
for i in range(2,n+1):
    if array[i]:
        print(i,end=' ')



# +
import math
m,n= map(int,input().split())
#n = 1000 #2부터 1000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(2,n+1)] #처음 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

#에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n))+1):#2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: #i가 소수인 경우(남은 수인 경우)
        #i를 제외한 i의 모든 배수를 지우기
        for j in range(i*2, len(array),i):
            array[j] = False
            
#모든 소수 출력
for i in range(m,n+1):
    if array[i]==True:
        print(i)
# -


