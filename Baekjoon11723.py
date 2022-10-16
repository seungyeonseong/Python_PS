import sys
input = sys.stdin.readline
m = int(input())
s = set()
for _ in range(m):
    x = input().strip()
    if x == "all":
        s = set([i for i in range(1,21)])
        continue
    elif x == "empty":
        s = set()
        continue
    a,b = x.split(" ")
    if a == "add" and int(b) not in s:
        s.add(int(b))
    elif a == "remove" and int(b) in s:
        s.remove(int(b))
    elif a == "check":
        if int(b) in s:
            print(1)
        else:
            print(0)
    elif a == "toggle":
        if int(b) in s:
            s.remove(int(b))
        else:
            s.add(int(b))