### 백준 #20055
### 컨베이어 벨트 위의 로봇

from collections import deque


#1. n, k
n,k=map(int,input().split())


#2. belt
belt=deque(list(map(int,input().split())))


#3.
step=0
robot=deque([0 for _ in range(n)])



while True:
    #3-0. 스텝 +1
    step+=1

    #3-1. 벨트랑 로봇  한 칸 회전
    robot[n-1]=0  #회전할 때 마지막 칸에 있는 로봇은 바닥에 내려와야
    belt.appendleft(belt.pop())
    robot.appendleft(robot.pop())
    
    
    #3-2. 가장 먼저 벨트에 올라간 로봇부터 한칸 이동
    for i in range(n-1,-1,-1):
        if robot[i]==1:
            #로봇이 맨 마지막칸이면 로봇 내려감
            if i==n-1:
                robot[i]=0
            else:
                #다음 칸에 로못이 없고 내구도가 1 이상이면 로봇 이동
                if robot[i+1]==0 and belt[i+1]>0:
                    robot[i]=0
                    robot[i+1]=1
                    belt[i+1]-=1

    
    #3-3. 올라가는 위치에 로봇이 없다면 로봇 올리기
    if robot[0]==0 and belt[0]>0:
        robot[0]=1
        belt[0]-=1

    
    #3-4. 내구도가 0인 칸의 개수가 k개 이상이면 과정종료
    if belt.count(0)>=k:
        break

print(step)
            
            
    
    
    
    
