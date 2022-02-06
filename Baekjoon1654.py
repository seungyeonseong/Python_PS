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
##시간초과 --> 이분 탐색 활용해야함

# +
k,n = map(int,input().split())

li = []
for i in range(k):
    li.append(int(input()))

def func(li,length):
    num = 0
    for i in li:
        num += i//length
    if num == n-1:
        return num
    return False

length = 1
while 1:
    
    if func(li,length) != False:
        print(length-1)
        break
    length += 1


# +
###메모리 초과 (재귀)

# +
k,n = map(int,input().split())
li = []
for i in range(k):
    li.append(int(input()))
array = [i for i in range(1,max(li)+1)]



def bin_search(array,start,end):
   
    mid = (start+end)//2
    ans = 0
    for i in li:
        ans += i //array[mid]
    if ans == n-1:
        return array[mid]
    elif ans > n-1: #length가 오른쪽
        start = mid +1
        bin_search(array,start,end)
    elif ans < n-1: #왼쪽 찾아야함
        end = mid-1
        bin_search(array,start,end)
        
print(bin_search(array,0,len(array)-1)-1)
    
    
        


# +
##구글링

# +
k,n = map(int,input().split())
li = []
for i in range(k):
    li.append(int(input()))

start = 1
end = max(li)

while start <= end:
    
    mid = (start+end)//2
    ans = 0
    for i in li:
        ans += i //mid
        
    if ans >= n: #length가 오른쪽
        start = mid +1

    else: #왼쪽 찾아야함
        end = mid-1
        
        
print(end)
    
    
        
# -

print(func(li,))

print(array)


