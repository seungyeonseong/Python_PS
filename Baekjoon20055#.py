from collections import deque
import sys
input = sys.stdin.readline

# n,k = 3,2
# belt = [1,2,1,2,1,2]
n,k = map(int,input().split())
belt = deque(map(int,input().split()))
robot = deque([0]*2*n)

step = 1
while True:
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한칸 회전
    belt.rotate(1)
    robot.rotate(1)
    robot[n-1] = 0
    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 이동
    #이동하려는 칸에 로봇이 없고, 그 칸 내구도가 1 이상 남아야 이동 가능
    for i in range(n-2,-1,-1):
        if robot[i] and not robot[i+1] and belt[i+1]:
            belt[i+1] -= 1
            robot[i+1],robot[i] = robot[i],0
    robot[-1] = 0
    if not robot[0] and belt[0]:
        robot[0] = 1
        belt[0] -= 1
    if belt.count(0)>=k:
        print(step)
        break
    step +=1