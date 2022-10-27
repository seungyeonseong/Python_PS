import sys
input = sys.stdin.readline
n,k = map(int,input().split())
li = list(input().rstrip())

cnt = 0
for idx,i in enumerate(li):
    if i == "P":
        for j in range(idx-k,idx+k+1):
            if j>=n or j <0:
                continue
            if li[j] == "H":
                cnt += 1
                li[j] = "X"
                break
print(li)
print(cnt)