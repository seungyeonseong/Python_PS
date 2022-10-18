import sys
input = sys.stdin.readline

n = int(input())
top = list(map(int,input().split()))
stack = []
stack.append([top[0],0])
ans =[0]*n

for idx,i in enumerate(top):
    while stack:
        if stack[-1][0] > i:
            ans[idx] = stack[-1][1]+1
            break
        else:
            stack.pop()

    stack.append([i,idx])

print(*ans)
