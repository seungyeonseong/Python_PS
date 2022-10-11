import sys
input = sys.stdin.readline

n,m = map(int,input().split())
keyword = dict()
for _ in range(n):
    keyword[input().rstrip()] = 1
ans = n

for _ in range(m):
    li = list(input().rstrip().split(","))

    for i in li:
        if i in keyword.keys():
            if keyword[i] == 1:
                keyword[i] -=1
                ans -= 1

    print(ans)



