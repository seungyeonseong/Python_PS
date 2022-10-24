import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int,input().split()))
m = int(input())
# n = 5
# li = [70,80,30,40,100]
# m = 450

amount = m//n
start = amount
end = max(li)
ans = 0

while start <= end:
    mid = (start+end)//2
    tmp = 0
    for i in li:
        if i > mid:
            tmp += mid
        else:
            tmp += i

    if tmp > m:
        end = mid -1
    else:
        ans = mid
        start = mid+1


print(ans)
