##문자열 입력받을 때 sys.stdin.readline 앞뒤 공백 처리 주의
import sys
#sys.setrecursionlimit(10*9)

# s = list(input())
# t = list(input())
s = input()
t = input()
# s = "BAAAAABAA"
# t = "BAABAAAAAB"
def dfs(t):
    if t == s:
        print(1)
        sys.exit()
    if len(t) == 0:
        return 0
    if t[-1] == "A":
        dfs(t[:-1])
    if t[0] == "B":
        dfs(t[1:][::-1])
    #print(x)

dfs(t)
print(0)

#시간초과 풀이 -> s=>t로 하면 경우의 수가 너무 많음, 거꾸로 t=>s로 만들어야함
# li =[]
# li.append(s)
# while len(li[0]) < len(t):
#     new = []
#     for i in li:#뒤에 A추가
#         x = i + "A"
#         new.append(x)
#          #뒤에 B추가, 뒤집기
#         x = i + "B"
#         new.append("".join(reversed(list(x))))
#     li = new
# if t in set(li):
#     print(1)
# else:
#     print(0)

# print(li)





