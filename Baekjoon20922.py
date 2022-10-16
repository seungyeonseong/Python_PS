import sys
input = sys.stdin.readline
n,k = map(int,input().split())
li = list(map(int,input().split()))

cnt = [0]*(100001)
left,right = 0,0
total = 0
while right < n:
    if cnt[li[right]] < k:
        cnt[li[right]] += 1
        right += 1
    else:
        cnt[li[left]] -=1
        left += 1
    total = max(total,right-left)
print(total)