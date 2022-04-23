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

# 타겟과 거리 구할때 <맨해튼 거리>사용해야함

# +

def solution(numbers, hand):
    answer = ''
    num = [[1,2,3],[4,5,6],[7,8,9],[10,0,12]]
    left,right = 10,12
    for i in numbers:
        if i%3==0 and i!=0:
            right = i
            answer +="R"
        elif i%3==1:
            left = i
            answer +="L"
        else: #가운데 처리
            for x in range(4):
                for y in range(3):
                    if num[x][y] ==i:
                        target = [x,y]
                    if num[x][y] ==left:
                        l =[x,y]
                    if num[x][y] == right:
                        r = [x,y]
            dist_l = abs(target[0]-l[0])+abs(target[1]-l[1])
            dist_r = abs(target[0]-r[0])+abs(target[1]-r[1])
            if dist_l == dist_r:
                if hand =="left":
                    left = i
                    answer += "L"
                else:
                    right = i
                    answer += "R"
            elif dist_l<dist_r:
                left = i
                answer += "L"
            else:
                right = i
                answer += "R"
        print(left,right)
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

print(solution(numbers,hand))
print("LRLLLRLLRRL")
# -


