import sys
input = sys.stdin.readline
n = int(input())
li= list(map(int,input().split()))

li = sorted(li)
#이분탐색
def binary_search(array,target,start,end):
    while start < end:
        if array[start]+array[end] == target:
            return True
        elif array[start] + array[end] > target:
            end -= 1
        else:
            start +=1
    return False
total = 0

for idx,target in enumerate(li):
    arr=[]
    for i in range(len(li)):
        if i != idx:
            arr.append(li[i])
    if binary_search(arr,target,0,len(arr)-1):
        total += 1

print(total)
