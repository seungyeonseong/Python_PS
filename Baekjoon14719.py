# h,w = 4,8
# li = [3,1,2,3,4,1,1,2]
#가장 높은 벽만날때까지
import sys
input = sys.stdin.readline
h,w = map(int,input().split())
li = list(map(int,input().split()))
total =0

for idx in range(1,w-1):
    left = max(li[:idx])
    right = max(li[idx+1:])
    m = min(left,right)
    if m > li[idx]:
        total += m-li[idx]

print(total)


