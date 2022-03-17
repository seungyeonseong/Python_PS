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

# +
###k보다 작은 것:mid//i (??)or 최대 n개
#처음에 이해하기 힘들었다,,,
#만약 4행에서 mid=7보다 작은 수 개수 구하려면, 
#7//4해서 1개가 나오는것,,만약 1행이면 7//1=7이지만, 최대개수는 n이므로
##-> min(mid//i,n)을 누적합해서 k와 비교! 
#k보다 작으면 범위를 늘리고 크면 범위를 줄인다 

# +
n = int(input())
k = int(input())

start = 1
end = k ##k번째 수는 k보다 클 수 없다
while start <= end:
    mid = (start+end)//2
    tmp = 0
    for i in range(1,n+1):    #mid보다 작은 수의 개수 구하기 
        tmp += min(mid//i,n)  #최대 n개,,
    if tmp < k:
        start = mid +1
    else:
        end = mid -1
print(start)


# +
#대각선 값 기준으로 모든 배열만들어서 b[k] 찾으려니 메모리 초과남

#->배열 b를 직접 만드는게 아닌듯

# +
#중복갯수를 가지는 배열 b로 다시만들었지만 역시나 메모리 초과

# +
def binary_search(array,target,start,end):
    while start <= end:
        mid = (start+end)//2
        if array[mid][0] <= target:
            start = mid +1
        else:
            end = mid -1
    return arr[mid][1]
            

n = int(input())
arr = []
total =0
for i in range(1,n+1):
    for j in range(i,n+1):
        if i == j:
            total += 1
            arr.append((total,i*j))
        else:
            total += 2
            arr.append((total,i*j))
            
k = int(input())

print(binary_search(arr,k,0,len(arr)))
# -


