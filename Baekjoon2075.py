#graph를 따로 만들었더니 메모리초과
#tmp보다 큰 값만 push했더니 시간초과 -> 큐 개수로 수정

import heapq
import sys
input = sys.stdin.readline
n = int(input())

q = []
for _ in range(n):
    li = list(map(int,input().split()))
    for num in li:
        if len(q) < n:
            heapq.heappush(q,num)
        else:
            if q[0] < num:
                heapq.heappop(q)
                heapq.heappush(q,num)

print(q[0])

