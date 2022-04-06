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
#내접근,,,구현 x
#초당 최대 처리량: 1초간 처리하는 요청의 최대 개수

#1.처리 시작 시간 구하기=처리 종료 시간 - 처리시간
#2.1초간 최대 개수 구하기
#->끝시간 기준으로 1초 이내 있는 로그 모두 확인

# +
#고수의 풀이
# -

#정수형으로 시간을 변환하는 코드
def get_time(time):
    hour = int(time[:2])*3600
    minute = int(time[3:5])*60
    second = int(time[6:8])
    millisecond = int(time[9:])
    return (hour + minute + second )*1000 + millisecond


#시작 시간을 구하는 코드
def get_start_time(time,duration_time):
    n_time = duration_time[:-1] #"s"제외
    int_duration_time = int(float(n_time)*1000)
    return get_time(time)-int+duration_time +1


# +
lines= ["2016-09-15 01:00:04.001 2.0s","2016-09-15 01:00:07.000 2s"]

#전체 코드
def solution(lines):
    answer = 0
    start_time = []
    end_time = []
    
    for t in lines:
        time = t.split(" ")
        start_time.append(get_start_time(time[1],time[2]))
        end_time.append(get_time(time[1]))
        
    for i in range(len(lines)):
        cnt = 0
        cur_end_time = end_time[i]
        for j in range(i,len(lines)):
            if cur_end_time > start_time[j] -1000:
                cnt += 1
        answer = max(answer,cnt)
    return answer
    
def get_time(time):
    hour = int(time[:2])*3600
    minute = int(time[3:5])*60
    second = int(time[6:8])
    millisecond = int(time[9:])
    return (hour + minute + second )*1000 + millisecond

def get_start_time(time,duration_time):
    n_time = duration_time[:-1] #"s"제외
    int_duration_time = int(float(n_time)*1000)
    return get_time(time)-int_duration_time +1

print(solution(lines))
# -


