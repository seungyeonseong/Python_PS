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

##구글링,,,-30001설정해서 갱신하는 법,,,공부하기
#해맨 이유:routes를 차량이 나간 지점 (진출) 기준으로 정렬


# +
def solution(routes):
    answer = 0
    cam = -30001
    routes.sort(key=lambda x:x[1]) 
    for n,i in enumerate(routes):
        if i[0] <= cam:
            continue
        else:
            answer += 1
            cam = i[1]

    return answer

print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2


# +
#정렬잘못해서 0점맞은 내풀이 ㅎ
#x:x[0] => x:x[1]로 바꿔주니까 100점맞음ㅋㅋ
# -

def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    v = [False]*len(routes)
    for n,i in enumerate(routes):
        if v[n] is True:
            continue
        start,end = i
        v[n]  =  True
        answer += 1
        for j in range(n+1,len(routes)):
            if routes[j][0] <= end and v[j] is False:
                v[j] = True
            else:
                break

    return answer
