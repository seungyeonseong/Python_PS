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
#내풀이_못품 ㅠ
#접근법:첫번째 공유기를 중간에 설치, 이분 탐색으로 설치하고자함
#문제점 -> 중간위치한 공유기가 설치대상이 아닐수도,,접근이 틀림

# +
#답안예시
#각 집의 좌표가 최대 10억이므로, 이진 탐색 이용하여 해결
#'가장 인접한 두 공유기 사이의 거리'의 최댓값을 찾아야하므로, C보다 많은 개수로
#공유기를 설치할 수 있다면 '가장 인접한 두 공유기 사이의 거리'의 값을 증가시켜서,
#더 큰 값에 대해서도 성립하는지 체크하기 위해 다시 탐색 수행 -->파라메트릭 서치 유형

# +
#집의 개수(N)와 공유기 개수(C)를 입력받기
n,c = map(int,input().split())

#전체 집의 좌표 정보를 입력받기
array= []
for _ in range(n):
    array.append(int(input()))
array.sort()    #이진 탐색 수행을 위해 정렬 수행

start = 1  #가능한 최소 거리(min gap)
end =  array[-1] - array[0]  #가능한 최대 거리(max gap)
result = 0

while(start <= end):
    mid = (start+end)//2  #mid는 가장 인접한 두 공유기 사이의 거리(gap)를 의미
    value = array[0]
    count = 1
    #현재의 mid값을 이용해 공유기를 설치
    for i in range(1,n):  #앞에서부터 차근차근 설치
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c:    #c개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        start = mid + 1
        result = mid  #촤적의 결과를 저장
    else:  #C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid -1
print(result)

# +
#재귀로 구현한 내 풀이,,,,진심 맞왜틀임;;;;

# +
#import sys
#input = sys.stdin.readline


n, c = map(int, input().split())
home = []
for _ in range(n):
    home.append(int(input()))
home.sort()

max_gap = home[-1] - home[0]
min_gap = 1


def func(home,min_gap, max_gap):
    cnt = 1
    gap = (max_gap + min_gap) // 2

    if min_gap == max_gap:
        return gap

    x = home[0]
    for i in range(1, n):
        if home[i] - x >= gap:
            cnt += 1
            x = home[i]
    if cnt < c:
        max_gap = gap-1
        return func(home,min_gap, max_gap)
    else:
        min_gap = gap +1
        return func(home,min_gap, max_gap)


print(func(home,min_gap, max_gap))
# -

# ### 


