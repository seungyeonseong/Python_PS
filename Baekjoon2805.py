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
###내풀이
#딱맞게 떨어지는 높이를 찾으면 출력, 못찾으면 반복문으로 최댓값 구하기

# +
n, m = map(int,input().split())

li = list(map(int,input().split()))


end = max(li)-1
start =1

while start <= end:
    mid = (start+end)//2
    
    ans = 0
    for i in li:
        if i >= mid:
            ans += i- mid
    if ans == m:
        print(mid)
        break
    elif ans > m:#오른쪽에서 찾아라
        start = mid +1
      
    else:
        end = mid -1
       
    #if start == end and ans != m:
    #print(mid)
    #    break

        
if ans!=m:
    while 1:
        ans = 0
        for i in li:
            if i >= mid:
                ans += i -mid
        if m <= ans:
            print(mid)
            break
        mid -= 1
#print(mid)

# +
#구글링__end는 m이 되도록 하는 값 중 최대에 멈춰서 이 때의 end를 반환

# +
n, m = map(int,input().split())

li = list(map(int,input().split()))


end = max(li)-1
start =1

while start <= end:
    mid = (start+end)//2
    
    ans = 0
    for i in li:
        if i >= mid:
            ans += i- mid
    if ans >= m:
        start = mid +1
      
    else:
        end = mid -1
print(end)#최대 높이인 end값 출력
# -


