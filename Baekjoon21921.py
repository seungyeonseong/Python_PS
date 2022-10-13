import sys
input =sys.stdin.readline

n,x = map(int,input().split())
visitor = list(map(int,input().split()))

tmp = sum(visitor[:x])
res = [tmp,1]
for i in range(x,n):
    tmp -= visitor[i-x]
    tmp += visitor[i]
    if res[0] < tmp:
        res[0] = tmp
        res[1] = 1
    elif res[0] == tmp:
        res[1] += 1
if res[0]==0:
    print("SAD")
else:
    print(res[0])
    print(res[1])