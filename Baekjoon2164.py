from collections import deque
n = 4
q = deque([i for i in range(1,n+1)])

while len(q) >= 2:
    q.popleft()
    x = q.popleft()
    q.append(x)

print(q[0])
