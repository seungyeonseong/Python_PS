import sys
from collections import deque
input = sys.stdin.readline


n,m = map(int,input().split())
li = list(map(int,input().split()))
# n,m = 10,10
# li = [1,6,3,2,7,9,8,4,10,5]
q = deque([i for i in range(1,n+1)])
cnt = 0
for i in li:
    idx = q.index(i)
    if idx <= len(q)//2:
        while q[0] != i:
            q.rotate(-1)
            cnt +=1
            if q[0] == i:
                break
        q.popleft()
    else:
        while q[0] != i:
            q.rotate()
            cnt += 1
            if q[0] == i:
                break
        q.popleft()
print(cnt)

