import sys
input =sys.stdin.readline

p,m = map(int,input().split())
room = []
# player=[]
# for _ in range(p):
#     x,y = input().rstrip().split()
#     player.append([y,int(x)])
player = [['a', 10], ['b', 15], ['c', 20], ['d', 25], ['e', 30], ['f', 17], ['g', 18], ['h', 26], ['i', 24], ['j', 28]]

for name,level in player:
    flag = False
    for i in range(len(room)):
        if len(room[i])==m:
            continue

        if abs(level-room[i][0][1]) <= 10:
            flag = True
            room[i].append([name,level])
            break
    if not flag:
        room.append([[name,level]])

print(player)
for i in range(len(room)):
    if len(room[i]) ==m:
        print('Started!')
        for j in sorted(room[i],key=lambda x:x[0]):
            print(j[1],j[0])
    else:
        print('Waiting!')
        for j in sorted(room[i],key=lambda x:x[0]):
            print(j[1],j[0])




#맞왜틀,,,,풀이
# from collections import deque
# import sys
# input =sys.stdin.readline
#
# p,m = map(int,input().split())
# room = deque()
# for _ in range(p):
#     x,y = input().rstrip().split()
#     room.append([y,int(x)])
# s = []
# cnt = 0
# while room:
#     if len(s)==0:
#         s.append((room.popleft()))
#     else:
#         if abs(room[0][1]-s[0][1]) <= 10:
#             s.append((room.popleft()))
#         else:
#             x,y = room.popleft()
#             room.append((x,y))
#
#     cnt += 1
#     if len(s)==m:
#         print("Started!")
#         for i in sorted(s,key=lambda x:x[0]):
#             print(i[1],i[0])
#         s = []
#         cnt = 0
#     elif cnt > p:
#         print("Waiting!")
#         for i in sorted(s,key=lambda x:x[0]):
#             print(i[1],i[0])
#         s = []
#         cnt = 0