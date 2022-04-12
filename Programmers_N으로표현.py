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

#while문 속 for문 케이스를 생각 x, 55% 정답
#가져갈 것 --> 중복제거 set


# +
def cal(X,Y):
    n_set = set()
    for x in X:
        for y in Y:
            n_set.add(x+y)
            n_set.add(x*y)
            n_set.add(x-y)
            if y !=0:
                n_set.add(x//y)
    return n_set
    

def solution(N,number):
    answer = 0
    dp={}
    index = 1
    dp[index] ={N}
    while index <9:
        if number in dp[index]:
            return index
        index += 1
        tmp ={int(index*str(N))}

        for n in range(1,index):
            tmp.update(cal(dp[n],dp[index-n]))
        dp[index] = tmp

    return -1
            

    
    
    
print(solution(4,17),4)


# +
#고수의 풀이

# +
def calculate_n(X, Y):
    n_set = set()
    for x in X:
        for y in Y:
            n_set.add(x+y)
            n_set.add(x-y)
            n_set.add(x*y)
            if y != 0:
                n_set.add(x//y)
    return n_set

def solution(N, number):
    answer = -1
    result = {}   # key는 숫자 사용횟수, value는 숫자를 key번 사용했을 때 나오는 연산 결과셋
    result[1] = {N} # N을 1번 사용할 때는 그냥 N
    if number == N:
        return 1
    for n in range(2, 9):  # 8번까지만 계산하므로
        i = 1
        temp_set = {int(str(N)*n)}  # N=5, 2번 사용할 때 먼저 55를 저장
        # 1 (op) N-1.... n-1 (op) 1 까지 계산
        while i < n:
            temp_set.update(calculate_n(result[i], result[n-i]))
            i += 1
        # 만들어진 셋에 원하는 숫자가 있으면 stop
        if number in temp_set:
            answer = n
            break

        result[n] = temp_set

    return answer

print(solution(4,17),4)
